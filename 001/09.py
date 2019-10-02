"""
输入年份判断是否是闰年
"""
a = int(input('请输入年份:'))
is_leep = (a/4==0 and a/100!=0 or a/400==0)
print(is_leep)