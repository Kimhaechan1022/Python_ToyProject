import pymysql       #pymysql 라이브러리

#connection 생성, pymysql.connect()함수 사용, 인자는 아래와 같음
conn = pymysql.connect(host='localhost', user='root', password='1234',db='karaokeDB',charset='utf8')

#커서 객체 선언
cursor = conn.cursor()

#쿼리문을 스트링으로 선언
sql = "SELECT * FROM songInfoTBL"

#스트링형식 쿼리 실행
cursor.execute(sql)

#모든 정보 fetch(물어옴)
res = cursor.fetchall()

#반복문을 통한 테이블 내의 정보 출력
for data in res:
    print(data)

conn.commit()
conn.close()
