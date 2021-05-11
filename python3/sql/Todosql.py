import pymysql       #pymysql 라이브러리

conn = pymysql.connect(host='localhost', user='root', password='1234',db='TodoDB',charset='utf8')

cursor = conn.cursor()

#select

def select():
    cursor.execute("SELECT * FROM dataTBL")
    res = cursor.fetchall()
    for data in res:
         print(data)

def insert(index,contents,do):
    cursor.execute("INSERT INTO dataTBL VALUES ({0},%s,{1})".format(index,do),contents)

def delect(index):
    cursor.execute("DELETE FROM dataTBL WHERE ID = {0}".format(index))


case = 0

while case !=4:    
    print("<1> SELECT , <2> INSERT(index,contents,do) , <3> DELETE(index), <4> EXIT")
    case = int(input("input :"))
    if case==1:
        select()
    elif case == 2:
        se_index = input("index :")
        se_con = input("contents :")
        insert(se_index,str(se_con),0)
    elif case == 3:
        de_index = input("index :")
        delect(de_index)
    elif case == 4:
        print("BYE")
    else:
        print("Error")



conn.commit()
conn.close()
