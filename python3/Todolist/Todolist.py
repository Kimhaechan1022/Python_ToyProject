from tkinter import * 
import pymysql


def fetch():
    conn = pymysql.connect(host='localhost', user='root', password='1234',db='TodoDB',charset='utf8')
    cursor = conn.cursor()

    cursor.execute("SELECT Contents FROM dataTBL")
    DB_data = cursor.fetchall()
    for item in DB_data:
        listbox.insert(END,item)
    conn.commit()
    conn.close()


def insert():

    conn = pymysql.connect(host='localhost', user='root', password='1234',db='TodoDB',charset='utf8')
    cursor = conn.cursor()
    
    
    cursor.execute("INSERT INTO dataTBL VALUES ({0} ,%s, 0)".format(listbox.index(END)+1),str(ent.get()))
    ent.delete(0,END)
  
    cursor.execute("SELECT Contents FROM dataTBL")
    DB_data = cursor.fetchall()
    listbox.insert(END,DB_data[-1]) #인덱스 끝에서부터 접근은 음수

    conn.commit()
    conn.close()


def delete():

    conn = pymysql.connect(host='localhost', user='root', password='1234',db='TodoDB',charset='utf8')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM dataTBL WHERE ID = {0}".format(listbox.index(END)))

    listbox.delete(END)

    conn.commit()
    conn.close()

root = Tk()    
root.title("List Example") 
root.geometry("250x300+100+100")
root.resizable(True, False)

box_frame = Frame(root)
box_frame.pack(pady=10)

label = Label(box_frame, text = "This is simple list Example")
label.pack()


#create list box 
listbox = Listbox(box_frame,width = 25,height = 5,bg="#ffdab9",fg="#003f3f")
listbox.pack(side = LEFT,fill = BOTH)

fetch()


#scroolbar create
scrBar = Scrollbar(box_frame)
scrBar.pack(side = RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrBar.set)
scrBar.config(command=listbox.yview)




ent =Entry(width=26)
ent.pack()




ins_btn = Button(text ="insert", command = insert)
ins_btn.pack()
ins_btn.place(x=80,y=200)


del_btn = Button(text ="delete", command = delete)
del_btn.pack()
del_btn.place(x=150,y=200)


root.mainloop()






