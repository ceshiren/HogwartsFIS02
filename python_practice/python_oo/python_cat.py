## 定义类，首字母需要大写
class Cat:
    # 毛色，橘色， 四条腿
    # 会吃， 会叫， 会睡
    ## 属性
    color = "orange"
    leg = 4
    ## 方法，在类的方法中，是使用def 关键字定义
    ## def 定义的 在类外叫做函数function, 在类内，叫做method
    def eat(self):
        print("猫在吃")
    def cry(self):
        print("猫在叫")

print(Cat.color)
# 类的实例化
cat = Cat()
