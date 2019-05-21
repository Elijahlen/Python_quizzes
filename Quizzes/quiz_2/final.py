import sys
from math import gcd


try:
    split = input('Enter two strictly positive integers: ').split()
    numerator, denominator = split
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

# Replace this comment with your code
S = []
Y = []
j = 0
i = 0
da = gcd(numerator,denominator)
n = numerator//da
m = denominator//da
while m%2 == 0:         #分解质因数
    m = m//2
while m%5 == 0:
    m = m//5
if m == 1:
    has_finite_expansion = True
    jieguo = str(numerator/denominator)        #可以直接把数字转化成字符串
    integral_part = str(numerator//denominator)
    sigma = jieguo[len(integral_part)+1::]     #字符串可以直接切片索引
    if sigma == '0':
        sigma = ''
else:
    m = denominator//da
    yu = n%m
    for i in range(0,m+2):         
        Y.append(yu)                  #往已知列表中添加元素
        yu = yu * 10
        s = yu // m
        S.append(s)
        yu = yu - m*s
        for j in range(0,i+1):
            if yu == Y[j]:
                break
        else:                         #嵌套循环中想要跳出2个循环用 for。。else
            continue                  #此处continue意味着继续下一个循环
        break
if not sigma:
    tau = [str(i) for i in S[j:i+1]]  #把列表中的所有元素转化为字符串说白了就是去逗号和大括号
    tau = ''.join(tau)                #他们拼接成一个连续的字符串，用epmty
    sigma = [str(i) for i in S[:j]]
    sigma = ''.join(sigma)

if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')
