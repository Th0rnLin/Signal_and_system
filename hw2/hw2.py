import math
import random

F_cos=open('cos.txt', 'w')
F_cos_noise=open('cos_noise.txt', 'w')

for i in range(5):
    for j in range(360):
        radian=math.radians(j)
        F_cos.write('{:.6f}, {:.6f}\n'.format((1/360)*j+1*i, math.cos(radian)))
        F_cos_noise.write('{:.6f}, {:.6f}\n'.format((1/360)*j+1*i, math.cos(radian)+random.uniform(-0.5, 0.5)))
F_cos.close()
F_cos_noise.close()