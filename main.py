import tkinter as tk
import tkinter.messagebox
from tkinter import *
import pymysql
from PIL import Image, ImageTk
from datetime import datetime
import numpy as np

#增删改查之后进去每个都可以对员工信息 商品信息 安全信息 仓库信息 供货信息 退货信息 会员信息进行操作


################################################################################################################

#数据库添加操作
def add_Goods():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Goods(Gnum,Gname,Gtype,Gprice,Gbid,Gstock,Galarm,Gplan,Vnum) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql,(g1.get(), g2.get(), g3.get(), g4.get(), g5.get(), g6.get(), g7.get(), g8.get(), g9.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Staff():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Staff(Snum,Sname,Ssex,Sage,Sseniority,Sphone,Sid,Ssalary,Syard) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql,(s1.get(), s2.get(), s3.get(), s4.get(), s5.get(), s6.get(), s7.get(), s8.get(), s9.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Check1():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Check(Cdate,Cyard,Cfire,Cspary) values(%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql, (c1.get(), c2.get(), c3.get(), c4.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Ware():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Ware(Wnum,Wname,Wplace,Snum) values(%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql, (w1.get(), w2.get(), w3.get(), w4.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Vendor():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Vendor(Vnum,Vname,Vphone,Vplace) values(%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql, (v1.get(), v2.get(), v3.get(), v4.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Infer():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Infer(Tnum,Gnum,Iamount,Imoney,Idate) values(%s,%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql, (i1.get(), i2.get(), i3.get(), i4.get(), i5.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Member():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Member(Mnum,Mname,Mphone,Mdate,Mtotal,Mbalance,Mpassword) values(%s,%s,%s,%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql, (m1.get(), m2.get(), m3.get(), m4.get(), m5.get(),m6.get(),m7.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Trade():
    global t5,t1,t6

    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 计算金额
    cursor.execute("select Gprice from Trade,Goods where Trade.Gnum=Goods.Gnum and Goods.Gnum=%s", (t4.get()))
    connect.commit()
    reGprice = cursor.fetchall()  # 商品单价,是元组形式，需要提取出元素
    reGprice = np.array(reGprice)  # 将列表转换成数组
    reGprice = [[int(num) for num in lst] for lst in reGprice]  # 把数组中的字符串转换成数字
    reGprice = np.array(reGprice)  # 再次转换成数组
    reGprice = reGprice[0][0]#得到数组中的值
    string_value = t5.get() #得到t5的值
    int_value = int(string_value)#把stringvar类型转换成int
    t6 = int_value * reGprice

    # 编写SQL语句
    sql = "insert into Trade(Tnum,Tdate,Snum,Gnum,Tamount,Tmoney,Mnum) values(%s,%s,%s,%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql, (t1, t2, t3.get(), t4.get(), t5.get(),t6,t7.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
        tkinter.messagebox.showinfo(title='消费的金额是', message=t6)
        #sql = "select Gstock from Goods where Gnum=%s"
        #cursor.execute(sql, (t4.get()))
        #result1=cursor.fetchall()
        #sql = "select Galarm from Goods where Gnum=%s"
        #cursor.execute(sql, (t4.get()))
        #result2 = cursor.fetchall()
        #if(result1<result2):
            #tkinter.messagebox.showinfo(title='提示', message='该商品较少，需要补货')
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Entry():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Entry(Enum,Gnum,Eamount,Emoney,Vnum,Edate,Snum) values(%s,%s,%s,%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql, (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(),e6.get(),e7.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
def add_Exits():
    # 连接数据库
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Exits(Xnum,Gnum,Xamount,Xmoney,Xdate,Snum) values(%s,%s,%s,%s,%s,%s)"
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql, (x1.get(), x2.get(), x3.get(), x4.get(), x5.get(),x6.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    connect.close()
########################################################################################################################
#数据库删除操作
def delete_Goods():
    connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
    cursor=connect.cursor()
    sql = "delete from Goods where Gnum=%s"
    try:
        cursor.execute(sql,(g10.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示","数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Staff():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Staff where Snum=%s"
    try:
        cursor.execute(sql, (s10.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Check1():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Check where Cdate=%s"
    try:
        cursor.execute(sql, (c6.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Ware():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Ware where Wnum=%s"
    try:
        cursor.execute(sql, (w5.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Vendor():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Vendor where Vnum=%s"
    try:
        cursor.execute(sql, (v5.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Infer():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Infer where Tnum=%s"
    try:
        cursor.execute(sql, (i6.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Member():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Member where Mnum=%s"
    try:
        cursor.execute(sql, (m8.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Trade():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Trade where Tnum=%s"
    try:
        cursor.execute(sql, (t8.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Entry():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Entry where Enum=%s"
    try:
        cursor.execute(sql, (e8.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
def delete_Exits():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "delete from Exits where Xnum=%s"
    try:
        cursor.execute(sql, (x7.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    connect.close()
#################################################################################################################################
#数据库更新操作
def update_Goods():
    connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql="update Goods set Gbid=%s,Gprice=%s where Gnum=%s"
    try:
        cursor.execute(sql,(g11.get(),g12.get(),g13.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示","数据更新成功！")
    except:
        connect.rollback()
    connect.close()
def update_Staff():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "update Staff set Sphone=%s,Ssalary=%s where Snum=%s"
    try:
        cursor.execute(sql, (s11.get(), s12.get(), s13.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据更新成功！")
    except:
        connect.rollback()
    connect.close()
def update_Ware():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "update Ware set Wname=%s,Snum=%s where Wnum=%s"
    try:
        cursor.execute(sql, (w6.get(), w7.get(), w8.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据更新成功！")
    except:
        connect.rollback()
    connect.close()
def update_Vendor():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "update Vendor set Vphone=%s,Vplace=%s where Vnum=%s"
    try:
        cursor.execute(sql, (v6.get(), v7.get(), v8.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据更新成功！")
    except:
        connect.rollback()
    connect.close()
def update_Infer():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "update Infer set Iamount=%s,Imoney=%s where Tnum=%s"
    try:
        cursor.execute(sql, (i7.get(), i8.get(), i9.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据更新成功！")
    except:
        connect.rollback()
    connect.close()
def update_Member():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "update Member set Mphone=%s,Mpassword=%s where Mnum=%s"
    try:
        cursor.execute(sql, (m9.get(), m10.get(), m11.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据更新成功！")
    except:
        connect.rollback()
    connect.close()
def update_Trade():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "update Trade set Tmoney=%s,Tamount=%s where Tnum=%s"
    try:
        cursor.execute(sql, (t9.get(), t10.get(), t11.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据更新成功！")
    except:
        connect.rollback()
    connect.close()
def update_Entry():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "update Entry set Emoney=%s,Eamount=%s where Enum=%s"
    try:
        cursor.execute(sql, (e9.get(), e10.get(), e11.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据更新成功！")
    except:
        connect.rollback()
    connect.close()
def update_Exits():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "update Exits set Xmoney=%s,Xamount=%s where Xnum=%s"
    try:
        cursor.execute(sql, (x8.get(), x9.get(), x10.get()))
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据更新成功！")
    except:
        connect.rollback()
    connect.close()
################################################################################################################################
#数据库条件查询
def select_Goods():
    connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Goods where Gnum=%s"
    try:
        cursor.execute(sql,(g14.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output',message=results)
    except:
        return
    connect.close()
def select_Staff():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Staff where Snum=%s"
    try:
        cursor.execute(sql, (s14.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()
def select_Check1():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Check where Cdate=%s"
    try:
        cursor.execute(sql, (c7.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()
def select_Ware():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Ware where Wnum=%s"
    try:
        cursor.execute(sql, (w9.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()
def select_Vendor():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Vendor where Vnum=%s"
    try:
        cursor.execute(sql, (v9.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()
def select_Infer():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Infer where Tnum=%s"
    try:
        cursor.execute(sql, (i10.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()
def select_Member():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Member where Mnum=%s"
    try:
        cursor.execute(sql, (m12.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()
def select_Trade():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Trade where Tnum=%s"
    try:
        cursor.execute(sql, (t12.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()
def select_Entry():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Entry where Enum=%s"
    try:
        cursor.execute(sql, (e12.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()
def select_Exits():
    connect = pymysql.connect(host="localhost", user="root", password="mysql", database="sqlwork")  # 建立连接
    cursor = connect.cursor()
    sql = "select * from Exits where Xnum=%s"
    try:
        cursor.execute(sql, (x11.get()))
        results = cursor.fetchall()
        tkinter.messagebox.showinfo(title='output', message=results)
    except:
        return
    connect.close()


######################################################################################################


#添加商品界面
def Goods_add():
    window_choice.destroy()
    #构建全集变量，方便上面的函数调用
    global window_function
    global g1,g2,g3,g4,g5,g6,g7,g8,g9
    #生成窗口
    window_function=tk.Tk()
    #窗口标题
    window_function.title("无人销售管理系统")
    #窗口大小
    window_function.geometry('400x700')


    #生成标签
    tk.Label(window_function, text="添加新商品", font=("黑体", 20)).grid(row=0,column=1,pady=10)
    tk.Label(window_function, text="请输入商品编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function,text="请输入商品名称：").grid(row = 2,column =0,padx=20,pady=20)
    tk.Label(window_function,text="请输入商品类别：").grid(row = 3,column =0,padx=20,pady=20)
    tk.Label(window_function,text="请输入商品售价：").grid(row = 4,column =0,padx=20,pady=20)
    tk.Label(window_function, text="请输入商品成本：").grid(row=5, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入库存量：").grid(row=6, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入告警量：").grid(row=7, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入计划库存量：").grid(row=8, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入供货商编号：").grid(row=9, column=0, padx=20, pady=20)
    #定义变量记录输入信息
    g1 = tk.StringVar()
    g2 = tk.StringVar()
    g3 = tk.StringVar()
    g4 = tk.StringVar()
    g5 = tk.StringVar()
    g6 = tk.StringVar()
    g7 = tk.StringVar()
    g8 = tk.StringVar()
    g9 = tk.StringVar()
    #生成输入框
    entry1 = tk.Entry(window_function,show=None,textvariable=g1).grid(row = 1,column =1)
    entry2 = tk.Entry(window_function,show=None,textvariable=g2).grid(row = 2,column =1)
    entry3 = tk.Entry(window_function,show=None,textvariable=g3).grid(row = 3,column =1)
    entry4 = tk.Entry(window_function, show=None, textvariable=g4).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=g5).grid(row=5, column=1)
    entry6 = tk.Entry(window_function, show=None, textvariable=g6).grid(row=6, column=1)
    entry7 = tk.Entry(window_function, show=None, textvariable=g7).grid(row=7, column=1)
    entry8 = tk.Entry(window_function, show=None, textvariable=g8).grid(row=8, column=1)
    entry9 = tk.Entry(window_function, show=None, textvariable=g9).grid(row=9, column=1)
    #生成按钮
    button = tk.Button(window_function, text="添加", command=add_Goods).place(relx=0.3,rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5,rely=0.9)


    #显示窗口
    window_function.mainloop()

#添加员工界面
def Staff_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global s1, s2, s3, s4, s5, s6, s7, s8, s9
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加新员工", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入员工编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工姓名：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工性别：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工年龄：").grid(row=4, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工工龄：").grid(row=5, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工电话：").grid(row=6, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入身份证号：").grid(row=7, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工工资：").grid(row=8, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入健康码情况：").grid(row=9, column=0, padx=20, pady=20)
    # 定义变量记录输入信息
    s1 = tk.StringVar()
    s2 = tk.StringVar()
    s3 = tk.StringVar()
    s4 = tk.StringVar()
    s5 = tk.StringVar()
    s6 = tk.StringVar()
    s7 = tk.StringVar()
    s8 = tk.StringVar()
    s9 = tk.StringVar()
    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=s1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=s2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=s3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=s4).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=s5).grid(row=5, column=1)
    entry6 = tk.Entry(window_function, show=None, textvariable=s6).grid(row=6, column=1)
    entry7 = tk.Entry(window_function, show=None, textvariable=s7).grid(row=7, column=1)
    entry8 = tk.Entry(window_function, show=None, textvariable=s8).grid(row=8, column=1)
    entry9 = tk.Entry(window_function, show=None, textvariable=s9).grid(row=9, column=1)
    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Staff).place(relx=0.3, rely=0.9)
    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)
    # 显示窗口
    window_function.mainloop()

#添加安全问题界面
def Check1_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global c1, c2, c3, c4
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加安全问题检查情况", font=("黑体", 20)).grid(row=0, column=0, pady=10)
    tk.Label(window_function, text="请输入检查日期：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入顾客健康码情况：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入灭火器情况：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入灭火喷洒装置情况：").grid(row=4, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    c1 = tk.StringVar()
    c2 = tk.StringVar()
    c3 = tk.StringVar()
    c4 = tk.StringVar()

    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=c1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=c2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=c3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=c4).grid(row=4, column=1)

    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Check1).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)

    # 显示窗口
    window_function.mainloop()
#添加仓库界面
def Ware_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global w1, w2, w3, w4
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加仓库信息", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入仓库编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入仓库名称：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入仓库地址：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入仓库管理员编号：").grid(row=4, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    w1 = tk.StringVar()
    w2 = tk.StringVar()
    w3 = tk.StringVar()
    w4 = tk.StringVar()

    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=w1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=w2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=w3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=w4).grid(row=4, column=1)

    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Ware).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)

    # 显示窗口
    window_function.mainloop()

#添加供货商界面
def Vendor_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global v1, v2, v3, v4
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加供货商信息", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入供货商编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入供货商名称：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入供货商电话：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入供货商地址：").grid(row=4, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    v3 = tk.StringVar()
    v4 = tk.StringVar()

    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=v1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=v2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=v3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=v4).grid(row=4, column=1)

    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Vendor).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)

    # 显示窗口
    window_function.mainloop()

#添加退货信息界面
def Infer_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global i1, i2, i3, i4,i5
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加退货信息", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入交易流水号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入商品编号：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入退货数量：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入退款金额：").grid(row=4, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入退货日期：").grid(row=5, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    i1 = tk.StringVar()
    i2 = tk.StringVar()
    i3 = tk.StringVar()
    i4 = tk.StringVar()
    i5 = tk.StringVar()

    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=i1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=i2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=i3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=i4).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=i5).grid(row=5, column=1)

    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Infer).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)

    # 显示窗口
    window_function.mainloop()

#添加会员表界面
def Member_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global m1, m2, m3, m4, m5, m6, m7
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加新会员", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入会员卡号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入会员姓名：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入会员电话：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入注册日期：").grid(row=4, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入累计金额：").grid(row=5, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入卡内余额：").grid(row=6, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入会员密码：").grid(row=7, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    m1 = tk.StringVar()
    m2 = tk.StringVar()
    m3 = tk.StringVar()
    m4 = tk.StringVar()
    m5 = tk.StringVar()
    m6 = tk.StringVar()
    m7 = tk.StringVar()

    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=m1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=m2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=m3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=m4).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=m5).grid(row=5, column=1)
    entry6 = tk.Entry(window_function, show=None, textvariable=m6).grid(row=6, column=1)
    entry7 = tk.Entry(window_function, show=None, textvariable=m7).grid(row=7, column=1)

    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Member).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)

    # 显示窗口
    window_function.mainloop()

#添加商品交易界面
def Trade_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global t1, t2, t3, t4, t5, t6, t7
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加商品交易信息", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    #tk.Label(window_function, text="请输入交易流水号：").grid(row=1, column=0, padx=20, pady=20)
    #tk.Label(window_function, text="请输入交易日期：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工编号：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入商品编号：").grid(row=4, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入交易数量：").grid(row=5, column=0, padx=20, pady=20)
    #tk.Label(window_function, text="请输入交易金额：").grid(row=6, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入会员卡号：").grid(row=7, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    t1 = datetime.now().strftime("%Y%m%d%H%M%S")   # '20230329201142' #把当前日期时间设置成交易流水号
    t2 = datetime.now() #当前系统日期和时间
    t3 = tk.StringVar()
    t4 = tk.StringVar()
    t5 = tk.StringVar()
    #t6 = tk.StringVar()
    t7 = tk.StringVar()

    # 生成输入框
    #entry1 = tk.Entry(window_function, show=None, textvariable=t1).grid(row=1, column=1)
    #entry2 = tk.Entry(window_function, show=None, textvariable=t2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=t3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=t4).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=t5).grid(row=5, column=1)
    #entry6 = tk.Entry(window_function, show=None, textvariable=t6).grid(row=6, column=1)
    entry7 = tk.Entry(window_function, show=None, textvariable=t7).grid(row=7, column=1)

    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Trade).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)

    # 显示窗口
    window_function.mainloop()

#添加入库信息界面
def Entry_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global e1, e2, e3, e4, e5, e6, e7
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加入库信息", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入入库单编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入商品编号：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入入库量：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入总金额：").grid(row=4, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入供货商编号：").grid(row=5, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入入库日期：").grid(row=6, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入入库员编号：").grid(row=7, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    e1 = tk.StringVar()
    e2 = tk.StringVar()
    e3 = tk.StringVar()
    e4 = tk.StringVar()
    e5 = tk.StringVar()
    e6 = tk.StringVar()
    e7 = tk.StringVar()

    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=e1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=e2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=e3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=e4).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=e5).grid(row=5, column=1)
    entry6 = tk.Entry(window_function, show=None, textvariable=e6).grid(row=6, column=1)
    entry7 = tk.Entry(window_function, show=None, textvariable=e7).grid(row=7, column=1)

    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Entry).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)

    # 显示窗口
    window_function.mainloop()

#添加出库信息界面
def Exits_add():
    window_choice.destroy()
    # 构建全集变量，方便上面的函数调用
    global window_function
    global x1, x2, x3, x4, x5, x6
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("无人销售管理系统")
    # 窗口大小
    window_function.geometry('400x700')

    # 生成标签
    tk.Label(window_function, text="添加出库信息", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入出库单编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入商品编号：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入出库量：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入总金额：").grid(row=4, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入出库日期：").grid(row=5, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入出库员编号：").grid(row=6, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    x1 = tk.StringVar()
    x2 = tk.StringVar()
    x3 = tk.StringVar()
    x4 = tk.StringVar()
    x5 = tk.StringVar()
    x6 = tk.StringVar()

    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=x1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=x2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=x3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=x4).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=x5).grid(row=5, column=1)
    entry6 = tk.Entry(window_function, show=None, textvariable=x6).grid(row=6, column=1)

    # 生成按钮
    button = tk.Button(window_function, text="添加", command=add_Exits).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=change_add).place(relx=0.5, rely=0.9)

    # 显示窗口
    window_function.mainloop()

############################################################################################

#删除商品界面
def Goods_delete():
    window_choice.destroy()
    global window_function
    global g10
    window_function=tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除商品", font=("黑体", 20)).grid(row=0,column=1,pady=20)
    tk.Label(window_function,text="请输入商品编号：").grid(row = 1,column =0,padx=20)
    g10 =tk.StringVar()
    entry1=tk.Entry(window_function,show=None,textvariable=g10).grid(row = 1,column =1,pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Goods,anchor = 's').place(relx=0.2,rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4,rely=0.5)
    window_function.mainloop()


# 删除员工界面
def Staff_delete():
    window_choice.destroy()
    global window_function
    global s10
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除员工", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入员工编号：").grid(row=1, column=0, padx=20)
    s10 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=s10).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Staff, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()


# 删除安全问题界面
def Check1_delete():
    window_choice.destroy()
    global window_function
    global c6
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除检查安全记录", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入检查日期：").grid(row=1, column=0, padx=20)
    c6 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=c6).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Check1, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()

# 删除仓库界面
def Ware_delete():
    window_choice.destroy()
    global window_function
    global w5
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除仓库", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入仓库编号：").grid(row=1, column=0, padx=20)
    w5 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=w5).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Ware, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()


# 删除供货商界面
def Vendor_delete():
    window_choice.destroy()
    global window_function
    global v5
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除供货商", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入供货商编号：").grid(row=1, column=0, padx=20)
    v5 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=v5).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Vendor, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()


# 删除退货信息界面
def Infer_delete():
    window_choice.destroy()
    global window_function
    global i6
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除退货信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入交易流水号：").grid(row=1, column=0, padx=20)
    i6 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=i6).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Infer, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()


# 删除会员表界面
def Member_delete():
    window_choice.destroy()
    global window_function
    global m8
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除会员信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入会员卡号：").grid(row=1, column=0, padx=20)
    m8 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=m8).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Member, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()

#删除商品交易记录界面
def Trade_delete():
    window_choice.destroy()
    global window_function
    global t8
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除商品交易记录", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入交易流水号：").grid(row=1, column=0, padx=20)
    t8 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=t8).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Trade, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()

#删除入库信息界面
def Entry_delete():
    window_choice.destroy()
    global window_function
    global e8
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除入库信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入入库单编号：").grid(row=1, column=0, padx=20)
    e8 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=e8).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Entry, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()

#删除出库信息界面
def Exits_delete():
    window_choice.destroy()
    global window_function
    global x7
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="删除出库信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入出库单编号：").grid(row=1, column=0, padx=20)
    x7 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=x7).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="删除", command=delete_Exits, anchor='s').place(relx=0.2, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_delete).place(relx=0.4, rely=0.5)
    window_function.mainloop()

#####################################################################################
#更新商品信息界面
def Goods_update():
    window_choice.destroy()
    global window_function
    global g11,g12,g13
    window_function=tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新商品信息", font=("黑体", 20)).grid(row=0,column=1,pady=20)
    tk.Label(window_function,text="请输入商品进价：").grid(row=1,column =0,padx=20,pady=20)
    tk.Label(window_function,text="请输入商品售价：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function,text="请输入商品编号：").grid(row=3,column =0,padx=20,pady=20)
    g11=tk.StringVar()
    g12=tk.StringVar()
    g13=tk.StringVar()
    entry1=tk.Entry(window_function,show=None,textvariable=g11).grid(row=1,column =1)
    entry2=tk.Entry(window_function,show=None,textvariable=g12).grid(row=2,column =1)
    entry3 = tk.Entry(window_function, show=None, textvariable=g13).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Goods).place(relx=0.3,rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5,rely=0.8)
    window_function.mainloop()

# 更新员工界面
def Staff_update():
    window_choice.destroy()
    global window_function
    global s11, s12, s13
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新员工信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入员工电话：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工工资：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入员工编号：").grid(row=3, column=0, padx=20, pady=20)
    s11 = tk.StringVar()
    s12 = tk.StringVar()
    s13 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=s11).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=s12).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=s13).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Staff).place(relx=0.3, rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5, rely=0.8)
    window_function.mainloop()


# 更新仓库界面
def Ware_update():
    window_choice.destroy()
    global window_function
    global w6,w7,w8
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新仓库信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入仓库名称：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入仓库管理员编号：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入仓库编号：").grid(row=3, column=0, padx=20, pady=20)
    w6 = tk.StringVar()
    w7 = tk.StringVar()
    w8 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=w6).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=w7).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=w8).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Ware).place(relx=0.3, rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5, rely=0.8)
    window_function.mainloop()


# 更新供货商界面
def Vendor_update():
    window_choice.destroy()
    global window_function
    global v6, v7, v8
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新供货商信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入供货商电话：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入供货商地址：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入供货商编号：").grid(row=3, column=0, padx=20, pady=20)
    v6 = tk.StringVar()
    v7 = tk.StringVar()
    v8 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=v6).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=v7).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=v8).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Vendor).place(relx=0.3, rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5, rely=0.8)
    window_function.mainloop()


# 更新退货信息界面
def Infer_update():
    window_choice.destroy()
    global window_function
    global i7,i8,i9
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新供货商信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入退货数量：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入退款金额：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入交易流水号编号：").grid(row=3, column=0, padx=20, pady=20)
    i7 = tk.StringVar()
    i8 = tk.StringVar()
    i9 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=i7).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=i8).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=i9).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Infer).place(relx=0.3, rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5, rely=0.8)
    window_function.mainloop()


# 更新会员表界面
def Member_update():
    window_choice.destroy()
    global window_function
    global m9,m10,m11
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新供货商信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入会员电话：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入会员密码：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入会员卡号编号：").grid(row=3, column=0, padx=20, pady=20)
    m9 = tk.StringVar()
    m10 = tk.StringVar()
    m11 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=m9).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=m10).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=m11).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Member).place(relx=0.3, rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5, rely=0.8)
    window_function.mainloop()

#更新商品交易记录界面
def Trade_update():
    window_choice.destroy()
    global window_function
    global t9,t10,t11
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新商品交易信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入交易金额：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入交易数量：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入交易流水号：").grid(row=3, column=0, padx=20, pady=20)
    t9 = tk.StringVar()
    t10 = tk.StringVar()
    t11 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=t9).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=t10).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=t11).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Trade).place(relx=0.3, rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5, rely=0.8)
    window_function.mainloop()

#更新入库信息界面
def Entry_update():
    window_choice.destroy()
    global window_function
    global e9,e10,e11
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新供货商信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入总金额：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入入库量：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入入库单编号：").grid(row=3, column=0, padx=20, pady=20)
    e9 = tk.StringVar()
    e10 = tk.StringVar()
    e11= tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=e9).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=e10).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=e11).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Entry).place(relx=0.3, rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5, rely=0.8)
    window_function.mainloop()

