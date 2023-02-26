import matplotlib.pyplot as plt
import json
import pandas as pd
import pdb

# raw_comments = pd.read_json("../data/cleaned_comment_data.json")

with open("../data/cleaned_comment_data.json", "r") as f:
    # pdb.set_trace()
    text = json.load(f)

total_text = []
for key in text:
    for comment in text[key]:
        total_text += [comment[0]]

print(total_text)


