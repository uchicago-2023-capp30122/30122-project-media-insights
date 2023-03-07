"""
    Authored by Jessup Jong

    This scrapes comments from multiple Youtube videos. Transcripts.py also
    relies on the scraping technique from this file to achieve transcripts
    scraping in one line. 
"""

import requests
import os
import re
import json
import googleapiclient.discovery
import pdb

def get_request(url_lst, specific_request):
    """
        This helper function does a get request that can be done for
        comments and transcripts.

        url_lst (lst): list of video urls that will be regexed for videoIds.
        specific_request(function): specific function that will be passed.
            This will either be comments or transcripts but can later be 
            expanded for more functionality. 
    """
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
    """
        This is the get_comments function that handles getting comments.
        This an optimized from the requirements from Google. 
        Normally, a python request requires a lot of overhead with the 
        googleapiclient.discovery functionality. For a faster usage without
        bugs and reliability, this function does the same job with a simple 
        get request. 
        Inputs:
            videoId(str): video id to scrape comments.

        Returns:
            response: get response from scraping data from Youtube.
    """
    api_key = os.environ['API_KEY']

    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={videoId}&key={api_key}"
    response = requests.get(url).json()
    return response

def get_comments_request_api(videoId="YzZUIYRCE38"):
    """
        A reduced version of the official requirement for YouTube API.
        While this version also works, we provide a faster version above 
        with less overhead of YouTube's methods. 

        Input: videoId(str): video Id to scrape
    """
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

# References
# https://github.com/youtube/api-samples
# https://developers.google.com/youtube/v3/docs/commentThreads/list
