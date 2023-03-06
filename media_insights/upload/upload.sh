#!/bin/bash

python upload_video.py --file="videos/test1.mov"
                       --title="Summer vacation in California"
                       --description="Had fun surfing in Santa Cruz"
                       --keywords="surfing,Santa Cruz"
                       --category="22"
                       --privacyStatus="public"

# python upload_video.py --file="videos/test1.mov" --title="Summer vacation in California" --description="Had fun surfing in Santa Cruz" --keywords="surfing, Santa Cruz" --category="22" --privacyStatus="public"

# ['--file', 'videos/test1.mov', '--title', 'Summer vacation in California', '--description', 'Had fun surfing in Santa Cruz', '--keywords', 'surfing, Santa Cruz', '--category', '22', '--privacyStatus', 'unlisted', '--auth-host-name', 'localhost', '--auth-host-port', '8080', '8090', '--logging-level', 'ERROR']
#https://studio.youtube.com/channel/UCIryH9MxV_Ge76Z13OBxWhg/videos