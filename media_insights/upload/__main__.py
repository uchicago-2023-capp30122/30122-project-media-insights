import subprocess
import time

test_lst = [('videos/test1.mov',
  f'Test Upload #{i}',
  'Surfing in Santa Cruz',
  'surfing, Santa Cruz',
  '22',
  'public',
  'localhost',
  '8080', '8090',
  'ERROR') for i in range(5)]

test_args = []

for test in test_lst:
    my_file, title, des, key, category, privacy, host1, host2, port, log = test

    test_args += [['--file', my_file, '--title', title,
                              '--description', des, '--keywords', key,
                              '--category', category, '--privacyStatus', privacy]]

for argument in test_args:
    subprocess.Popen(["python", "upload_video.py"] + argument)
    time.sleep(3)
