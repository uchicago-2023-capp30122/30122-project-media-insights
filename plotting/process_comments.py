"""
Author: Darren Colby
"""

import re
import json
import translators
import pandas as pd
from autocorrect import Speller
from time import sleep
from flair.models import TextClassifier
from flair.data import Sentence

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

with open("data/cleaned_comment_data.json",'r') as f:
    data = json.loads(f.read())

raw_comments = pd.json_normalize(data)


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


def preprocess_comments(raw_comments: pd.Series, fast: bool=False):
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

    for comm_lst in raw_comments:
        for comm in comm_lst:
            text, date = comm[0], comm[1]
            no_emojis = remove_emojis(text)
            no_newline = re.sub(r'[\r\n\t]', '', no_emojis)
            no_punct = re.sub(r'[^\w\s]', '', no_newline)
            no_extra_space = re.sub(r'\s+', ' ', no_punct)
            lowercase = no_extra_space.strip().lower()

            if fast:
                better_spelling = corrector(lowercase)
                clean_comments.append(better_spelling); clean_dates.append(date)
            else:
                translation = translators.translate_text(lowercase)

                # Spell checking
                better_spelling = corrector(translation)

                # Avoid getting blocked
                sleep(1)
                clean_comments.append(better_spelling); clean_dates.append(date)

    return pd.DataFrame(zip(clean_comments, clean_dates), columns=['text', 'date'])

