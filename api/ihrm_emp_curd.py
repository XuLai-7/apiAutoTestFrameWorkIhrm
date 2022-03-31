"""员工管理模块的 接口对象层"""
import requests


class IhrmEmpCURD(object):
    # 添加员工
    # header 中的令牌 是变化的
    @classmethod
    def add_emp(cls, header, json_data):
        url = "http://ihrm-test.itheima.net/api/sys/user"
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp

    # 查询员工
    @classmethod
    def query_emp(cls, header, emp_id):
        # 字符串 拼接上 传递过来的员工id
        # 传递过来的 emp_id 要是字符串才行
        url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
        print("拼接好的url= ",url)
        resp = requests.get(url=url, headers=header)
        return resp

    # 修改员工
    @classmethod
    def modify_emp(cls, header, emp_id, modify_data):
        url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
        resp = requests.put(url=url, headers=header, json=modify_data)
        return resp

    # 　删除员工
    @classmethod
    def delete_emp(cls, header, emp_id):
        url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
        resp = requests.delete(url=url, headers=header)
        return resp


if __name__ == '__main__':
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer 5e78e5a4-7d5b-4af8-be57-711c987a3ba8"}
    json_data = {"username": "cyj2", "mobile": "12132312729", "workNumber": "9004"}
    modify_data = {"username": "xwh"}
    # emp_id 需要写成 字符串的形式 传递, 否则和字符串拼接不过
    emp_id = "1508394740977098752"
    print("添加: ", IhrmEmpCURD.add_emp(header, json_data).json())
    print("查询: ", IhrmEmpCURD.query_emp(header, emp_id).json())
    print("修改: ", IhrmEmpCURD.modify_emp(header, emp_id, modify_data).json())
    print("删除: ", IhrmEmpCURD.delete_emp(header, emp_id).json())

#     测试通过, 说明以上实现的接口方法 没有问题.
