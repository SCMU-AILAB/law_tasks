# 1.定义一个类
class Washer():
    def wash(self):
        print('能洗衣服')

# 2.创建对象
# 对象名 = 类名()
haier = Washer()

# 3.验证结果
# 打印haier对象
print(haier)

# 使用wash功能 -- 实例方法/对象方法 -- 对象名.Wash()
haier.wash()