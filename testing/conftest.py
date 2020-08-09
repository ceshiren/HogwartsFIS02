from typing import List

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


import os

# 通过 os.path.dirname能够获取文件所在的目录
yamlfilepath = os.path.dirname(__file__) + "/datas/calc.yml"
# . 代表当前路径，  也就是说你在哪个路径下执行测试文件，就叫做当前路径
with open(yamlfilepath) as f:
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


# 如果不去定义这些hook 函数， 它会按照pytest默认的规则去运行测试用例
# 如果在conftest.py文件里面定义的这些hook函数， 名字和参数要与官网定义的一模一样，
# 在Hook函数内部 实现要改写的规则
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param _pytest.main.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[_pytest.nodes.Item] items: List of item objects.
    """
    print("items")
    print(items)
    # 测试用例反转
    items.reverse()
    # 测试用例参数的编码格式改写
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # 如果测试用例里面有 字符，则自动的添加一些标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)

        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)

        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts-FIS")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 参数说明
                      )

    mygroup.addoption("--des",  # 注册一个命令行选项
                      default='aaa',  # 默认值
                      dest='aaa',  # 存储的变量
                      help='set your param'  # 参数说明
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')
