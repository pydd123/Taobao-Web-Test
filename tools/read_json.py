# 导包
import json


def read_json(filename):
    filepath = "../data/" + filename
    # 打开文件并调用 load方法
    with open(filepath, "r", encoding="utf-8")as f:
        datas = json.load(f)
    # arrs = []
    # for data in datas.values():
    #     arrs.append((data["username"],
    #                  data["pwd"],
    #                  data["expect_result"],
    #                  data["success"]
    #                  ))
    return datas

if __name__ == '__main__':
    print(read_json("login_data.json"))
