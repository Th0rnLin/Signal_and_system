import math
import random

def create_white_noise():
    F_cos=open('cos.txt', 'w')
    F_cos_noise=open('cos_noise.txt', 'w')

    for i in range(5):
        for j in range(0, 360, 36):
            radian=math.radians(j)
            F_cos.write('{:.6f}, {:.6f}\n'.format((1/360)*j+1*i, math.cos(radian)))
            F_cos_noise.write('{:.6f}, {:.6f}\n'.format((1/360)*j+1*i, math.cos(radian)+random.uniform(-0.5, 0.5)))
    F_cos.close()
    F_cos_noise.close()

def read_noise():
    noise=[]
    F_cos=open('cos_noise.txt', 'r')
    for i in F_cos.readlines():
        a, b=i.split(' ')
        noise.append(float(b.replace('\n', '')))
    F_cos.close()
    return noise

def rectangular():
    noise=read_noise()
    F_rectangular=open('cos_rectangular.txt', 'w')
    for i in range(len(noise)):
        tmp=noise[i]
        if i-1>0: tmp+=noise[i-1]
        if i+1<len(noise): tmp+=noise[i+1]
        F_rectangular.write('{:.6f}\n'.format(tmp/3))
    F_rectangular.close()

def triangular():
    noise=read_noise()
    F_triangular=open('cos_triangular.txt', 'w')
    for i in range(len(noise)):
        tmp=noise[i]*3
        if i-2>0: tmp+=noise[i-2]
        if i-1>0: tmp+=noise[i-1]*2
        if i+1<len(noise): tmp+=noise[i+1]*2
        if i+2<len(noise): tmp+=noise[i+2]
        F_triangular.write('{:.6f}\n'.format(tmp/9))
    F_triangular.close()

def golay():
    noise=read_noise()
    F_golay=open('cos_golay.txt', 'w')
    for i in range(len(noise)):
        tmp=noise[i]*17
        if i-2>0: tmp+=noise[i-2]*-3
        if i-1>0: tmp+=noise[i-1]*12
        if i+1<len(noise): tmp+=noise[i+1]*12
        if i+2<len(noise): tmp+=noise[i+2]*-3
        F_golay.write('{:.6f}\n'.format(tmp/35))
    F_golay.close()

def main():
    create_white_noise()
    rectangular()
    triangular()
    golay()

if __name__=='__main__':
    main()