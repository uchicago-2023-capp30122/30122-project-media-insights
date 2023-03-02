"""
    Authored by Jessup Jong
"""

import matplotlib.pyplot as plt
import json
import numpy as np
from PIL import Image
import wordcloud


def plot_wordcloud():
    """
    Plot a word cloud for comments on a channel

    Returns:
        A matplotlib object
    """
    with open("../data/preprocessed_comment_data.json", "r") as f:
        text = json.load(f)

    total_text = " ".join(
        [
            comment[0]
            for key in text
            for comment in text[key]
        ]
    )

    dog_mask = np.array(Image.open(f"../data/dog.png"))

    DPI = 1000

    word_cloud_inst = wordcloud.WordCloud(
        background_color="white",
        mask=dog_mask,
        width=2000,
        height=2000,
    )

    dog_colors = wordcloud.ImageColorGenerator(dog_mask)
    dog_word_cloud = word_cloud_inst.generate(total_text)

    plot = plt.figure(figsize=(10, 10), dpi=DPI)

    plot.imshow(
        dog_word_cloud.recolor(color_func=dog_colors, random_state=3),
        interpolation="bilinear",
    )

    plot.axis("off")

    return plot

