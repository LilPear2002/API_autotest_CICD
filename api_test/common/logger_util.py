import logging
import time
import os

class LoggerUtil:

    def create_log(self, logger_name='log'):
        # 1.创建日志收集器
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 2.防止日志重复打印 （单例模式或者判断handlers）
        if not self.logger.handlers:
            # 3.定义日志文件的路径和文件名
            # 获取项目根目录
            root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # 拼接logs目录
            log_path = os.path.join(root_path, 'logs')
            # 如果目录不存在则创建
            if not os.path.exists(log_path):
                os.mkdir(log_path)

            # 文件名按日期命名
            current_time = time.strftime('%Y_%m_%d')
            log_file_name = os.path.join(log_path, f"{current_time}_test.log")

            # 4.创建文件处理器-写入文件
            file_handler = logging.FileHandler(log_file_name, encoding='utf-8')
            file_handler.setLevel(logging.INFO)

            # 5.创建控制台处理器-输出到控制台
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # 6.定义日志格式
            # 时间-文件名[行号]-日志级别-消息
            formatter = logging.Formatter(
                '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # 7.添加处理器到收集器
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

        return self.logger

# 全局初始化一个logger供其他模块直接导入使用
logger = LoggerUtil().create_log()