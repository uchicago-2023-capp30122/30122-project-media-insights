"""
Authored by Darren Colby
"""

import pandas as pd
import altair as alt
from prophet import Prophet
from itertools import product
from gensim.models import KeyedVectors

glove = KeyedVectors.load("media_insights/data/glove.d2v")


def get_forecast(df: pd.DataFrame, lead: int):
    """
    Make a forcast on time series data

    Parameters:
        df (pd.DataFrame): A dataframe with "x" and "date" columns
        lead (int): The number of periods to forecast

    Returns:
        A dataframe with actual and predicted values
    """
    # Prophet requires "ds" and "x" columns and altair doesn't like timezones
    ts_df = df[["date", "x"]].rename(columns={"date": "ds", "x": "y"})
    ts_df["ds"] = ts_df.ds.dt.tz_localize(None)

    df2 = df.copy(deep=True)
    df2["forecast"] = "Actual"

    model = Prophet()
    model.fit(ts_df)
    future_df = model.make_future_dataframe(periods=lead)
    forecast = model.predict(future_df)[["ds", "yhat"]].rename(columns={"ds": "date", 
                                                                    "yhat": "x"})
    forecast["forecast"] = "Predicted"

    return pd.concat([forecast, df2[["date", "x", "forecast"]]])


def plot_ts(df: pd.DataFrame, title: str, y_col: str, y_title: str, caption: bool, 
            lead: int):
    """
    Base function for plotting time series data and forecasts

    Parameters:
        df (pd.DataFrame): The dataframe to plot
        title (str): The title for the plot
        y_col (str): The columnt to use for the y-axis
        y_title (str): The title for the y-axis
        caption (bool): Should only be True for sentiment time series
        lead (int): The number of periods to forecast into the future

    Returns:
        An altair line chart
    """
    df_to_plot = get_forecast(df, lead)

    # Have to convert to datetime and remove timezone for altair
    df_to_plot["date"] = pd.to_datetime(df_to_plot.date, utc=True)

    # The base plot
    ts_plot = alt.Chart(df_to_plot).mark_line().encode(
        alt.X(f"yearmonthdatehours(date):T", 
              title="",

              # Only displays the first and last ticks and labels
              # Found suggestion on Stack Overflow from user jakevdp
              # https://stackoverflow.com/questions/59699412/altair-display-all-axis-ticks-but-only-some-tick-labels
              axis=alt.Axis(tickCount=df_to_plot.shape[0])),
        alt.Y(y_col, 
              title=y_title),
        color=alt.Color(
            "forecast:N",
            scale=alt.Scale(range=["steelblue", "orange"]),
            legend=alt.Legend(title="",
                              orient="bottom")
        )
    ).properties(
        title=title,
        width=300,
        height=300
    )


    # Only adds caption for sentiment time series
    if caption:
        # The caption, which is not a property in the Chart class
        # Found solution on Stack Overflow by user jakevdp
        # https://stackoverflow.com/questions/57244390/how-to-add-a-subtitle-to-an-altair-generated-chart
        # It might not show due to 
        caption = alt.Chart(
            {"values": [{"text": 
                        "Sentiment ranges from -1 for most negative to +1 for most positive"
                        }]}
        ).mark_text(align="left").encode(
            text="text:N",
        )

        ts_plot = alt.vconcat(
            ts_plot,
            caption
        )
    
    return ts_plot


def plot_sentiment_ts(df: pd.DataFrame, lead:int):
    """
    Plot time series data and forecast for sentiment of comments on a video

    Parameters:
        df (pd.DataFrame): A dataframe with "date" and "sentiment" columns
        lead (int): The number of periods to forecast into the future

    Returns:
        An altair line chart
    """
    df_copy = df.copy(deep=True)
    df_copy["x"] = df_copy.sentiment

    return plot_ts(df_copy, "Changes in Sentiment", "x", "Sentiment", True, lead)

 
def plot_comment_ts(df: pd.DataFrame, lead: int):
    """
    Plot time series for the number of comments on a video

    Parameters:
        df (pd.DataFrame): A dataframe with "date" and "sentiment" columns
        lead (int): The number of periods to forecast into the future

    Returns:
        An altair line chart
    """
    new_df = df.copy(deep=True)
    new_df = new_df.date.value_counts().rename_axis("date").reset_index(name="x")

    # Extra characters in title due to streamlit but
    # See https://github.com/streamlit/streamlit/issues/5467
    return plot_ts(new_df, "``Comments over time", "x", "Comments", False, lead)


def plot_comment_cumsum_ts(df: pd.DataFrame, lead: int):
    """
    Plot time series for the cumulative number of comments on a video

    Parameters:
        df (pd.DataFrame): A dataframe with "date" and "sentiment" columns
        lead (int): The number of periods to forecast into the future

    Returns:
        An altair line chart
    """
    new_df = df.copy(deep=True)
    new_df = new_df.date.value_counts().rename_axis("date").reset_index(name="x")
    new_df["date"] = pd.to_datetime(new_df.date)
    new_df.sort_values("date", inplace=True)
    new_df["x"] = new_df["x"].cumsum()

    # Extra characters in title due to streamlit but
    # See https://github.com/streamlit/streamlit/issues/5467
    return plot_ts(new_df, "``Cumulative comments", "x", "Comments", False, lead)


def plot_cosine_similarity(df: pd.DataFrame):
    """
    Plot a heatmap of the cosine similarity of comments from different videos

    Parameters:
        df (pd.DataFrame): Dataframe to use for potting

    Returns:
        An altair chart
    """
    df.fillna("", inplace=True)

    all_comments = [" ".join(lst) for lst in  df.T.values.tolist()]
    perm1, perm2 = [], []
    similarities = []
    id1, id2 = [], []

    for p1, p2 in product(all_comments, all_comments):
        perm1.append(p1); perm2.append(p2)
        similarities.append(glove.n_similarity(p1.split(), p2.split()))

    for (vid1, vid2) in product(df.columns, df.columns):
        id1.append(vid1); id2.append(vid2)

    similarities_df = pd.DataFrame(list(zip(perm1, perm2, id1, id2, similarities)), 
                                columns=["p1", "p2", "vid1", "vid2", "Cosine similarity"])

    base = alt.Chart(similarities_df).mark_rect().encode(
        x=alt.X('vid1:O',
                title="Video ID"),
        y=alt.Y('vid2:O',
                title="Video ID"),
        color='Cosine similarity:Q',
    ).properties(
        height=300,
        width=300,
        title="Comment similarity"
    )

    return base
