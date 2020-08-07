import pytest
import yaml

from pythoncode.calc import Calculator


@pytest.fixture(scope='module')
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")


@pytest.fixture(scope='class')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


with open('./datas/calc.yml') as f:
    datas = yaml.safe_load(f)['add']
    adddatas = datas['datas']
    print(adddatas)
    myid = datas['myid']
    print(myid)


@pytest.fixture(params=adddatas, ids=myid)
def get_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")