#更新出库信息界面
def Exits_update():
    window_choice.destroy()
    global window_function
    global x8,x9,x10
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="更新供货商信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入总金额：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入出库量：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入出库单编号：").grid(row=3, column=0, padx=20, pady=20)
    x8 = tk.StringVar()
    x9 = tk.StringVar()
    x10 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=x8).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=x9).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=x10).grid(row=3, column=1)
    button = tk.Button(window_function, text="更新", command=update_Exits).place(relx=0.3, rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=change_update).place(relx=0.5, rely=0.8)
    window_function.mainloop()

#############################################################################################################################

#条件查找商品界面
def Goods_select():
    window_choice.destroy()
    global window_function
    global g14
    window_function=tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找商品信息", font=("黑体", 20)).grid(row=0,column=1,pady=20)
    tk.Label(window_function,text="请输入商品编号：").grid(row = 1,column =0,padx=20)
    g14 =tk.StringVar()
    entry1=tk.Entry(window_function,show=None,textvariable=g14).grid(row = 1,column =1,pady=40)
    button = tk.Button(window_function, text="查找", command=select_Goods).place(relx=0.3,rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5,rely=0.5)
    window_function.mainloop()

# 查找员工界面
def Staff_select():
    window_choice.destroy()
    global window_function
    global s14
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找员工信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入员工编号：").grid(row=1, column=0, padx=20)
    s14 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=s14).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Staff).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()


