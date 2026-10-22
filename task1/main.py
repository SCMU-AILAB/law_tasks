"""
题目：一元二次函数的数学分析
给定二次函数：

f(x)=ax^2+bx+c, a != 0

程序需要实现以下数学功能：
1. 计算判别式
2. 根据判别式求出方程的实数根
3. 计算抛物线顶点坐标与对称轴
4. 计算指定自变量对应的函数值
5. 求函数在指定闭区间上的最大值和最小值
"""

from math import sqrt


def main() -> None:
    a = int(input("输入 a: "))
    b = int(input("输入 b: "))
    c = int(input("输入 c: "))

    delta: float = b * b - 4 * a * c
    print(f"判别式 Delta = {delta}")

    if delta > 0:
        x1: float = (-b + sqrt(delta)) / (2 * a)
        x2: float = (-b - sqrt(delta)) / (2 * a)

        print("方程有两个实数根 x1 x2: ")
        print(f"    x1 = {x1:.2f}")
        print(f"    x2 = {x2:.2f}")
    elif delta == 0:
        x: float = -b / (2 * a)
        print("方程有一个实数根 x: ")
        print(f"    x = {x:.2f}")
    else:
        print("Delta < 0 方程无实数根")

    vertex_x: float = -b / (2 * a)
    vertex_y: float = a * vertex_x**2 + b * vertex_x + c

    print(f"顶点坐标：({vertex_x:.2f}, {vertex_y:.2f})")
    print(f"对称轴：x = {vertex_x:.2f}")

    if a > 0:
        print("抛物线开口向上")
    else:
        print("抛物线开口向下")

    # 可以在这里加入输入 x 值
    for x in [-2, -1, 0, 1, 2]:
        y = a * x**2 + b * x + c
        print(f"f({x}) = {y:.4f}")

    left = float(input("请输入区间左端点："))
    right = float(input("请输入区间右端点："))

    if left > right:
        left, right = right, left

    y_left = a * left**2 + b * left + c
    y_right = a * right**2 + b * right + c

    values = [y_left, y_right]

    if left <= vertex_x <= right:
        values.append(vertex_y)

    max_value = max(values)
    min_value = min(values)

    print(f"区间：[{left}, {right}]")
    print(f"最大值：{max_value:.2f}")
    print(f"最小值：{min_value:.2f}")


if __name__ == "__main__":
    main()