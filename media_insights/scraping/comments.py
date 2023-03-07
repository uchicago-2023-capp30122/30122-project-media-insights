"""
    Authored by Jessup Jong
"""

import requests
import os
import re
import json
import googleapiclient.discovery
import pdb

def get_request(url_lst, specific_request):
    raw_data = []
    video_id = []

    for url in url_lst:
        video = re.search(r'(?<=v=)[\w-]+', url)
        if video:
            video = video.group(0)
            raw_data += [specific_request(video)]
            video_id += [video]

    return (raw_data, video_id)


def get_comments_request(videoId):
    api_key = os.environ['API_KEY']

    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={videoId}&key={api_key}"
    response = requests.get(url).json()
    return response

def get_comments_request_api(videoId="YzZUIYRCE38"):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ['API_KEY']
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="replies",
        videoId = videoId
    )
    response = request.execute()

    return response

if __name__ == "__main__":
    url_lst = ["https://www.youtube.com/watch?v=w55xmZLWfBg",
            "https://www.youtube.com/watch?v=NsscBcwjTNg",
            "https://www.youtube.com/watch?v=DEtyL4lXp7s",
            "https://www.youtube.com/watch?v=ECHlvUyaXFU",
            "https://www.youtube.com/watch?v=4znhKBm5oOA"]

    comment_data = get_request(url_lst, get_comments_request)[0]

    with open("../data/comment_data.json", "w") as f:
        json.dump(comment_data, f)



# Possibly think about storing data in database
    # db file, or json file.

# References
# https://github.com/youtube/api-samples
# https://developers.google.com/youtube/v3/docs/commentThreads/list
