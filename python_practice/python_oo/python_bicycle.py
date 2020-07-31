"""
写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，参数传入,
同时有两个方法：
1. fill_charge(vol) 用来充电, vol 为电量
2. run(km) 方法用于骑行,每骑行10km消耗电量1度,
当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""
class Bicycle:
    def run(self, km):
        # 字面量插值传递km参数
        print(f"用脚一共骑行了{km}km，好累好累呀")

# 再写一个电动自行车类EBicycle继承自Bicycle
class Ebicycle(Bicycle):
    # 类属性， 类体内，方法之外
    # volume = 1000
    # 构造方法
    def __init__(self, valume):
        # 实例属性， 类体内，方法内，并且以"self.变量名"的方式，去定义的变量
        self.valume = valume
        # 普通属性， 类体内，方法内，局部变量（我只在当前的方法内有用）
        # valume = valume
        #1. fill_charge(vol) 用来充电, vol 为电量

    def fill_charge(self, vol):
        print(f"电动车已充电{vol}度")
        print(f"充完电之后还有{vol+self.valume}度")


    def run(self, km):
        # run(km)方法用于骑行, 每骑行10km消耗电量1度,

        # 有电的时候能骑到的公里数
        e_km = self.valume*10
        print("电动车的最大公里数",e_km)
        # 当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
        # 当用电的能骑公里数大于我们要骑
        if  km  <= e_km:
            print(f"用电一共骑了{km}km")
        else:
        # 用脚骑的公里数 = 总公里数 - 用电的公里数
            print(f"用电一共骑了{e_km}km")
        # 调用父类的方法，知识点
        # 第一种调用父类的方法，和普通实例化类，调用方法相同
            bike = Bicycle()
            bike.run(km - e_km)
        # 第二种调用父类的方法
            super().run(km - e_km)



    #,添加电池电量valume属性通过

# 继承之后子类可以调用父类的属性和方法
# 构造函数的参数，需要在实例化类的时候传递
ebike = Ebicycle(100)

# 当子类中有和父类重名的方法或者属性，那么首先选择的是子类的
ebike.run()


# # 类在实例化的时候需要加括号
# bike = Bicycle()
# bike.run(100)

