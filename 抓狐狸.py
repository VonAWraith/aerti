from random import choice,randrange
def catchme(n=5,maxsteps=10):
    positions = [0]*n

    oldpos = randrange(0,n)
    positions[oldpos] = 1

    while maxsteps>=0:
        maxsteps -=1
        while True:
            try:
                x = int(input('请输入你以为狐狸在的洞口数'))
                assert 0<=x<n
                break
            except:
                print('你是不是玩不起?')

        if positions[x]==1:
            print('不错啊')
            break   
        else:
            print('你不行~~~')
        if oldpos == n-1:
            newpos = oldpos-1
        elif oldpos==0:
            newpos = oldpos+1
        else:
            newpos = oldpos + choice((-1,1))
        positions[oldpos],positions[newpos]=0,1
        oldpos = newpos

print('想玩儿游戏嘛，先来答个问题吧')
x = int(input('请输入10+9等于多少'))
if x ==19:
    catchme()
else:
    print('玩个屁')
    
