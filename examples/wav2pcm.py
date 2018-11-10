import os
import numpy as np
f = open("D:\\java\\workspace\\rtasr-demo\\resource\\2018-11-10T07_50_32.665Z.wav","rb");
f.seek(0)
f.read(44)
data = np.fromfile(f,dtype=np.int16)
data.tofile("D:\\test.pcm")