import pymysql       #pymysql 라이브러리

conn = pymysql.connect(host='localhost', user='root', password='1234',db='TodoDB',charset='utf8')

cursor = conn.cursor()

#조회
def select():
    print("( ID | contents | Did or yet )")
    cursor.execute("SELECT * FROM dataTBL")
    res = cursor.fetchall()
    for data in res:
         print(data)

#투두 아이템 삽입
def insert(index,contents,do):
    cursor.execute("INSERT INTO dataTBL VALUES ({0},%s,{1})".format(index,do),contents)

#아이템 삭제
def delect(index):
    cursor.execute("DELETE FROM dataTBL WHERE ID = {0}".format(index))

#이행한 상태 변화
def status_change(index,boolean):
    cursor.execute("UPDATE dataTBL SET Do = {0} WHERE ID = {1}".format(boolean,index))

case = 0
print("\n\n****** This is simple Todo List Text Application ******\n\n")
while case !=5:    
    print("<1> SELECT      <2> INSERT(index,contents,do)      <3> DELETE(index)\n<4> status_change( index, status(0-yet , 1-did))      <5> EXIT\n")
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
        ch_index = input("index :")
        ch_bool = input("0 or 1 :")
        status_change(ch_index,ch_bool)
    elif case == 5:
        print("BYE")
    else:
        print("Error")



conn.commit()
conn.close()
