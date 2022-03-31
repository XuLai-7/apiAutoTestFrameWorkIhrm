
import requests

"""
# 添加员工
url = "http://ihrm-test.itheima.net/api/sys/user"
header = {"Content-Type": "application/json", "Authorization": "Bearer 1bca1f3c-8784-400b-af87-24169c30af7a"}
json_data = {"username": "cyj2", "mobile": "12132312723", "workNumber": "9004"}
resp = requests.post(url=url,headers=header,json=json_data)
print("添加员工: ", resp.json())
"""
# 查询员工
"""
url_query="http://ihrm-test.itheima.net/api/sys/user/1508378758732701696"
header_query={"Authorization": "Bearer 1bca1f3c-8784-400b-af87-24169c30af7a"}
resp = requests.get(url=url_query,headers=header_query)
print("查询员工: ",resp.json())
"""
"""
# 修改员工
url_modify="http://ihrm-test.itheima.net/api/sys/user/1508378758732701696"
header_modify = {"Content-Type": "application/json", "Authorization": "Bearer 1bca1f3c-8784-400b-af87-24169c30af7a"}
modify_data={
"username":"xwh"
}
resp_modify = requests.put(url=url_modify,headers=header_modify,json=modify_data)
print("修改员工: ",resp_modify.json())
"""
# 删除员工
url_del = "http://ihrm-test.itheima.net/api/sys/user/1508378758732701696"
header_del = {"Authorization": "Bearer 1bca1f3c-8784-400b-af87-24169c30af7a"}
resp_del = requests.delete(url=url_del, headers=header_del)
print("删除员工: ", resp_del.json())
