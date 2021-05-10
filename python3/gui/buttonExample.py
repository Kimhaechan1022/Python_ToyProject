from tkinter import *  #GUI 프로그래밍을 위한 패키지

root = Tk()    
root.title("button window") 


root.geometry("300x200+100+100")
root.resizable(True, False)


cnt = 0

def cntP():
    global cnt
    cnt+=1
    lbl2.config(text=str(cnt))
def cntM():
    global cnt
    cnt-=1
    lbl2.config(text=str(cnt))


lbl = Label(root, text="버튼 커맨드 예제") #label
lbl.pack() #컴포넌트 부착

lbl2 = Label(root, text="0")   #버튼 커맨드 확인을 위한 라벨
lbl2.pack()

btn = Button(root,text="plus",command = cntP) #button
btn.pack()

btn2 = Button(root,text="minus",command = cntM) #button
btn2.pack()

root.mainloop()
