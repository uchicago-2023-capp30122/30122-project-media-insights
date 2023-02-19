import requests
import os
import re
import json
import googleapiclient.discovery
import pdb

def get_comments(url_lst):
    return_lst = []

    for url in url_lst:
        video = re.search(r'(?<=v=)[\w-]+', url)
        if video:
            video = video.group(0)
            print(video)
            return_lst += [get_request(videoId=video)]
    
    with open("comment_data.json", "w") as f:
        json.dump(return_lst, f)


def get_request(videoId):
    api_key = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"

    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={videoId}&key={api_key}"
    response = requests.get(url).json()
    return response

def get_comments_api(videoId="YzZUIYRCE38"):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="replies",
        videoId = videoId
    )
    response = request.execute()

    return response

url_lst = ["https://www.youtube.com/watch?v=IrGZ66uKcl0",
           "https://www.youtube.com/watch?v=RrH40nCcjwE",
           "https://www.youtube.com/watch?v=V4-ycdxqimA",
           "https://www.youtube.com/watch?v=R6-6wV0agvs"]
get_comments(url_lst)


# Possibly think about storing data in database
    # db file, or json file.

# References
# https://github.com/youtube/api-samples
# https://developers.google.com/youtube/v3/docs/commentThreads/list