# 查找安全问题界面
def Check1_select():
    window_choice.destroy()
    global window_function
    global c7
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找安全检查信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入检查日期：").grid(row=1, column=0, padx=20)
    c7 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=c7).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Check1).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()

# 查找仓库界面
def Ware_select():
    window_choice.destroy()
    global window_function
    global w9
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找仓库信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入仓库编号：").grid(row=1, column=0, padx=20)
    w9 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=w9).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Ware).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()


# 查找供货商界面
def Vendor_select():
    window_choice.destroy()
    global window_function
    global v9
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找供货商信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入供货商编号：").grid(row=1, column=0, padx=20)
    v9 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=v9).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Vendor).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()


# 查找退货信息界面
def Infer_select():
    window_choice.destroy()
    global window_function
    global i10
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找退货信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入交易流水号：").grid(row=1, column=0, padx=20)
    i10 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=i10).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Infer).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()


# 查找会员表界面
def Member_select():
    window_choice.destroy()
    global window_function
    global m12
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找会员信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入会员卡号：").grid(row=1, column=0, padx=20)
    m12 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=m12).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Member).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()

#查找商品交易记录界面
def Trade_select():
    window_choice.destroy()
    global window_function
    global t12
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找商品交易信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入交易流水号：").grid(row=1, column=0, padx=20)
    t12 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=t12).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Trade).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()

