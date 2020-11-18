import time
import threading
from tkinter import *


class EyeRelax:
    """主要类"""
    log_line = "========================"

    def __init__(self):
        self.root = Tk()
        self.lb_wkt = Label(master=self.root)
        self.lb_rlt = Label(master=self.root)
        self.ety_wkt = Entry(master=self.root)
        self.ety_rlt = Entry(master=self.root)
        self.btn_wkt = Button(master=self.root)
        self.btn_rlt = Button(master=self.root)

        self.work_time = 10
        self.relax_time = 10

    def set_root(self):
        self.root.title("eye care")
        self.root.wm_geometry("300x300")

    def quit(self):
        """关闭程序"""
        self.root.quit()
        self.root.destroy()

    def show(self):
        """展示护眼屏幕"""

        # 拾取输入框的数字
        self.work_time = int(self.ety_wkt.get() if self.ety_wkt.get() != '' else 10)
        self.relax_time = int(self.ety_rlt.get() if self.ety_rlt.get() != '' else 10)

        while True:
            new_window = Toplevel(self.root, bg="green")  # toplevel 是一个弹出框组件
            new_window.overrideredirect(True)  # 无边框
            new_window.geometry("1920x1080")

            # 设置 护眼 屏保 文字
            lb_hint = Label(new_window, text="relaxing.....", bg="green")
            lb_hint.pack()

            self.root.focus_force()  # 强制获得焦点
            new_window.bind("<FocusOut>", new_window.focus_force())
            new_window.update()  # update方法和 withdraw 相反，将隐藏的窗口展现出来
            for j in range(self.relax_time, 0, -1):  # 开始休息指定的秒数
                new_window.focus_force()  # 用来给组件获取焦点
                lb_hint["text"] = j
                self.root.update()
                time.sleep(1)

            # 隐藏屏保，蛰伏指定的秒数，然后重又出现
            new_window.withdraw()  # withdraw 意思是隐藏
            print(self.log_line + "蛰伏")
            time.sleep(self.work_time)
            print(self.log_line + "回复")

    def show_threading(self):
        print(self.log_line + "启动线程")
        t = threading.Thread(target=self.show, name="thread_show")
        t.setDaemon(True)
        t.start()

    def start(self):
        """启动程序"""
        print(self.log_line + "start")
        self.set_root()

        self.lb_wkt.configure(text="工作时间")
        self.lb_wkt.pack()
        self.ety_wkt.pack()

        self.lb_rlt.configure(text="休息时间")
        self.lb_rlt.pack()
        self.ety_rlt.pack()

        self.btn_wkt.configure(text="OK", command=self.show_threading)
        self.btn_wkt.pack()
        self.btn_rlt.configure(text="quit", command=self.quit)
        self.btn_rlt.pack()

        self.root.mainloop()


if __name__ == "__main__":
    EyeRelax().start()
