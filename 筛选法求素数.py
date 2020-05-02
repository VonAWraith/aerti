
while True:
    try:
        n = int(input('请输入一个大于二的正整数'))
        assert n>2
        break
    except:
        print('taoqi,bixu大于2')

aList = []
aList[::] = range(n)
bList = [i+1 for i in aList]
a = bList[1:n]
m = int(n**0.5)
for i,d in enumerate(a):
    if d > m:
        break
    a[i+1:] = filter(lambda x : x%d!=0,a[i+1:])
print(a)
'''
maxnumber=int(input('输入一个比2大的数字'))
a = list(range(2,maxnumber))
m = int(maxnumber**0.5)
for i,d in enumerate(a):
    if d > m:
        break
    a[i+1:] = filter(lambda x : x%d!=0,a[i+1:])
print(a)'''
   

