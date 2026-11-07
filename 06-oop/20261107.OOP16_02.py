'''请创建一个日志记录器类 Logger，满足以下需求：
该类包含一个类属性 log_file，表示日志文件的名称，默认为 app.log。
实现一个类方法 set_log_file(cls, filename)，用于更改日志文件的名称。
实现一个静态方法 log(message)，用于将日志消息写入指定的日志文件。
日志消息需要包含时间戳和日志级别（如 INFO、WARNING、ERROR）。'''
import datetime
class Logger:
    log_file = 'app.log'
    @classmethod
    def set_log_file(cls, filename):
        cls.log_file = filename
    @staticmethod
    def log(msg, level='INFO'):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f'{timestamp} [{level}] {msg}\n'
        with open(Logger.log_file, 'a') as f:
            f.write(log_msg)

# 设置日志文件名称
Logger.set_log_file("fishc_app.log")
   
# 记录不同级别的日志消息
Logger.log("应用启动。", level="INFO")
Logger.log("出现异常。", level="ERROR")
Logger.log("用户登入。", level="INFO")
Logger.log("内存空间不足。", level="WARNING")

# 查看日志文件 "fishc_app.log" 中的内容
with open("fishc_app.log", "r") as f:
    content = f.read()
    print("日志文件内容：")
    print(content)