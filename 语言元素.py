#练习1：华氏温度转换为摄氏温度。
'''
f = float(input('请输入华氏温度：'))
c = (f-32)/1.8
print('%.lf华氏度=%.lf摄氏度'%(f,c))
'''
#练习2：输入圆的半径计算计算周长和面积
'''
r = float(input('请输入半径：')
c = 2*3.1416*r
s = 4*3.1416*r*r
print('圆周长为%.2f,面积为%.2f'%(c,s))
'''
#练习3：输入年份判断是不是闰年

year = int(input('请输入年份:'))
is_leap = ((year%4==0)and(year%100!=0)) or(year%400==0)
print(is_leap)

    

