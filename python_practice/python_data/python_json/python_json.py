import json
# json.dump 表示把python对象写入在文件中
# json.dumps 表示把python对象 ,转化成字符串（dumps 代表dump-> string）
dict_hogwarts = {
    "a" : [1,2,3],
    "name": ["sprider man", "星矢"]
}
# # 在data.json当中写入python object 数据
# with open("data.json", "w") as f:
#     json.dump(dict_hogwarts, f , ensure_ascii=False)
print(type(dict_hogwarts))
print(type(json.dumps(dict_hogwarts)))

json_load = json.load(open("data.json"))
print("使用json_load的数据为", type(json_load))

