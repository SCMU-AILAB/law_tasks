class Washer():
    def __init__(self):
        # 添加示例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier = Washer()
haier.print_info()