import json


# path_filename 使用绝对路径
def read_json_data(path_filename):
    # 读取 json 文件
    # 从json 文件中读取 [{},{},{},...] 字典列表 数据
    with open(path_filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    # [{},{},{},...] 字典列表 ----> [(),(),(),...] 元组列表
    list_data = []
    for item in json_data:
        tmp = tuple(item.values())
        # 截掉 desc , 追加到列表
        # list_data.append(tmp[1:])
        list_data.append(tmp)
    return list_data


if __name__ == '__main__':
    print(read_json_data("../data/ihrm_login.json"))
