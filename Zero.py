import math
from decimal import Decimal

text = """这是一个零点计算器，将基于你输入的函数、范围、精度（符和二分法使用条件），使用二分法计算出零点。

现在，请输入输入函数，输入规则：
使用 * 乘法，如5倍x要写成 5*x；
对数函数，log(真数,底数)；
幂， ** 表示幂，如x的二分之三次幂为 x**(2/3)；
pi表示圆周率，e表示e。
f(x)="""

def function(expression):
    def f(x):
        return eval(expression, {"x": x, "log": math.log, "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan, "pi": math.pi, "e": math.e, "**": math.pow})
    return f
def oz(f,a,b):
    return f(a) * f(b) < 0

f = function(input(text)) #f即为f(x)
e = float(input("ε="))
a = float(input("a="))
b = float(input("b="))
i = 1
c = 0
if not oz(f, a, b):
    print("在区间 [a, b] 上没有零点，或不满足二分法条件")
else:
    i = 1
    while abs(a - b) >= e:
        c = (a + b) / 2
        if f(c) == 0:
            a = c
            break
        elif oz(f, a, c):
            b = c
        else:
            a = c
        print(f"第{i}次二分，a = {a}，b = {b}")
        i += 1
    c=(a+b)/2
    print("{0:.36f}".format(c))