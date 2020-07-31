# 快捷键导入 alt + enter（回车）
# 文件名、 路径名、 变量名、函数名、类名，不要和python内置库冲突
from python_practice.python_oo.game.python_game import Game


class HouYi(Game):
    # 子类的init 构造方法覆盖掉了父类的构造方法
    def __init__(self, houyi_hp, your_hp, defense):
        # 继承父类的构造方法,
        # 使用关键字传参方式，给game 父类传参
        super().__init__(my_hp=houyi_hp, your_hp=your_hp)
        self.defense = defense

    def fight(self):
        # 对打多轮，谁的血量先小于等于0，谁就输了
        while True:
            self.my_hp = self.my_hp + self.defense - self.your_power
            self.your_hp = self.your_hp - self.my_power
            if self.my_hp<=0:
                # pycharm 快捷键， ctrl+D 可以复制当前行
                print("后裔的剩余血量为",self.my_hp)
                print("你的剩余血量为",self.your_hp)
                print("后裔输了")
                break
            elif self.your_hp <= 0:
                print("后裔的剩余血量为",self.my_hp)
                print("你的剩余血量为",self.your_hp)
                print("你输了")
                break


houyi = HouYi(1000, 1000 ,100)
houyi.fight()

