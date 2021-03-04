from cx_Oracle import *
'''
con=connect("system/bigil@localhost")
cur=con.cursor()
#cur.execute("create table student(sid number(10),sname varchar2(16),scourse varchar2(5),sage number(2))")
while True:
    sid=int(input("enter the studen id no:"))
    name=input("enter the student name:")
    course=input("enter the course name:")
    age=int(input("enter the student age:"))
    cur.execute(f"insert into student values({sid},'{name}','{course}',{age})")
    con.commit()
    print("thankk you!!!!!!!")
    opt=input("do you want to add one more row into the student table")
    if opt.lower()=="no":
        break
con.commit()
cur.close()
con.close()
'''
class data:
    ob=1
    def __init__(self):
        self.con=connect("system/bigil@localhost")
        self.cur=self.con.cursor()
    def create(self):
        self.cur.execute("create table emp(eid number(10),ename varchar2(18),eadd varchar2(33),esal number(7))")
        data.ob=0
        return data.ob
    def insert(self):
        while True:
            eid=int(input("enter the employee id"))
            ename=input("enter the employee name:")
            eadd=input("enter the employee address:")
            esal=int(input("enter the employee salary:"))
            self.cur.execute(f"insert into emp values({eid},'{ename}','{eadd}',{esal})")
            self.con.commit()
            op=input("do you want to insert one mor value (y/n)")
            if op.lower()=="n":
                break
    def fech(self):
        self.cur.execute("select * from emp where esal<22000")
        data=self.cur.fetchmany()
        print(data)
        self.cur.close()
        self.con.close()
p=data()
#p.create()
#p.insert()
p.fech()
