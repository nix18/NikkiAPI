import sqlite3
import time
# 检查数据库连接
from utils.dbUtils import txt2dic

conn=sqlite3.connect("api.db")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" 连接数据库成功")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS `Nikki`;")
conn.commit()
c.execute('''CREATE TABLE Nikki
       (QUES    varchar(500) PRIMARY KEY     NOT NULL,
        ANS     varchar(500) NOT NULL
       );''')
conn.commit()
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" 表创建成功")
dic=txt2dic()
for keys in dic:
    c.execute("INSERT INTO Nikki VALUES ('{}','{}')".format(keys,dic[keys]))
conn.commit()
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" 表初始化数据成功")
conn.close()