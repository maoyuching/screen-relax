# -*-coding:utf-8-*-
import tkinter
import time
# import tkMessageBox
# import sys
# import BeBigModule

class MainFrame:
    def __init__(self):
        self.frame = tkinter.Frame()  # frame 是一个gui容器
        self.frame.pack()

        contentsWork = tkinter.StringVar()
        contentsRelax = tkinter.StringVar()

        self.entryWorkWidget = tkinter.Entry(self.frame, text=contentsWork)
        contentsWork.set('input workTime here:')
        self.entryWorkWidget["width"] = 35  # 这句话和下句话的先后顺序不会影响程序
        self.entryWorkWidget.pack(side='top')

        self.entryRelaxWidget = tkinter.Entry(self.frame, text=contentsRelax)
        contentsRelax.set('input relaxTime here:')
        self.entryRelaxWidget.config(width=35)
        self.entryRelaxWidget.pack(side='top')

        self.startButton = tkinter.Button(self.frame, text="OK", command=self.start)
        self.startButton.pack(side='left')

        self.quitButton = tkinter.Button(self.frame, text="Exit", command=self.quit)
        self.quitButton.pack(side='right')
        self.frame.mainloop()

    def start(self):
        workTime = self.entryWorkWidget.get().strip()
        workTimeNum = int(workTime.split(":")[1])
        #         self.frame.deiconify()
        #         self.frame.withdraw
        relaxTime = self.entryRelaxWidget.get().strip()
        relaxTimeNum = int(relaxTime.split(":")[1])

        self.frame.destroy()
        beBigFrame = BeBig(workTimeNum, relaxTimeNum)

    def quit(self):
        pass

class BeBig():
    workTime = 0
    relaxTime = 0
    root = tkinter.Tk()
    Label1 = tkinter.Label(root, text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    def __init__(self, workTimeNum, relaxTimeNum):
        self.workTime = workTimeNum
        self.relaxTime = relaxTimeNum

        # 设置最小的尺寸为全屏
        self.root.minsize(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        # self.root.geometry('300x200-100-100')
        self.root.config(bg='green')

        self.Label1.pack(side='top')
        topTitle = self.root.winfo_tplevel()
        topTitle.overrideredirect(True)
        self.trickit(self.relaxTime, self.workTime)
        self.root.mainloop()

    def trickit(self, relaxTime, workTime):
        for j in range(relaxTime, 0, -1):
            self.Label1["text"] = j
            self.root.update()
            time.sleep(1)

        self.root.withdraw()
        time.sleep(workTime)
        self.root.minsize(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.root.update()
        self.root.deiconify()  # 删掉图标
        self.trickit(self.relaxTime, self.workTime)

root=tkinter.Tk()
root.title("CountDowm")

mainFrame=MainFrame()
root.mainloop()
# mainFrame = MainFrame()
# 目前来看就剩个问题了，怎么设定窗口的显示位置
