from tkinter import *  #GUI 프로그래밍을 위한 패키지

def add_str():
    lbl2.config(text = ent.get())

root = Tk()    
root.title("Entry & Button Example") 
root.geometry("300x200+100+100")
root.resizable(True, False)

lbl1 = Label(root, text = "Make any text and push add button")
lbl1.pack()

lbl2 = Label(root, text="NULL")   #버튼 커맨드 확인을 위한 라벨
lbl2.pack()

#entry 생성
ent = Entry(root,width=30)
ent.pack()

btn = Button(text="add",command=add_str)
btn.pack()

root.mainloop()
