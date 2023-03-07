"""
    Authored by Jessup Jong

    This file cleans the comment raw data and stores information in 
    a new json file that stores text and date data. 
"""

import comments
import json
import pdb

with open("../data/comment_data.json", "r") as f:
    video_responses = json.load(f)

cleaned_comments = {}
for video_response in video_responses:
    cleaned_video = []
    for i, comment in enumerate(video_response["items"]):
        try:
            text = comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            date = comment["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
            cleaned_video += [(text, date)]
        except:
            print(f"Structure Different for Comment {i}")
    cleaned_comments[video_response["items"][0]["snippet"]["videoId"]] = cleaned_video

with open("../data/cleaned_comment_data.json", "w") as f:
    json.dump(cleaned_comments, f)
