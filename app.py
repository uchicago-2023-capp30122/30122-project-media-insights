import streamlit as st
import pandas as pd
from media_insights.plotting.ts_plots import plot_comment_ts, plot_sentiment_ts
from media_insights.plotting.ts_plots import plot_comment_cumsum_ts
from media_insights.plotting.word_cloud import plot_wordcloud
from PIL import Image

main_df = pd.read_json("media_insights/data/preprocessed_comments.json")

st.set_page_config(layout="wide", page_title="Your media analytics")


st.title("Media Insights")
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
    st.altair_chart(sentiment_ts_chart)

with col2:
    # Cumulative comments over time
    comment_cumsum_ts_chart = plot_comment_cumsum_ts(main_df, p3)
    st.altair_chart(comment_cumsum_ts_chart, use_container_width=True)