#查找入库信息界面
def Entry_select():
    window_choice.destroy()
    global window_function
    global e12
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找入库信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入入库单编号：").grid(row=1, column=0, padx=20)
    e12 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=e12).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Entry).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()

#查找出库信息界面
def Exits_select():
    window_choice.destroy()
    global window_function
    global x11
    window_function = tk.Tk()
    window_function.title("无人销售管理系统")
    window_function.geometry('500x400')
    tk.Label(window_function, text="查找出库信息", font=("黑体", 20)).grid(row=0, column=1, pady=20)
    tk.Label(window_function, text="请输入出库单编号：").grid(row=1, column=0, padx=20)
    x11 = tk.StringVar()
    entry1 = tk.Entry(window_function, show=None, textvariable=x11).grid(row=1, column=1, pady=40)
    button = tk.Button(window_function, text="查找", command=select_Exits).place(relx=0.3, rely=0.5)
    button2 = tk.Button(window_function, text="返回", command=change_select).place(relx=0.5, rely=0.5)
    window_function.mainloop()




########################################################################################################
#增删改查之后进去每个都可以对员工信息 商品信息 安全信息 仓库信息 供货信息 退货信息 会员信息等等进行操作
def all_add():
    #window.destroy()
    global window_choice
    window_choice = tk.Tk()
    window_choice.title("无人销售管理系统")
    window_choice.geometry('500x500')

    # 加载背景图片并转换为Tkinter能使用的格式
    background_image = Image.open("background.jpg")
    background_image = background_image.resize((500, 500), Image.ANTIALIAS)
    background_image_tk = ImageTk.PhotoImage(background_image)

    # 创建一个Canvas，用于显示背景图片
    canvas = tk.Canvas(window_choice, width=4500, height=500)
    canvas.pack(fill="both")

    # 在Canvas上添加背景图片
    canvas.create_image(0, 0, image=background_image_tk, anchor="nw")

    # 添加标题标签
    canvas.create_text(250, 50, text="欢迎使用无人销售管理系统", font=("黑体", 20), fill="black")

    # 创建并添加按钮
    button1 = tk.Button(window_choice, text="添加员工信息", command=Staff_add)
    button2 = tk.Button(window_choice, text="添加商品信息", command=Goods_add)
    button3 = tk.Button(window_choice, text="添加安全信息", command=Check1_add)
    button4 = tk.Button(window_choice, text="添加仓库信息", command=Ware_add)
    button5 = tk.Button(window_choice, text="添加供货商信息", command=Vendor_add)
    button6 = tk.Button(window_choice, text="添加退货信息", command=Infer_add)
    button7 = tk.Button(window_choice, text="添加会员信息", command=Member_add)
    button8 = tk.Button(window_choice, text="添加交易信息", command=Trade_add)
    button9 = tk.Button(window_choice, text="添加入库信息", command=Entry_add)
    button10 = tk.Button(window_choice, text="添加出库信息", command=Exits_add)
    button_return = tk.Button(window_choice, text="返回", command=change_main)

    # 在Canvas上添加按钮
    canvas.create_window(0, 120, anchor="nw", window=button1)
    canvas.create_window(100, 120, anchor="nw", window=button2)
    canvas.create_window(200, 120, anchor="nw", window=button3)
    canvas.create_window(300, 120, anchor="nw", window=button4)
    canvas.create_window(400, 120, anchor="nw", window=button5)
    canvas.create_window(0, 200, anchor="nw", window=button6)
    canvas.create_window(100, 200, anchor="nw", window=button7)
    canvas.create_window(200, 200, anchor="nw", window=button8)
    canvas.create_window(300, 200, anchor="nw", window=button9)
    canvas.create_window(400, 200, anchor="nw", window=button10)
    canvas.create_window(250, 350, anchor="center", window=button_return)

    window_choice.mainloop()

