import sqlite3
import time


def txt2dic():
    # 声明一个空字典，来保存文本文件数据
    dict_temp = {}

    # 打开文本文件
    file = open('dic.txt', 'r', encoding="UTF-8")

    # 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    for line in file.readlines():
        line = line.strip()
        k = line.split('::')[0]
        v = line.split('::')[1]
        dict_temp[k] = v

    # 依旧是关闭文件
    file.close()

    return dict_temp


def outAns(ques):
    conn = sqlite3.connect("api.db")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 连接数据库成功")
    c = conn.cursor()
    cursor=c.execute("SELECT ANS FROM Nikki WHERE QUES LIKE '%{}%'".format(ques))
    ans=cursor.fetchone()
    if ans==None:
        return "查不到答案"
    return ans[0]
