"""
    Authored by Jessup Jong and edited by Darren Colby
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import wordcloud


def plot_wordcloud(df: pd.DataFrame):
    """
    Plot a word cloud for comments on a channel
    Input:
        pandas dataframe: originally did not have any input, but edited
            to be compatibale and usable from the plotting functions. 

    Returns:
        png image file with a dog word cloud.
    """
    total_text = "".join([string for string in df.text])

    dog_mask = np.array(Image.open(f"media_insights/data/dog.png"))

    word_cloud_inst = wordcloud.WordCloud(
        mask=dog_mask,
        scale=0.65,
        background_color="white"
    )

    dog_colors = wordcloud.ImageColorGenerator(dog_mask)
    dog_word_cloud = word_cloud_inst.generate(total_text)

    plt.figure(dpi=600)

    plt.imshow(dog_word_cloud.recolor(color_func=dog_colors))

    plt.axis("off")

    plt.savefig("media_insights/data/wordcloud.png")

