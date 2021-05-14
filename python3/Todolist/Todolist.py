#today plan : do, font change


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


def cross_off():

    conn = pymysql.connect(host='localhost', user='root', password='1234',db='TodoDB',charset='utf8')
    cursor = conn.cursor()
    
    listbox.itemconfig(
            listbox.curselection(),
            fg="#fff",
            )

    index = listbox.curselection()[0]+1
    
    
    cursor.execute("UPDATE dataTBL SET Do = 1 WHERE ID = {0}".format(index))

    
    conn.commit()
    conn.close()



def cross_on():
    
    conn = pymysql.connect(host='localhost', user='root', password='1234',db='TodoDB',charset='utf8')
    cursor = conn.cursor()

    listbox.itemconfig(
            listbox.curselection(),
            fg="#003300",
            )
    
    index = listbox.curselection()[0]+1


    cursor.execute("UPDATE dataTBL SET Do = 0 WHERE ID = {0}".format(index))


    conn.commit()
    conn.close()


root= Tk()    
root.title("Todolist") 
root.geometry("250x300+100+100")
root.resizable(True, False)

box_frame = Frame(root)
box_frame.pack(pady=10)

label = Label(box_frame, text = "DB : TodoDB, TABLE : dataTBL")
label.pack()


#create list box 
listbox = Listbox(box_frame,width = 25,height = 5,bg="#ffdab9",fg="#003300")
listbox.pack(side = LEFT,fill = BOTH)

fetch()


#scroolbar create
scrBar = Scrollbar(box_frame)
scrBar.pack(side = RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrBar.set)
scrBar.config(command=listbox.yview)




ent =Entry(width=26)
ent.pack()




ins_btn = Button(text ="ins", command = insert)
ins_btn.pack()
ins_btn.place(x=20,y=200)


del_btn = Button(text ="del", command = delete)
del_btn.pack()
del_btn.place(x=70,y=200)

did_btn = Button(text= "did", command = cross_off)
did_btn.pack
did_btn.place(x=120,y=200)

yet_btn = Button(text= "yet", command = cross_on)
yet_btn.pack
yet_btn.place(x=170,y=200)


root.mainloop()




