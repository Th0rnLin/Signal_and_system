import math

file_name   = input('file_name: ')
input_TF    = input('please input your choise (T or F): ')
value       = int(input('please input your value for T or F: '))
sample_rate = int(input('please input your sample rate: '))

value=value if input_TF=='T' else 1/value
delta_angle = int(360/(sample_rate*value))
F=open('{}.txt'.format(file_name), 'w')

for i in range(2):
    for j in range(0, 360, delta_angle):
        radian=math.radians(j)
        # print('{}, {}\n'.format((value/360)*j+value*i, math.cos(radian)))
        F.write('{}, {}\n'.format((value/360)*j+value*i, math.cos(radian)))
F.close()