def all_delete():
    #window.destroy()
    global window_choice
    window_choice = tk.Tk()
    window_choice.title("无人销售管理系统")
    window_choice.geometry('500x500')

    # 加载背景图片并转换为Tkinter能使用的格式
    background_image = Image.open("background.jpg")
    background_image = background_image.resize((500, 500), Image.ANTIALIAS)
    background_image_tk = ImageTk.PhotoImage(background_image)

    # 创建一个Canvas，用于显示背景图片
    canvas = tk.Canvas(window_choice, width=4500, height=500)
    canvas.pack(fill="both")

    # 在Canvas上添加背景图片
    canvas.create_image(0, 0, image=background_image_tk, anchor="nw")

    # 添加标题标签
    canvas.create_text(250, 50, text="欢迎使用无人销售管理系统", font=("黑体", 20), fill="black")


    # 创建并添加按钮
    button1 = tk.Button(window_choice, text="删除员工信息", command=Staff_delete)
    button2 = tk.Button(window_choice, text="删除商品信息", command=Goods_delete)
    button3 = tk.Button(window_choice, text="删除安全信息", command=Check1_delete)
    button4 = tk.Button(window_choice, text="删除仓库信息", command=Ware_delete)
    button5 = tk.Button(window_choice, text="删除供货商信息", command=Vendor_delete)
    button6 = tk.Button(window_choice, text="删除退货信息", command=Infer_delete)
    button7 = tk.Button(window_choice, text="删除会员信息", command=Member_delete)
    button8 = tk.Button(window_choice, text="删除交易信息", command=Trade_delete)
    button9 = tk.Button(window_choice, text="删除入库信息", command=Entry_delete)
    button10 = tk.Button(window_choice, text="删除出库信息", command=Exits_delete)
    button_return = tk.Button(window_choice, text="返回", command=change_main)

    # 在Canvas上添加按钮
    canvas.create_window(0, 120, anchor="nw", window=button1)
    canvas.create_window(100, 120, anchor="nw", window=button2)
    canvas.create_window(200, 120, anchor="nw", window=button3)
    canvas.create_window(300, 120, anchor="nw", window=button4)
    canvas.create_window(400, 120, anchor="nw", window=button5)
    canvas.create_window(0, 200, anchor="nw", window=button6)
    canvas.create_window(100, 200, anchor="nw", window=button7)
    canvas.create_window(200, 200, anchor="nw", window=button8)
    canvas.create_window(300, 200, anchor="nw", window=button9)
    canvas.create_window(400, 200, anchor="nw", window=button10)
    canvas.create_window(250, 350, anchor="center", window=button_return)

    window_choice.mainloop()
