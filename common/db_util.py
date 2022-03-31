"""
 将常用的数据库操作, 封装到一个方法, 后续再操作数据库时, 通过调用该方法来实现.
 封装数据库操作类
"""
import logging

import pymysql


class DBUtil(object):
    # 添加类属性
    conn = None

    @classmethod
    def __get_conn(cls):
        # 判断 conn 是否为空
        if cls.conn is None:
            cls.conn = pymysql.connect(host="211.103.136.244", port=7061, user="student", password="iHRM_student_2021",
                                       database="ihrm", charset="utf8")
            # cls.conn = pymysql.connect(host="localhost", port=3306, user="root", password="root",
            #                            database="ihrm", charset="utf8")
        # 返回非空连接, 用户多次操作, 都是一个连接
        return cls.conn

    # 关闭连接
    @classmethod
    def __close_conn(cls):
        # 如果用户在操作中关过连接,就不用关了.
        # 不为空,没关,就关闭连接
        if cls.conn is not None:
            cls.conn.close()
            # 下次关闭连接,判断为空,就不会执行再次关闭连接
            cls.conn = None

    # 查询一条
    @classmethod
    def select_one(cls, sql):
        # global 变量名, 定义全局变量
        # global cursor, res
        cursor = None
        res = None
        try:
            # 获取连接
            # 返回的就是类变量,用类变量接收
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            # 提取一条结果
            res = cursor.fetchone()
        except Exception as err:
            print("查询语句执行错误:", str(err))
        finally:
            cursor.close()
            cls.__close_conn()
            return res

    # 查询多条
    # 查询所有
    # 增删改
    @classmethod
    def uid_db(cls, sql):
        cursor = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            # print("影响的行数: ", cls.conn.affected_rows())
            logging.info(f"影响的行数: {cls.conn.affected_rows()}")
            cls.conn.commit()
        except Exception as err:
            # print("增删改语句执行出错:", str(err))
            logging.error(f"增删改语句执行出错: {str(err)}")
            cls.conn.rollback()
        finally:
            cursor.close()
            # 重要,报错就在这
            cls.__close_conn()


    # def __方法名() 定义一个私有的方法
    # global 变量名, 定义全局变量
    # global cursor, res


if __name__ == '__main__':
    # print(DBUtil.select_one("select * from t_book"))
    # print(DBUtil.select_one("select * from t_book where id = 666"))
    # DBUtil.uid_db("update t_book set title ='laptop' where id = 1")
    # DBUtil.uid_db("insert into t_book(id,title,pub_date) values(6,'keyboard','2022-03-26')")
    # DBUtil.uid_db("delete from t_book where id =1")
    # 伪删除
    # DBUtil.uid_db("update t_book set is_delete = 1 where id = 3")
    # 真正的删除
    DBUtil.uid_db("delete from t_book where id = 3")
