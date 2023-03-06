import requests
import comments
import json
import pdb
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcripts_request(videoId):
    """
        This is an optional function provided that scrapes manually added transcript data.
        For most cases, the third party API should be sufficient.
    """
    url = f"http://video.google.com/timedtext?lang=en&v={videoId}"
    return requests.get(url).text

if __name__ == "__main__":
    url_lst = ["https://www.youtube.com/watch?v=z-dOfoxSkFU",
            "https://www.youtube.com/watch?v=2mdAgnFOzOU",
            "https://www.youtube.com/watch?v=Xo4txCMetIs",
            "https://www.youtube.com/watch?v=eN0sAYQ3_NM",
            "https://www.youtube.com/watch?v=crH_fqwKJuk"]

    transcript_data = comments.get_request(url_lst, YouTubeTranscriptApi.get_transcript)

    with open("../data/transcript_data.json", "w") as f:
        json.dump(transcript_data, f)