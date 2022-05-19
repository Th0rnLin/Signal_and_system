import math
import matplotlib.pyplot as plt

signal, res=[], []

for i in range(5):
    for j in range(360):
        signal.append(math.cos(math.radians(j)))
for i in range(len(signal)):
    if(i+1<len(signal) and signal[i]>signal[i+1] and i-1>0 and signal[i]>signal[i-1] and signal[i]>0):
        res.append(i)

print(res)

idx=range(len(signal))
plt.plot(idx, signal)