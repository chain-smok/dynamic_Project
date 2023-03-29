import sqlite3
conn=sqlite3.connect("wei.db")
c=conn.cursor()
c.execute('''create table member(full_name char(50),
                                 nationality char(50),
                                 born datetime,
                                 picture char(255),
                                 phone char(255),
                                 pet char(255));''')
c.execute("insert into member(full_name,nationality,born,picture,phone,pet) values('沈暐勛','Taiwan','2002-07-20','me.png','Samsung','mimi')")
result=c.execute("select * from member")
for row in result:
    print("{},{},{},{},{},{}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
conn.commit()