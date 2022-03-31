"""获取登录成功的令牌, 拼接到请求头, 返回"""
import logging

import requests


# 定义函数
def get_header():
    resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"}
                         )
    # 从登录成功的响应体中, 获取 data 的值
    token = 'Bearer ' + resp.json().get('data')
    # 使用日志记录
    logging.info(f"获取到的token: {token}")
    header = {"Content-Type": "application/json",
              "Authorization": token}
    # 返回封装好的请求头
    return header

if __name__ == '__main__':
    print(get_header())



    """
        __file__: 获取 当前文件的绝对路径
        BASE_DIR=os.path.dirname(__file__): 获取 到 当前文件的上一级目录
            此代码写在 config.py 中, 可以直接获取项目目录
        项目中使用:
            1. config.py中, 添加获取项目路径 全局变量 BASE_DIR = os.path.dirname(__file__)
            2. 修改 read_json_util 中 read_json_data() 函数, 添加参数 path_filename
            3. 使用此函数时, 拼接 json 文件路径, 传入到函数中.
    
    
    """