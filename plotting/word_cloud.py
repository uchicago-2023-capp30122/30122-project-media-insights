"""
    Authored by Jessup Jong
"""

import matplotlib.pyplot as plt
import json
import pandas as pd
import numpy as np
from PIL import Image
import wordcloud
import pdb
from process_comments import regex_fix

stopwords = set(wordcloud.STOPWORDS)

with open("../data/cleaned_comment_data.json", "r") as f:
    text = json.load(f)

total_text = " ".join(
    [
        comment[0]
        for key in text
        for comment in text[key]
        if "Paul" not in comment[0] and "Tony" not in comment[0]
    ]
)

total_text = regex_fix(total_text)

for i in range(3):
    dog_mask = np.array(Image.open(f"../data/dog{i}.png"))

    DPI = 1000

    word_cloud_inst = wordcloud.WordCloud(
        background_color="white",
        stopwords=stopwords,
        mask=dog_mask,
        width=2000,
        height=2000,
    )
    dog_colors = wordcloud.ImageColorGenerator(dog_mask)
    dog_word_cloud = word_cloud_inst.generate(total_text)

    plt.figure(figsize=(10, 10), dpi=DPI)
    plt.imshow(
        dog_word_cloud.recolor(color_func=dog_colors, random_state=3),
        interpolation="bilinear",
    )
    plt.axis("off")
    plt.savefig(f"../data/word_cloud{i}.png", bbox_inches="tight", dpi=DPI)
