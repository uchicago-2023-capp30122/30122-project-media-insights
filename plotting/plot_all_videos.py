import process_comments

with open("../data/cleaned_comment_data.json",'r') as f:
    data = json.loads(f.read())

temp_clean_text = raw_comments.apply(preprocess_comments)