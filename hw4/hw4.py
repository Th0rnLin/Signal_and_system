import math
import matplotlib.pyplot as plt

signal, res=[], 0

for j in range(360):
    signal.append(math.cos(math.radians(j)))
for i in signal:
    res+=abs(i)
print(res)
idx=range(len(signal))
plt.plot(idx, signal)