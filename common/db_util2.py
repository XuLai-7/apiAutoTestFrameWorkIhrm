import pymysql

# 封装数据库工具类
class DBUtil(object):
    # 添加类属性
    conn = None

    @classmethod
    def __get_conn(cls):
        # 判断 conn 是否为空，如果是，再创建
        if cls.conn is None:
            cls.conn = pymysql.connect(host="211.103.136.244", port=7061, user="student",
                                       password="iHRM_student_2021", database="ihrm", charset="utf8")
        # 返回 非空连接
        return cls.conn

    @classmethod
    def __close_conn(cls):
        # 判断，conn 不为空，需要关闭。
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None

    # 常用方法：查询一条
    @classmethod
    def select_one(cls, sql):
        cursor = None
        res = None
        try:
            # 获取连接
            cls.conn = cls.__get_conn()

            # 获取游标
            cursor = cls.conn.cursor()

            # 执行 查询语句
            cursor.execute(sql)

            # 提取一条结果
            res = cursor.fetchone()

        except Exception as err:
            print("查询sql错误：", str(err))
        finally:
            # 关闭游标
            cursor.close()

            # 关闭连接
            cls.__close_conn()

            # 将查询sql执行的 结果，返回
            return res

    # 常用方法：增删改
    @classmethod
    def uid_db(cls, sql):
        cursor = None
        try:
            # 获取连接
            cls.conn = cls.__get_conn()

            # 获取游标
            cursor = cls.conn.cursor()

            # 执行 uid 语句
            cursor.execute(sql)
            print("影响的行数：", cls.conn.affected_rows())

            # 提交事务
            cls.conn.commit()

        except Exception as err:
            # 回滚事务
            cls.conn.rollback()
            print("增删改 SQL 执行失败：", str(err))

        finally:
            # 关闭游标
            cursor.close()
            # 关闭连接
            cls.__close_conn()


if __name__ == '__main__':
    res = DBUtil.select_one("select * from t_book;")
    print("查询结果为：", res)

    DBUtil.uid_db("update t_book set is_delete = 1 where id = 1111;")