def all_update():
    #window.destroy()
    global window_choice
    window_choice = tk.Tk()
    window_choice.title("无人销售管理系统")
    window_choice.geometry('500x500')

    # 加载背景图片并转换为Tkinter能使用的格式
    background_image = Image.open("background.jpg")
    background_image = background_image.resize((500, 500), Image.ANTIALIAS)
    background_image_tk = ImageTk.PhotoImage(background_image)

    # 创建一个Canvas，用于显示背景图片
    canvas = tk.Canvas(window_choice, width=4500, height=500)
    canvas.pack(fill="both")

    # 在Canvas上添加背景图片
    canvas.create_image(0, 0, image=background_image_tk, anchor="nw")

    # 添加标题标签
    canvas.create_text(250, 50, text="欢迎使用无人销售管理系统", font=("黑体", 20), fill="black")

    # 创建并添加按钮
    button1 = tk.Button(window_choice, text="更新员工信息", command=Staff_update)
    button2 = tk.Button(window_choice, text="更新商品信息", command=Goods_update)
    #button3 = tk.Button(window_choice, text="删除安全信息", command=Check1_delete)
    button4 = tk.Button(window_choice, text="更新仓库信息", command=Ware_update)
    button5 = tk.Button(window_choice, text="更新供货商信息", command=Vendor_update)
    button6 = tk.Button(window_choice, text="更新退货信息", command=Infer_update)
    button7 = tk.Button(window_choice, text="更新会员信息", command=Member_update)
    button8 = tk.Button(window_choice, text="更新交易信息", command=Trade_update)
    button9 = tk.Button(window_choice, text="更新入库信息", command=Entry_update)
    button10 = tk.Button(window_choice, text="更新出库信息", command=Exits_update)
    button_return = tk.Button(window_choice, text="返回", command=change_main)

    # 在Canvas上添加按钮
    canvas.create_window(0, 120, anchor="nw", window=button1)
    canvas.create_window(100, 120, anchor="nw", window=button2)
    #canvas.create_window(200, 120, anchor="nw", window=button3)
    canvas.create_window(200, 120, anchor="nw", window=button4)
    canvas.create_window(300, 120, anchor="nw", window=button5)
    canvas.create_window(410, 120, anchor="nw", window=button6)
    canvas.create_window(0, 200, anchor="nw", window=button7)
    canvas.create_window(125, 200, anchor="nw", window=button8)
    canvas.create_window(250, 200, anchor="nw", window=button9)
    canvas.create_window(375, 200, anchor="nw", window=button10)
    canvas.create_window(250, 350, anchor="center", window=button_return)


    window_choice.mainloop()
