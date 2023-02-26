import matplotlib.pyplot as plt
import json
import pandas as pd
import pdb

raw_comments = pd.read_json("../data/preprocessed_comments.json")

# with open("../data/preprocessed_comments.json", "r") as f:
#     # pdb.set_trace()
#     text = json.load(f)


# new_text = pd.json_normalize(text)

cleaned_comments = preprocess_comments(raw_comments.iloc[:, 0], fast =False)

print(cleaned_comments)
