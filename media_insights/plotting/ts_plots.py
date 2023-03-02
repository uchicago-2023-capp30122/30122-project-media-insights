"""
Authored by Darren Colby
"""

import pandas as pd
import altair as alt

def plot_ts(df: pd.DataFrame, title: str, y_col: str, y_title: str, caption: bool):
    """
    Base function for plotting time series. Essentially this is a python version of multiple
    dispatch.

    Parameters:
        df (pd.DataFrame): The dataframe to plot
        title (str): The title for the plot
        y_col (str): The columnt to use for the y-axis
        y_title (str): The title for the y-axis
        caption (bool): Should only be True for sentiment time series

    Returns:
        An altair line plot
    """
    # The base plot
    ts_plot = alt.Chart(df).mark_line(color="#0868ac").encode(
        alt.X(f"yearmonthdatehours(date):T", 
              title="",

              # Only displays the first and last ticks and labels
              # Found suggestion on Stack Overflow from user jakevdp
              # https://stackoverflow.com/questions/59699412/altair-display-all-axis-ticks-but-only-some-tick-labels
              axis=alt.Axis(tickCount=df.shape[0])),
        alt.Y(y_col, 
              title=y_title)
    ).properties(
        title=title
    )

    # Only adds caption for sentiment time series
    if caption:
        # The caption, which is not a property in the Chart class
        # Found solution on Stack Overflow by user jakevdp
        # https://stackoverflow.com/questions/57244390/how-to-add-a-subtitle-to-an-altair-generated-chart
        caption = alt.Chart(
            {"values": [{"text": 
                        "Sentiment ranges from -1 for most negative to +1 for most positive"}]}
        ).mark_text(align="left").encode(
            text="text:N"
        )

        final_plot = alt.vconcat(
            ts_plot,
            caption
        )

        return final_plot
    
    return ts_plot


def plot_sentiment_ts(df: pd.DataFrame, title: str):
    """
    Plot time series for sentiment of comments on a video

    Parameters:
        df (pd.DataFrame): A dataframe with "date" and "sentiment" columns
        title (str): A title for the plot

    Returns:
        An altair line chart
    """
    return plot_ts(df, title, "sentiment", "Sentiment", True)


def plot_comment_ts(df: pd.DataFrame, title: str):
    """
    Plot time series for the number of comments on a video

    Parameters:
        df (pd.DataFrame): A dataframe with "date" and "sentiment" columns
        title (str): A title for the plot

    Returns:
        An altair line chart
    """
    new_df = df.copy(deep=True)
    new_df = new_df.date.value_counts().rename_axis("date").reset_index(name="counts")

    return plot_ts(new_df, title, "counts", "Comments", False)

