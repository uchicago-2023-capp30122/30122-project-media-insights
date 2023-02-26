import process_comments as pc
import json
import pandas as pd
from PIL import Image

with open("../data/cleaned_comment_data.json",'r') as f:
    data = json.loads(f.read())

raw_comments = pd.json_normalize(data)

temp_clean_text = raw_comments.apply(pc.preprocess_comments)

clean_text.to_json("../data/preprocessed_comments.json")