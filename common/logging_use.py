import logging.handlers
import logging
import time


def init_log_config(filename, when='midnight', interval=1, backup_count=7):
    """
    功能：初始化日志配置函数
    :param filename: 日志文件名
    :param when: 设定日志切分的间隔时间单位
    :param interval: 间隔时间单位的个数，指等待多少个 when 后继续进行日志记录
    :param backup_count: 保留日志文件的个数
    :return:
    """
    # 1. 创建日志器对象
    logger = logging.getLogger()

    # 2. 设置日志打印级别
    logger.setLevel(logging.DEBUG)
    # logging.DEBUG 调试级别
    # logging.INFO 信息级别
    # logging.WARNING 警告级别
    # logging.ERROR 错误级别
    # logging.CRITICAL 严重错误级别

    # 3. 创建处理器对象
    # 控制台对象
    st = logging.StreamHandler()
    # 日志文件对象
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when=when,
                                                   interval=interval,
                                                   backupCount=backup_count,
                                                   encoding='utf-8')

    # 4. 日志信息格式
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 5. 给处理器设置日志信息格式
    st.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 6. 给日志器添加处理器
    logger.addHandler(st)
    logger.addHandler(fh)


if __name__ == '__main__':
    # 初始化日志
    init_log_config('a.log')
    # 打印输出日志信息
    logging.debug('我是一个调试级别的日志')
    a=100
    logging.info(f'我是一个 info 级别的信息 a={a}')