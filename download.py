import os
f = 0

for files in os.listdir(os.path.dirname(__file__)):
    if "." not in files:
        for file in os.listdir(os.path.join(os.path.dirname(__file__), files)):
            if ".hevc" in file:
                f+=1
                ffmpeg = os.system("ffmpeg -i {} {}\output{}.mp4".format(os.path.join(os.path.join(os.path.dirname(__file__), files), file), os.path.join(os.path.dirname(__file__), files), f))
