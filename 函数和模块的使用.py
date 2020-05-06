#组合
'''
m = int(input('m='))
n = int(input('n='))
M =1
for i in range(1,m+1):
    M = M*i
N = 1
for i in range(1,n+1):
    N = N*i
z = 1
for i in range(1,m-n+1):
    z = z*i
column = M//(z*N)
print(column)
'''
#组合引申
'''
def zuhe(num):
    f = 1
    for i in range(1,num+1):
        f *= i
    return f

m = int(input('m='))
n = int(input('n='))
print(zuhe(m) // zuhe(n) // zuhe(m - n))
'''
#
'''
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
'''
#
'''
def foo():
    print(3)


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
'''
#练习1：实现计算求最大公约数和最小公倍数的函数
'''
def gys(x,y):
    if x>y:
        x,y = y,x
    for fac in range(x,0,-1):
        if x%fac==0 and y%fac==0:
            return fac
            
def gbs(x,y):
    return x*y//gys(x,y)
'''
'''#练习3：实现判断一个数是不是回文数的函数。
def hws(x):
    num = x
    re_num =0
    while num>0:
        re_num = re_num*10 + num%10
        num //=10
    return re_num==x

#练习3：实现判断一个数是不是素数的函数
def sushu(num):
    end = int(num**0.5)
    is_l = True
    for i in range(2,end+1):
        if num%i==0:
            is_l = False
            break
    return is_l and num!=1
#练习4：写一个程序判断输入的正整数是不是回文素数
if __name__ == '__main__':
    n = int(input('请输入一个数:'))
    if hws(n) and sushu(n):
        print('是回文素数')
    else:
        print('不是回文素数')'''
#作用域
def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        nonlocal b
        b=3
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    print(b)
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
