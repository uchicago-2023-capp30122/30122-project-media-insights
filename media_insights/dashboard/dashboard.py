import streamlit as st
import pandas as pd
from ts_plots import plot_comment_ts, plot_sentiment_ts
from PIL import Image

main_df = pd.read_json("media_insights/data/preprocessed_comments.json")

st.set_page_config(layout="wide", page_title="Your media analytics")

st.title("Media Insights")

st.text("Here are the latest analytics from your channel")

image = Image.open('media_insights/data/word_cloud1.png')
st.image(image, caption='Top words from your comments section', width=700)

periods = st.slider("Number of periods to forecast", 0, 365, step=1, value=7)

col1, col2 = st.columns(2)

with col1:
    comment_ts_chart = plot_comment_ts(main_df, periods)
    st.altair_chart(comment_ts_chart, use_container_width=True)

with col2:
    sentiment_ts_chart = plot_sentiment_ts(main_df, periods)
    st.altair_chart(sentiment_ts_chart, use_container_width=True)