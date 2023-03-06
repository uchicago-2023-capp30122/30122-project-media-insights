"""
Author: Darren Colby
"""

import re
import json
import translators
import pandas as pd
import spacy
from autocorrect import Speller
from time import sleep
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Credit: https://stackoverflow.com/questions/51217909/removing-all-emojis-from-text
EMOJI_PATTERN = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF" 
        u"\U0001F680-\U0001F6FF" 
        u"\U0001F1E0-\U0001F1FF" 
        u"\U0001F1F2-\U0001F1F4" 
        u"\U0001F1E6-\U0001F1FF" 
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)

def remove_emojis(text: str):
    """
    Remove emojis from strings

    Parameters:
        text (str): The input string

    Returns:
        (str) The string with emojis removed
    """
    cleaner_text = EMOJI_PATTERN.sub(r'', text)

    return cleaner_text


def regex_fix(text: str):
    """
    Fixes strings by removing emojis, newlines, tabs, carriage returns, punctuation, 
    whitespace, and digits and converts to lowercase

    Parameters:
        text (str): The text to clean

    Returns:
        (str) Cleaned text
    """
    no_emojis = remove_emojis(text)
    no_newline = re.sub(r'[\r\n\t]', '', no_emojis)
    no_bracket = re.sub(r" ?\([^)]+\)", "", no_newline)
    no_punct = re.sub(r'[^\w\s]', '', no_bracket)
    no_extra_space = re.sub(r'\s+', ' ', no_punct)
    lowercase = no_extra_space.strip().lower()
    no_digits = re.sub(r'[0-9]+', '', lowercase)

    # Remove hyperlinks
    no_links = re.sub(r'http\S+', '', no_digits)
    no_links = re.sub(r"[!@#$]", '', no_links)

    return no_links


def preprocess_comments(raw_comments: pd.Series, fast: bool=False, series: bool=False):
    """
    Preprocess comments by removing emojis, newline, tab, and carriage return characters; 
    removing punctuation and extra spaces; converting to lowercase; spell checking; and 
    translating them to English
    Parameters:
        raw_comments (pd.Series): Raw comments to preprocess
        fast (bool): If this is set to False, translation to English is performed
    Returns:
        (pd.DataFrame) A dataframe with text and date columns for a given video
    """
    clean_comments, clean_dates = [], []
    corrector = Speller()

    # Download lemmas and stopwords if needed
    try:
        en_model = spacy.load('en_core_web_lg', disable = ['parser','ner'])
    except:
        spacy.cli.download("en_core_web_lg")
        en_model = spacy.load('en_core_web_lg', disable = ['parser','ner'])

    STOP_WORDS = en_model.Defaults.stop_words

    for comm_lst in raw_comments:
        for comm in comm_lst:
            text, date = regex_fix(comm[0]), comm[1]
            
            if text == '':
                continue

            if fast:
                # Spell checking
                better_spelling = corrector(text)
            else:
                # Translate to english
                sleep(1)
                translation = translators.translate_text(text)

                better_spelling = corrector(translation)

            # Lemmatize and remove stopwords
            doc = en_model(better_spelling)
            clean_doc = " ".join([tok.lemma_ for tok in doc 
                                  if tok.lemma_ not in STOP_WORDS and len(tok.lemma_) > 1])

            clean_comments.append(clean_doc); clean_dates.append(date)

    if series:
        return pd.Series(clean_comments)

    return pd.DataFrame(zip(clean_comments, clean_dates), columns=['text', 'date'])
            

def calculate_comment_sentiment(text: str):
   """
   Calculate the sentiment polarity score using VADER

   Parameters:
    text (str): The text to analyze

    Returns:
        (float) The compound sentiment score
   """
   return SentimentIntensityAnalyzer().polarity_scores(text)['compound']


def preprocess_transcripts():
    """
    Cleans transcripts from videos
    """
    def process_comment(comment: str):
        corrector = Speller()
        try:
            en_model = spacy.load('en_core_web_lg', disable = ['parser','ner'])
        except:
            spacy.cli.download("en_core_web_lg")
            en_model = spacy.load('en_core_web_lg', disable = ['parser','ner'])

        text = regex_fix(comment)
        better_spelling = corrector(text)
        STOP_WORDS = en_model.Defaults.stop_words

        doc = en_model(better_spelling)
        clean_doc = " ".join([tok.lemma_ for tok in doc 
                            if tok.lemma_ not in STOP_WORDS and len(tok.lemma_) > 1])
        
        return clean_doc

    transcripts = pd.read_json("media_insights/data/transcript_data.json").T
    new_cols = [vid for vid in transcripts.iloc[:, 0] if vid is not None]
    transcripts = transcripts.iloc[:, 1:]
    transcripts.columns = new_cols
    transcripts = transcripts.applymap(lambda x: x if x is not None else {"text": ""})
    transcripts = transcripts.applymap(lambda x: "".join(list(x["text"])))
    transcripts = transcripts.apply(lambda x: process_comment(str(x))).T
    transcripts = pd.DataFrame(transcripts).rename_axis("vid")
    transcripts.reset_index(inplace=True)
    transcripts.columns = ["vid", "text"]
    transcripts.to_json("media_insights/data/transcript_data.json")


def main():
    """
    Reads in a json file with raw comments from a youtube video, removes emojis, hyperlinks,
    and other problematic characters, converst them to lowercase, removes stopwords, 
    translates words to English, and lemmatizes them.
    """
    with open("media_insights/data/cleaned_comment_data.json",'r') as f:
        data = json.loads(f.read())

    raw_comments = pd.json_normalize(data)

    clean_text = preprocess_comments(raw_comments.iloc[:, 0])
    clean_text['sentiment'] = clean_text.apply(lambda r: calculate_comment_sentiment(r.text), 
                                            axis=1)
    clean_text.to_json("media_insights/data/preprocessed_comments.json")

    similarity_comments = raw_comments.apply(preprocess_comments, series=True)
    similarity_comments.to_json("media_insights/data/similarity_data.json")

    preprocess_transcripts()


if __name__ == '__main__':
    main()
