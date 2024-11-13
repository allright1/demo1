# import random
# for i in range(0,5):
#     x = random.randrange(0,2)
#     y = random.randrange(2,4)
#     z = x * y
#     print(z)

# # 随机生成验证码
# str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
#     #随机选取4个值作为验证码
# rand_str = ''
# for j in range(0, 4):
#     rand_str += str1[random.randrange(0, len(str1))]
# print(rand_str)


# def add_num1(a,b):
#     """加减法说明文档"""
#     res = a+b
#     print(res)
# a = int(input("a="))
# b = int(input("b="))
# add_num1(a,b)

# help(add_num1)
# for i in range(5):
#     pass
# print(i)

# # 函数
# def fn1():
#     return 200
# print(fn1)
# print(fn1())
#  # lambda表达式
# fn2 = lambda: 100
# print(fn2)
# print(fn2())

# # 烤地瓜
# class SweetPotato():
#     def __init__(self):
#         # 被烤的时间
#         self.cook_time = 0
#         # 地⽠瓜的状态
#         self.cook_static = '⽣生的'
#         # 调料料列列表
#         self.condiments = []

#     def cook(self, time):
#         """烤地⽠瓜的⽅方法"""
#         self.cook_time += time
#         if 0 <= self.cook_time < 3:
#             self.cook_static = '生的'
#         elif 3 <= self.cook_time < 5:
#             self.cook_static = '半生不熟'
#         elif 5 <= self.cook_time < 8:
#             self.cook_static = '熟了了'
#         elif self.cook_time >= 8:
#             self.cook_static = '烤糊了了'

#     def add_condiments(self, condiment):
#         """添加调料料"""
#         self.condiments.append(condiment)

#     def __str__(self):
#         return f'这个地⽠瓜烤了了{self.cook_time}分钟, 状态是{self.cook_static}，加了调料：{self.condiments}'

# digua1 = SweetPotato()
# # print(digua1)
# digua1.cook(5)
# digua1.add_condiments("孜然")
# print(digua1)   

# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果⼦子配⽅方]'
#     def make_cake(self):
#         print(f'运⽤用{self.kongfu}制作煎饼果⼦子')
#  # 创建学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '[⿊黑⻢马煎饼果⼦子配⽅方]'
#     def make_cake(self):
#         print(f'运⽤用{self.kongfu}制作煎饼果⼦子')
# class Prentice(School, Master):
#     def __init__(self):
#       self.kongfu = '[独创煎饼果⼦子配⽅方]'
#     def make_cake(self):
#       # 如果是先调用了父类的属性和⽅方法，父类属性会覆盖⼦子类属性，故在调用属性前，先调⽤⾃己子类的初始化
#         # self.__init__()
#         print(f'运⽤用{self.kongfu}制作煎饼果⼦子')
#  # 调⽤父类⽅方法，但是为保证调⽤用到的也是⽗父类的属性，必须在调⽤方法前调⽤父类的初始化
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def make_school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)

# daqiu = Prentice()
# print(daqiu.kongfu)
# daqiu.make_master_cake()
# a = 0
# b = 0
# for i in range(1,366):
#     if i%6 == 0:
#         b += 1
#     elif i%7 == 0:
#         b += 1
#     else:
#         a += 1
#         # print(i)
#         print(a)

# a = 720
# b = 0
# for i in range(1,13):
#     b = a + b
#     print(f"Month {i}:")
#     print(b)

# c = b * 0.015
# print(c)

# import pandas as pd  
# import matplotlib.pyplot as plt  
  
# # 读取Excel文件  
# file_path = r'C:\Users\info\Desktop\客户与销售情况报表.xlsx' 
# sheet_name = '销售订单数据'  
# data = pd.read_excel(file_path, sheet_name=sheet_name)  
  
# # 确保下单日期是日期类型  
# data['下单日期'] = pd.to_datetime(data['下单日期'])  
  
# # 计算周数（假设周一为每周的第一天）  
# data['年月'] = data['下单日期'].dt.strftime('%Y-%m') 
# # 计算每周的销售额（小计人民币）  
# weekly_sales = data.groupby('年月')['小计人民币'].sum().reset_index()  
  
# # 绘制销售额周趋势图  
# plt.figure(figsize=(10, 6))  
# plt.plot(weekly_sales['年月'], weekly_sales['小计人民币'], marker='o', linestyle='-', color='b')  
# plt.title('销售额周趋势图')  
# plt.xlabel('年月')  
# plt.ylabel('销售额（人民币）')  
# plt.grid(True)  
# plt.xticks(weekly_sales['年月'], rotation=45)  # 旋转x轴标签，以便更清晰地显示  
# plt.tight_layout()  
# plt.show()

def make_div(func):
    """对被装饰的函数的返回值 div标签"""
    def inner(*args, **kwargs):
        return "<div>" + func() + "</div>"
    return inner


def make_p(func):
    """对被装饰的函数的返回值 p标签"""
    def inner(*args, **kwargs):
        return "<p>" + func() + "</p>"
    return inner


# 装饰过程: 1 content = make_p(content) 2 content = make_div(content)
# content = make_div(make_p(content))
@make_div
@make_p
def content():
    return "人生苦短"

result = content()

print(result)


