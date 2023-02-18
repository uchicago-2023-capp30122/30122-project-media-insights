import comments
import json

response = json.dumps(comments.get_comments_simple())
print(response.get('textDisplay'))

# regex with string

# prof Turk choice
# extracting them specifically
for comment in response['items']:
        comment = comment.get('replies', None)
        if comment:
            print(comment['comments'][0]['snippet']['textOriginal'], "\n")

# recursive for loop that is more general (not based on structure)

# Also, extract date from the comments as well.

