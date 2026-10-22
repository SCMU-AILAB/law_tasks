from math import sqrt


def read_coefficients() -> tuple[int,int,int]:
    a = int(input("输入 a: "))
    b = int(input("输入 b: "))
    c = int(input("输入 c: "))
    return a,b,c


def calc_discriminant(a: int, b: int, c: int) -> float:
    delta: float = b * b - 4 * a * c
    print(f"判别式 Delta = {delta}")
    return delta


def show_roots(a: int, b: int, c: int, delta: float) -> None:
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)

        print("方程有两个实数根 x1 x2: ")
        print(f"   x1 = {x1:.2f}")
        print(f"   x2 = {x2:.2f}")
    elif delta == 0:
        x: float = -b / (2 * a)
        print("方程有一个实数根 x: ")
        print(f"   x = {x:.2f}")
    else:
        print("Delta < 0 方程无实数根")


def show_vertex(a: int, b: int, c: int) -> tuple[float,float]:
    vertex_x: float = -b / (2 * a)
    vertex_y: float = a * vertex_x**2 + b * vertex_x + c

    print(f"顶点坐标：({vertex_x:.2f}, {vertex_y:.2f})")
    print(f"对称轴：x = {vertex_x:.2f}")

    if a > 0:
        print("抛物线开口向上")
    else:
        print("抛物线开口向下")

    return vertex_x, vertex_y


def show_function_values(a: int, b: int, c: int) -> None:
    x = float(input("请输入 x 的值："))
    y = a * x ** 2 + b * x + c
    print(f"f({x:g}) = {y:.4f}")

def show_interval_extremes(a: int, b: int, c: int,
                           vertex_x: float, vertex_y: float) -> None:
    left = float(input("请输入区间左端点："))
    right = float(input("请输入区间右端点："))

    if left > right:
        left, right = right, left

    y_left = a * left ** 2 + b * left + c
    y_right = a * right ** 2 + b * right + c

    values = [y_left, y_right]

    if left <= vertex_x <= right:
        values.append(vertex_y)

    max_value = max(values)
    min_value = min(values)

    print(f"区间：[{left}, {right}]")
    print(f"最大值：{max_value:.2f}")
    print(f"最小值：{min_value:.2f}")


def print_menu() -> None:
    print()
    print("=" * 34)
    print("  1. 计算判别式")
    print("  2. 求方程的实数根")
    print("  3. 求顶点坐标与对称轴")
    print("  4. 计算指定自变量的函数值")
    print("  5. 求闭区间上的最大值与最小值")
    print("  6. 重新输入系数 a b c")
    print("  0. 退出")
    print("=" * 34)


def main() -> None:
    print("一元二次函数 f(x) = ax^2 + bx + c 分析程序")
    a, b, c = read_coefficients()

    while True:
        print(f"\n当前函数：f(x) = {a}x^2 + {b}x + {c}")
        print_menu()
        choice = input("请选择功能编号：").strip()

        if choice == "1":
            calc_discriminant(a, b, c)

        elif choice == "2":
            delta = b * b - 4 * a * c
            show_roots(a, b, c, delta)

        elif choice == "3":
            show_vertex(a, b, c)

        elif choice == "4":
            show_function_values(a, b, c)

        elif choice == "5":
            vertex_x = -b / (2 * a)
            vertex_y = a * vertex_x**2 + b * vertex_x + c
            show_interval_extremes(a, b, c, vertex_x, vertex_y)

        elif choice == "6":
            a, b, c = read_coefficients()

        elif choice == "0":
            print("程序结束。")
            break

        else:
            print("无效的选项，请输入 0~6 之间的数字。")


if __name__ == "__main__":
    main()