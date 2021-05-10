from tkinter import *  #GUI 프로그래밍을 위한 패키지

root = Tk()    #객체 생성

root.title("example window")  #창의 이름 설정


root.geometry("300x200+100+100")  # x는 문자'x'
# 가로 사이즈 x 세로 사이즈 + 창을 띄울 화면의 x 좌표 + y 좌표
root.resizable(True, False) # 창의 사이즈를 조절할수있을지 여부



lbl = Label(root, text="예제 라벨") #label
lbl.pack() #컴포넌트 부착

btn = Button(root,text="exit") #button
btn.pack()

root.mainloop()