def all_select():
    #window.destroy()
    global window_choice
    window_choice = tk.Tk()
    window_choice.title("无人销售管理系统")
    window_choice.geometry('500x500')

    # 加载背景图片并转换为Tkinter能使用的格式
    background_image = Image.open("background.jpg")
    background_image = background_image.resize((500, 500), Image.ANTIALIAS)
    background_image_tk = ImageTk.PhotoImage(background_image)

    # 创建一个Canvas，用于显示背景图片
    canvas = tk.Canvas(window_choice, width=4500, height=500)
    canvas.pack(fill="both")

    # 在Canvas上添加背景图片
    canvas.create_image(0, 0, image=background_image_tk, anchor="nw")

    # 添加标题标签
    canvas.create_text(250, 50, text="欢迎使用无人销售管理系统", font=("黑体", 20), fill="black")

    # 创建并添加按钮
    button1 = tk.Button(window_choice, text="查询员工信息", command=Staff_select)
    button2 = tk.Button(window_choice, text="查询商品信息", command=Goods_select)
    button3 = tk.Button(window_choice, text="查询安全信息", command=Check1_select)
    button4 = tk.Button(window_choice, text="查询仓库信息", command=Ware_select)
    button5 = tk.Button(window_choice, text="查询供货商信息", command=Vendor_select)
    button6 = tk.Button(window_choice, text="查询退货信息", command=Infer_select)
    button7 = tk.Button(window_choice, text="查询会员信息", command=Member_select)
    button8 = tk.Button(window_choice, text="查询交易信息", command=Trade_select)
    button9 = tk.Button(window_choice, text="查询入库信息", command=Entry_select)
    button10 = tk.Button(window_choice, text="查询出库信息", command=Exits_select)
    button_return = tk.Button(window_choice, text="返回", command=change_main)

    # 在Canvas上添加按钮
    canvas.create_window(0, 120, anchor="nw", window=button1)
    canvas.create_window(100, 120, anchor="nw", window=button2)
    canvas.create_window(200, 120, anchor="nw", window=button3)
    canvas.create_window(300, 120, anchor="nw", window=button4)
    canvas.create_window(400, 120, anchor="nw", window=button5)
    canvas.create_window(0, 200, anchor="nw", window=button6)
    canvas.create_window(100, 200, anchor="nw", window=button7)
    canvas.create_window(200, 200, anchor="nw", window=button8)
    canvas.create_window(300, 200, anchor="nw", window=button9)
    canvas.create_window(400, 200, anchor="nw", window=button10)
    canvas.create_window(250, 350, anchor="center", window=button_return)

    window_choice.mainloop()

