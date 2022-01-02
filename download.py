import os

val = input("relative location?")

f = 1
for file in os.listdir(os.path.dirname(os.path.realpath(val))):
    if ".hevc" in file:
        ffmpeg = os.system("ffmpeg -i {} output{}.mp4".format(os.path.abspath(file), f))
        print("output{}.mp4 loaded".format(f))
        f = f + 1

        