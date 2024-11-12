import pymysql


#数据库初始化
#创建表
connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
if connect:
    print("连接成功!")

cursor = connect.cursor()   # 创建一个游标对象,python里的sql语句都要通过cursor来执行
#创建表及其约束
cursor.execute("create table Staff(Snum  varchar(10) primary key,Sname varchar(20) not null,Ssex varchar(5) check(Ssex in('男','女')),Sage int not null check(Sage>=18),Sseniority int not null check(Sseniority>=0),Sphone varchar(20) not null,Sid varchar(25) not null,Ssalary int check(Ssalary>=0),Syard varchar(20) check(Syard in('红码','黄码','绿码')) )")
cursor.execute("create table Vendor(Vnum varchar(10) primary key,Vname varchar(10) not null,Vphone varchar(20) not null,Vpalce varchar(10) not null)")
#  on delete cascade
cursor.execute("create table Goods(Gnum varchar(10) primary key,Gname varchar(10) not null,Gtype varchar(10) not null,Gprice int check(Gprice>=0),Gbid int check(Gbid>=0),Gstock int check(Gstock>=0),Galarm int check(Galarm>=0), Gplan int check(Gplan>=0),Vnum varchar(10) not null)")
cursor.execute("create table Member(Mnum varchar(10) primary key,Mname varchar(10) not null,Mphone varchar(20) not null,Mdate datetime,Mtotal int check(Mtotal>=0),Mbalance int check(Mbalance>=0),Mpassword varchar(25) not null)")
# on delete set null
cursor.execute("create table Ware(Wnum varchar(10) primary key,Wname varchar(10) not null,Wplace varchar(10) not null,Snum varchar(10) not null)")
cursor.execute("create table Trade(Tnum varchar(10) primary key,Tdate datetime  not null,Snum varchar(10) not null,Gnum varchar(10) not null,Tamount int check(Tamount>=0),Tmoney int check(Tmoney>=0),Mnum varchar(10) not null)")
cursor.execute("create table Infer(Tnum varchar(10) not null,Gnum varchar(10) not null,Iamount int check(Iamount>=0),Imoney int check(Imoney>=0),Idate datetime not null)")
# on delete cascade
cursor.execute("create table Entry(Enum varchar(10) primary key,Gnum varchar(10) not null,Eamount int check(Eamount>=0),Emoney int check(Emoney>=0),Vnum varchar(10) not null,Edate datetime not null,Snum varchar(10) not null)")
cursor.execute("create table Exits(Xnum varchar(10) primary key,Gnum varchar(10) not null,Xamount int check(Xamount>=0),Xmoney int check(Xmoney>=0),Xdate datetime not null,Snum varchar(10) not null)")
cursor.execute("create table Check1(Cdate date primary key,Cyard varchar(10) check(Cyard in('红码','黄码','绿码')),Cfire varchar(10) check(Cfire in('是','否')),Cspary varchar(10) check(Cspary in('是','否')))")
connect.commit()  #提交
cursor.close()  # 关闭游标
connect.close()

#初始化数据（两条数据或一条数据，为了后续增加约束）
connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
cursor.execute("insert into Goods values ('200001','薯片','零食',8,5,500,100,600,'100002')")
cursor.execute("insert into Goods values ('200002','可乐','饮料',3,2,1000,100,1200,'100001')")
cursor.execute("insert into Vendor values ('100001','可口','123456','杭州')")
cursor.execute("insert into Vendor values ('100002','乐事','135790','西安')")
cursor.execute("insert into Staff values ('0001','张三','男',30,5,'139820117','411481320301',5000,'绿码')")
cursor.execute("insert into Staff values ('0002','熊大','女',32,3,'178883132','411481310302',3000,'绿码')")
cursor.execute("insert into Member values ('300001','迪迦','179320118',20220830194422,1050,300,'321336')")
cursor.execute("insert into Ware values('400001','一号','上海','0001')")
cursor.execute("insert into Check1 values(20220620,'绿码','是','是')")


connect.commit()  # 提交
cursor.close()
connect.close()

#创建触发器 满足顾客买商品的一个场景
connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
# 创建光标
cursor = connect.cursor()
#购买的商品数量要在库存里减去
cursor.execute("create trigger update_Goods before insert on Trade for each row update Goods set Gstock=Gstock-new.Tamount where Gnum=new.Gnum;")
#要在会员卡的总消费和余额里改变相应的数值
cursor.execute("create trigger update_Member before insert on Trade for each row update Member set Mtotal=Mtotal+new.Tmoney,Mbalance=Mbalance-new.Tmoney where Mnum=new.Mnum;")
connect.commit()
cursor.close()
connect.close()

connect = pymysql.connect(host="localhost", user="root",password="mysql", database="sqlwork")  # 建立连接
cursor = connect.cursor()

cursor.execute("alter table Goods add foreign key(Vnum) references Vendor(Vnum) on delete cascade")
cursor.execute("alter table Ware add foreign key(Snum) references Staff(Snum)")
cursor.execute("alter table Trade add foreign key(Snum) references Staff(Snum)")
cursor.execute("alter table Trade add foreign key(Gnum) references Goods(Gnum)")
cursor.execute("alter table Trade add foreign key(Mnum) references Member(Mnum)")
cursor.execute("alter table Infer add foreign key(Tnum) references Trade(Tnum)")
cursor.execute("alter table Infer add foreign key(Gnum) references Goods(Gnum)")
cursor.execute("alter table Entry add foreign key(Snum) references Staff(Snum)")
cursor.execute("alter table Entry add foreign key(Gnum) references Goods(Gnum)")
cursor.execute("alter table Entry add foreign key(Vnum) references Vendor(Vnum)")
cursor.execute("alter table Exits add foreign key(Snum) references Staff(Snum)")
cursor.execute("alter table Exits add foreign key(Gnum) references Goods(Gnum)")

connect.commit()
# 关闭数据库连接，防止泄露
connect.close()
