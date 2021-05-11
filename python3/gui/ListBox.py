from tkinter import * 

def add_list():
    listbox.insert(END, ent.get())
    ent.delete(0,END)
def del_list():
    listbox.delete(END)

root = Tk()    
root.title("List Example") 
root.geometry("250x300+100+100")
root.resizable(True, False)

frm = Frame(root)
frm.pack(pady=10)

lbl = Label(frm, text = "This is simple list Example")
lbl.pack()


#list box create
listbox = Listbox(frm,width = 25,height = 5,bg="#ffdab9",fg="#003f3f")
listbox.pack(side = LEFT,fill = BOTH)

#scroolbar create
scrBar = Scrollbar(frm)
scrBar.pack(side = RIGHT, fill=BOTH)

#리스트 박스에서 마우스휠을 돌릴때 스크롤바 따라옴
listbox.config(yscrollcommand=scrBar.set)
#스크롤바를 사용해서 리스트 박스 조종
scrBar.config(command=listbox.yview)




ent =Entry(width=30)
ent.pack()

btn1 = Button(text ="add", command = add_list)
btn1.pack(side = LEFT)

btn2 = Button(text ="del", command = del_list)
btn2.pack(side = LEFT)

root.mainloop()
