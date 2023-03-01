import pandas as pd
import altair as alt

def plot_comment_ts(df: pd.DataFrame, title: str):
    """
    Plot the change in sentiment for a video over time

    Parameters:
        df (pd.DataFrame): A pandas dataframe to plot with columns "date" and "sentiment"
        title (str): A title for the plot

    Returns:
        An altair Chart object
    """
    # The base plot
    ts_plot = alt.Chart(df).mark_line().encode(
        alt.X(f"yearmonthdatehours(date):T", 
              title="",

              # Only displays the first and last ticks and labels
              # Found suggestion on Stack Overflow from user jakevdp
              # https://stackoverflow.com/questions/59699412/altair-display-all-axis-ticks-but-only-some-tick-labels
              axis=alt.Axis(tickCount=df.shape[0])),
        alt.Y("sentiment", 
              title="Sentiment")
    ).properties(
        title=video_title
    )

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

