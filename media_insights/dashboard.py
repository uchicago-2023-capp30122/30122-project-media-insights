import streamlit as st
import pandas as pd
from plotting.ts_plots import plot_comment_ts, plot_sentiment_ts, plot_cosine_similarity
from plotting.ts_plots import plot_comment_cumsum_ts, plot_comment_ts
from plotting.word_cloud import plot_wordcloud
from PIL import Image

INTRO = """
           Get insights into your user inteaction on YouTube. This tool enables you to
           quickly see trends in comments and sentiments in your videos. The time series 
           predictions are powered by Prophet, a time series library developed at Facebook,
           that separately models day, month, year, and autoregression components using 
           Bayesian Markov Chain Monte Carlo. Sentiment classification is based on VADER
           using preprocessed text. When conducting sentiment classification, the program 
           removes emojis, newlines, tabs, carriage returns, punctuation, and numbers before
           translating any foreign text to English and correcting misspelled words."""

main_df = pd.read_json("media_insights/data/preprocessed_comments.json")
similarity_df = pd.read_json("media_insights/data/similarity_data.json")

st.set_page_config(layout="wide", page_title="Your media analytics")


st.title("Media Insights")
st.text(INTRO)
st.text("Here are the latest analytics from your channel")

# Make sidebar with sliders to change forecasts
with st.sidebar:
    st.markdown("## Forecast Settings")
    st.markdown("You can **change** how far out to forecast.")
    p1 = st.slider('Comments', min_value=0, max_value=365, step=1, value=7)
    p2 = st.slider('Cumulative comments', min_value=0, max_value=365, step=1, value=7)
    p3 = st.slider('Sentiment', min_value=0, max_value=365, step=1, value=7)
    st.text('-1 is negative and +1 is positive')

# plot_wordcloud saves the plot to an image because plotting it is slow
plot_wordcloud(main_df)
image = Image.open('media_insights/data/wordcloud.png')
st.image(image, caption='Top words from your comments section', width=700)

col1, col2 = st.columns(2)

with col1:
    # Comments over time
    comment_ts_chart = plot_comment_ts(main_df, p1)
    st.altair_chart(comment_ts_chart, use_container_width=True)

    # Sentiment time series
    sentiment_ts_chart = plot_sentiment_ts(main_df, p3)
    st.altair_chart(sentiment_ts_chart, use_container_width=True)

with col2:
    # Cumulative comments over time
    comment_cumsum_ts_chart = plot_comment_cumsum_ts(main_df, p3)
    st.altair_chart(comment_cumsum_ts_chart, use_container_width=True)

    # Cosine similarity of video ids
    cosine_chart = plot_cosine_similarity(similarity_df)
    st.altair_chart(cosine_chart, use_container_width=True)
