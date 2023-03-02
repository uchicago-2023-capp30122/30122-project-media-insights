#!/bin/bash

python upload_video.py --file="videos/test1.mov"
                       --title="Summer vacation in California"
                       --description="Had fun surfing in Santa Cruz"
                       --keywords="surfing,Santa Cruz"
                       --category="22"
                       --privacyStatus="unlisted"
                       
# python upload_video.py --file="videos/test1.mov" --title="Summer vacation in California" --description="Had fun surfing in Santa Cruz" --keywords="surfing, Santa Cruz" --category="22" --privacyStatus="unlisted"


(media insights-py3.9) (base) currentuser@users-MacBook-Pro-3 upload % python upload_video.py --file="videos/test1.mov" --title="Summer vacation in California" --description="Had fun surfing in Santa Cruz" --keywords="surfing, Santa Cruz" --category="22" --privacyStatus="private"
Traceback (most recent call last):
  File "/Users/currentuser/Dropbox/Miscellaneous/Python/CSA2/project-spring23/30122-project-media-insights/upload/upload_video.py", line 173, in <module>
    youtube = get_authenticated_service(args)
  File "/Users/currentuser/Dropbox/Miscellaneous/Python/CSA2/project-spring23/30122-project-media-insights/upload/upload_video.py", line 71, in get_authenticated_service
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
  File "/Users/currentuser/Library/Caches/pypoetry/virtualenvs/media_insights-jCOsSxil-py3.9/lib/python3.9/site-packages/oauth2client/_helpers.py", line 133, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "/Users/currentuser/Library/Caches/pypoetry/virtualenvs/media_insights-jCOsSxil-py3.9/lib/python3.9/site-packages/oauth2client/client.py", line 2134, in flow_from_clientsecrets
    client_type, client_info = clientsecrets.loadfile(filename,
  File "/Users/currentuser/Library/Caches/pypoetry/virtualenvs/media_insights-jCOsSxil-py3.9/lib/python3.9/site-packages/oauth2client/clientsecrets.py", line 165, in loadfile
    return _loadfile(filename)
  File "/Users/currentuser/Library/Caches/pypoetry/virtualenvs/media_insights-jCOsSxil-py3.9/lib/python3.9/site-packages/oauth2client/clientsecrets.py", line 122, in _loadfile
    obj = json.load(fp)
  File "/opt/anaconda3/lib/python3.9/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/opt/anaconda3/lib/python3.9/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/opt/anaconda3/lib/python3.9/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/opt/anaconda3/lib/python3.9/json/decoder.py", line 353, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 10 column 5 (char 490)