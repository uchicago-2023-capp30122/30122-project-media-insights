import subprocess
import time

"""
    Authored by Jessup Jong
    
    This provides multiple uploads of videos. 
    
    The current number is at 2 because after 2 videos, the YouTube quota is met. With a paid service , you will be able to upload many more. 
    
    This functionality is commented out to have 1 video as the default. 
"""

#test_lst = [('videos/test1.mov',
#  f'Test Upload #{i}',
#  'Surfing in Santa Cruz',
#  'surfing, Santa Cruz',
#  '22',
#  'public',
#  'localhost',
#  '8080', '8090',
#  'ERROR') for i in range(2)]
#
#test_args = []
#
#for test in test_lst:
#    my_file, title, des, key, category, privacy, host1, host2, port, log = test
#
#    test_args += [['--file', my_file, '--title', title,
#                              '--description', des, '--keywords', key,
#                              '--category', category, '--privacyStatus', privacy]]
#
#for argument in test_args:
#    subprocess.Popen(["python", "upload_video.py"] + argument)
#    subprocess.check_output(['bash','-c', 'echo "one video done."'])
#    time.sleep(20)
