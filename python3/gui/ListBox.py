from tkinter import * 


root = Tk()    
root.title("List Example") 
root.geometry("250x300+100+100")
root.resizable(True, False)

lbl = Label(root, text = "This is simple list Example")
lbl.pack()


#list box create
listbox = Listbox(width = 25,height = 5,bg="#ffdab9",fg="#003f3f")
listbox.pack(side = LEFT,fill = BOTH)

#scroolbar create
scrBar = Scrollbar(root)
scrBar.pack(side = LEFT, fill=BOTH)

#리스트 박스에서 마우스휠을 돌릴때 스크롤바 따라옴
listbox.config(yscrollcommand=scrBar.set)
#스크롤바를 사용해서 리스트 박스 조종
scrBar.config(command=listbox.yview)


#test list 
test = ["sgge","14ssf3","qqrs","asdasd","asd","ss","s","a","Hello world","I am list","fuck up","born hair","song by ph1"]

#insert into listbox, 테스트 리스트를 리스트박스 안으로  넣음
for item in test:
    listbox.insert(END,item)



root.mainloop()
