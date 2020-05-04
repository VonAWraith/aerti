#1
'''
import random
x = random.choice(range(1,101))
while True:
    counts +=1
    n = int(input('请输入一个数字:'))
    if n>x:
        print('大')
    elif n<x:
        print('小')
    else:
        print('对了')
        break
print('你一共猜测了%d次'%n)
if counts > 7:
    print('你的智商余额明显不足')
'''
#2
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end='\t')
    print()
'''
#练习1：输入一个正整数判断是不是素数
'''
from math import sqrt
num = int(input('请输入一个正整数:'))
end = int(sqrt(num))
is_l = True
for i in range(2,end+1):
    if num%i==0:
        is_l = False
        break
if is_l and num !=0:
    print('是素数')
else :
    print('不是素数')
'''
#练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
'''
x = int(input('x = '))
y = int(input('y = '))

if x>y:
    x,y = y,x
for f in range(x,0,-1):
    if x%f==0 and y%f==0:
        print('%d和%d的最大公约数为%d'%(x,y,f))
        print('%d和%d的最大公倍数为%d'%(x,y,x*y//f))
        break
'''
#练习3：打印如下所示的三角形图案。
row = int(input('输入行数:'))
for i in range(row):
    for j in range(i+1):
        print('*',end = ' ')
    print()

for i in range(row):
    for j in range(row):
        if j<row-i-1:
         print(' ',end=' ')
        else:
         print('*',end=' ')
    print()

for i in range(row):
    for j in range(row -i-1):
        print(' ',end = ' ')
    for j in range(2*i+1):
        print('*',end=' ')
    print()

    






