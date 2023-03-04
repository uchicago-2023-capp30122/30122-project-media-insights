"""
    Authored by Jessup Jong and Darren Colby
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import wordcloud


def plot_wordcloud(df: pd.DataFrame):
    """
    Plot a word cloud for comments on a channel

    Returns:
        A matplotlib object
    """
    total_text = "".join([string for string in df.text])

    dog_mask = np.array(Image.open(f"media_insights/data/dog2.png"))

    word_cloud_inst = wordcloud.WordCloud(
        mask=dog_mask,
        contour_width=1.5,
        contour_color="#b58900",
        background_color="#002b36"
    )

    dog_colors = wordcloud.ImageColorGenerator(dog_mask)
    dog_word_cloud = word_cloud_inst.generate(total_text)

    plot = plt.figure(dpi=600, facecolor='#002b36')
    plt.tight_layout(pad=0)

    plt.imshow(
        dog_word_cloud.recolor(color_func=dog_colors),
        interpolation="bilinear",
    )

    plt.axis("off")

    plt.savefig("media_insights/data/wordcloud.png")

