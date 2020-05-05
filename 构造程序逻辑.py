#寻找水仙花数
'''
for num in range(100,10000):
    first = num%10
    second = num//10%10
    third = num//10//10%10
    if first**3+second**3+third**3==num:
        print('%d'%num)
'''
#将一个正整数反转
'''
num = int(input('请输入一个正整数:'))
re = 0
while num>0:
    re = re*10 +num%10
    num//=10
print(re)
'''
#百钱百鸡问题
'''
for i in range(1,100):
    for j in range(1,100):
        for z in range(1,100):
            if 5*i+3*j+(1*z)/3==100 and i+j+z==100:
                print('公鸡%d只,母鸡%d只，小鸡%d只'%(i,j,z))
                break
'''
#CRAPS赌博游戏
'''
from random import randint
money = 1000
while money>1000:
    print('你的总资产为:',money)
    needs_go_on = False
    while True:
        try:
            debt = int(input('请输入赌注:'))
            assert 0<=debt<=monry
            break
        except:
            print('请重新下注')
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first==7 or first ==11:
        print('玩家胜利')
        money+=debt
    elif first ==2 or first==3 or first ==12:
        print('庄家胜利')
        money-=debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current= randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current==7:
            print('庄家胜利')
            money-=debt
        elif current == first:
            print('玩家胜利')
            money+=debt
        else:
            needs_go_on = True
print('你破产了，游戏结束')
'''
#生成斐波那契数列
'''
def rabbit(n):
    i=1
    j=1
    data = [1,1]
    for z in range(1,n):
        z = i+j
        i,j=j,z
        data.append(z)
    print(data)
'''
#找出10000以内的完美数
'''
for i in range(1,10000):
    add = 0
    for j in range(2,i+1):
        if i%j==0:
            add += i//j
    if add == i:
        print(i)
'''
#输出100以内所有的素数
'''
from math import sqrt
for num in range(1,101):
    end = int(sqrt(num))
    is_l = True
    for i in range(2,end+1):
        if num%i==0:
            is_l = False
            break
    if is_l and num!=1:
        print(num)
'''
    
    

    
            
            










    

