import altair as alt
import vega_datasets
import pandas as pd
from scraping.comments import get_comments

#df = vega_datasets.data.stocks()

#def plot_comment_ts(df: pd.DataFrame, x: str, y:str):
    #alt.Chart(df).mark_line().encode(
        #x='x',
        #y="y"
    #)

#plot_comment_ts(df, "date", "price")

get_comments()
