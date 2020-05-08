#1
'''
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')
'''
#2
'''
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')
'''
#3
'''
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
s1 = 'hello ' * 3
print(s1) # hello hello hello 
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
'''
#4斐波那契数列
'''
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
'''
#5 跑马灯文字
'''
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
'''
#设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
'''
import random
def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for i in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code
'''
#练习3：设计一个函数返回给定文件名的后缀名。
'''
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
'''
#练习4：设计一个函数返回传入的列表中最大和第二大的元素的值
'''
def maxandseconf(x):
    m1,m2=(x[0],x[1]) if (x[0]>x[1])else(x[1],x[0])
    for i in range(2,len(x)):
        if x[i]>m1:
            m2=m1
            m1=x[i]
        elif x[i]>m2:
            m2=x[i]
    return m1,m2
'''
#练习5：计算指定的年月日是这一年的第几天
'''
def if_runnian(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def days(year,month,day):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][if_runnian(year)]
    total = 0
    for i in range(month-1):
        total +=days_of_month[i]
    return total+day
'''
#6打印杨辉三角
'''
def main():
    num = int(input('Number of rows: '))
    yh = [[]]*num
    for row in range(len(yh)):
        yh[row] = [1]*(row+1)
        for col in range(len(yh[row])):
            if col==0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col-1] + yh[row-1][col]
            print(yh[row][col],end='\t')
        print()

if __name__ == '__main__':
    main()
'''
  
        











