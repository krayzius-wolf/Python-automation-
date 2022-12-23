import speedtest
import time
import matplotlib.pyplot as plt
import numpy as np

speed_test = speedtest.Speedtest()

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

a=[]
for i in range(25):
    time.sleep(20)
    download_speed = bytes_to_mb(speed_test.download())
    #p\rint("Your Download speed is", download_speed, "MBPS")
    a.append(download_speed)
t=[]
time=0
for i in range(25):
    t.append(time)
    time=time+20
a=np.array(a)
t=np.array(t)

plt.plot(t,a)
plt.show()
