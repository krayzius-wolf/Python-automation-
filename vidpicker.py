import os, random, subprocess
def rndmp():

   folder=r"E:\desktop_dell\secure\videos"
   randomfile = random.choice(os.listdir(folder))
   file = folder +'\\'+ randomfile
   subprocess.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', file])

rndmp()
