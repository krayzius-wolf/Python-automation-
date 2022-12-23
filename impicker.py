import os, random,time

folder=r"E:\desktop_dell\secure\pictures"
a=[]
[a.append(random.choice(os.listdir(folder))) for i in range(5)]

from PIL import Image
for i in a:
    file = folder+'\\'+i
    Image.open(file).show()
    time.sleep(3)