####################################################################################################

#添加商品界面跳转
def change_add():
    window_function.destroy()
    all_add()
def change1_add():
    window.destroy()
    all_add()
#删除商品界面跳转
def change_delete():
    window_function.destroy()
    all_delete()
def change1_delete():
    window.destroy()
    all_delete()
#更新商品界面跳转
def change_update():
    window_function.destroy()
    all_update()
def change1_update():
    window.destroy()
    all_update()
#条件查询商品界面跳转
def change_select():
    window_function.destroy()
    all_select()
def change1_select():
    window.destroy()
    all_select()
#主界面跳转
def change_main():
    window_choice.destroy()
    mainpage()
def change_login():
    login1.destroy()
    mainpage()

###################################################################################################
#主界面
def mainpage():
    global window
    window = tk.Tk()
    window.title("无人销售管理系统")

    # 添加标题标签
    tk.Label(window, text="欢迎使用无人销售管理系统", font=("黑体", 20)).pack(side=tk.TOP, pady=(10, 2))

    # 创建一个frame来放置按钮
    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.TOP, fill=tk.X, expand=False)  # 按钮放在标题下方，横向填充

    # 在frame中添加按钮，横向排列
    tk.Button(button_frame, text="添加信息", command=change1_add).pack(side=tk.LEFT, padx=15)
    tk.Button(button_frame, text="删除信息", command=change1_delete).pack(side=tk.LEFT, padx=15)
    tk.Button(button_frame, text="修改信息", command=change1_update).pack(side=tk.LEFT, padx=15)
    tk.Button(button_frame, text="信息查询", command=change1_select).pack(side=tk.LEFT, padx=15)

    # 插入图片背景
    image = Image.open("background.jpg").resize((300, 300))  # 调整图片大小以适应窗口
    pyt = ImageTk.PhotoImage(image)
    canvas_window = tk.Canvas(window, width=300, height=300)  # 画布大小与图片一致
    canvas_window.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # 放在按钮下方，填充剩余空间
    canvas_window.create_image(180, 150, image=pyt)  # 创建画布上的图片，位置根据图片大小调整

    window.mainloop()
####################################################################################
#登录界面
def login():
    global login1,username,password
    login1=tk.Tk()
    login1.title("登录界面")
    login1.geometry('300x200')
    tk.Label(login1, text="请输入账号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(login1, text="请输入密码：").grid(row=2, column=0, padx=20, pady=20)

    # 定义变量记录输入信息
    username = tk.StringVar()
    password = tk.StringVar()
    # 生成输入框
    entry1 = tk.Entry(login1, show=None, textvariable=username).grid(row=1, column=1)
    entry2 = tk.Entry(login1, show='*', textvariable=password).grid(row=2, column=1)

    # 生成按钮

    button = tk.Button(login1, text="login", command=login_l).place(relx=0.3, rely=0.8)
   # else:
      #  tkinter.messagebox.showinfo(title='提示', message='账号或密码错误')
    login1.mainloop()

def login_l():
    name=username.get()
    pwd=password.get()
    if name=='1' and pwd =='1':
        change_login()
    else:
        tkinter.messagebox.showinfo(title='提示', message='账号或密码错误')
#调用登录界面
if __name__ == '__main__':
    login()
