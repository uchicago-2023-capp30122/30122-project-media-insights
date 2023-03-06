import requests
import comments
import json
import pdb

def get_transcripts_request(videoId):
    url = f"http://video.google.com/timedtext?lang=en&v={videoId}"
    return requests.get(url).text

if __name__ == "__main__":
    url_lst = ["https://www.youtube.com/watch?v=w55xmZLWfBg",
            "https://www.youtube.com/watch?v=NsscBcwjTNg",
            "https://www.youtube.com/watch?v=DEtyL4lXp7s",
            "https://www.youtube.com/watch?v=ECHlvUyaXFU",
            "https://www.youtube.com/watch?v=4znhKBm5oOA"]

    transcript_data = comments.get_request(url_lst, get_transcripts_request)

    with open("../data/transcript_data.json", "w") as f:
        json.dump(transcript_data, f)