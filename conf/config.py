# 数据库配置
db_host="115.28.108.130"
db_port=3306
db_user='test'
db_password='123456'
db='longtengserver'


# 路径配置
import os
project_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_file=os.path.join(project_path,'data','data.xlsx')
log_file=os.path.join(project_path,'log','log.txt')
report_file=os.path.join(project_path,'report','report.html')



# log配置
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,)


# 邮件配置
smtp_server='smtp.163.com'
smtp_user="ivan-me@163.com"
smtp_password="hanzhichao123"

receiver='296170764@qq.com'
subject="接口测试报告"
body="hi all,\n附件是接口测试报告，请查收。"

is_send_report=True



if __name__ == '__main__':
    logging.info('hello world')