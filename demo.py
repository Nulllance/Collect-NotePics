import tkinter as tk
from PIL import Image, ImageTk
import cv2
import threading


class basebesk():
    def __init__(self, master):
        self.win = master
        self.win.config()
        self.win.title("收集握手姿势")
        self.win.geometry('1200x800')
        initface(self.win)


class initface():
    def __init__(self, master):
        # -------------顶部文本介绍-------------
        introduction = "你好,这是一个手握笔姿势图片的收集小程序,可以用来收集握笔的9种姿势,分别标号为1~9,"
        global male, age, select
        self.win = master
        self.win.config(bg='white')
        self.initface = tk.Frame(self.win, )
        self.initface.pack()
        text = tk.Text(win, width=20, height=5)
        text.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        text.insert("insert", introduction)
        text.window_create("insert")

        # -------------中间的性别,年龄,拍摄角度的选择-------------
        lb_tip = tk.Label(win, text='请先输入年龄')
        lb_tip.place(relx=0.45, rely=0.15, relwidth=0.1, relheight=0.05)
        lb_age = tk.Label(win, text='age: ')
        lb_age.place(relx=0.45, rely=0.25, relwidth=0.05, relheight=0.05)
        age = tk.Entry(win, show=None)
        age.place(relx=0.50, rely=0.25, relwidth=0.05, relheight=0.05)

        button_male0 = tk.Button(win, command=male0, text="女生", width=20, height=2)
        button_male0.place(relx=0.45, rely=0.2, relwidth=0.05, relheight=0.05)
        button_male1 = tk.Button(win, command=male1, text="男生", width=20, height=2)
        button_male1.place(relx=0.50, rely=0.2, relwidth=0.05, relheight=0.05)

        button_s0 = tk.Button(win, command=select0, text="侧拍", width=20, height=2)
        button_s0.place(relx=0.45, rely=0.3, relwidth=0.05, relheight=0.05)
        button_s1 = tk.Button(win, command=select1, text="俯拍", width=20, height=2)
        button_s1.place(relx=0.50, rely=0.3, relwidth=0.05, relheight=0.05)
        button_insert = tk.Button(win, command=lambda x=age: insert_text(x), text="确认", width=20, height=2)
        button_insert.place(relx=0.45, rely=0.4, relwidth=0.1, relheight=0.1)

        # -------------右边输出框-------------
        # text_run = tk.Label(win, text=txt)
        # text_run.place(relx=0.69, rely=0.1, relwidth=0.2, relheight=0.4)
        right_info()

        # -------------底部示例照片-------------
        lb_pics = tk.Label(win, text='示例手势:')
        lb_pics.place(relx=0, rely=0.69, relwidth=0.05, relheight=0.05)

        path = str(1) + '.png'
        photo1 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 0 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo1)

        path = str(2) + '.png'
        photo2 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 1 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo2)

        path = str(3) + '.png'
        photo3 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 2 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo3)

        path = str(4) + '.png'
        photo4 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 3 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo4)

        path = str(5) + '.png'
        photo5 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 4 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo5)

        path = str(6) + '.png'
        photo6 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 5 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo6)

        path = str(7) + '.png'
        photo7 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 6 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo7)

        path = str(8) + '.png'
        photo8 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 7 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo8)

        path = str(9) + '.png'
        photo9 = tk.PhotoImage(file=path)
        canvas = tk.Canvas(win, width=100, height=100)
        canvas.place(relx=0.05 + 8 / 10, rely=0.65)
        canvas.create_image(50, 50, image=photo9)

        # -------------底部9种手势按钮-------------
        lb_butt = tk.Label(win, text='按下即拍照')
        lb_butt.place(relx=0, rely=0.8, relwidth=0.05, relheight=0.05)
        for i in range(0, 9):
            button = tk.Button(win, command=lambda x=i: button_command(x), text="手势" + str(i + 1), cursor="hand2",
                               width=25, height=2)
            button.place(relx=(i / 10 + 0.06), rely=0.8, relwidth=0.07, relheight=0.06)

        button_next = tk.Button(win, command=next_one, text="next one", width=20,
                                height=2)
        button_next.place(relx=0.45, rely=0.9, relwidth=0.07, relheight=0.07)
        # -------------视频展示部分-------------
        button_flag = tk.Button(win, command=open_video, text="turn on/off", width=20,
                                height=2)
        button_flag.place(relx=0.1, rely=0.56, relwidth=0.07, relheight=0.07)

        video_thread = threading.Thread(target=video_demo, args=())
        video_thread.start()
        win.mainloop()


def right_info():
    global txt
    text_run = tk.Label(win, text=txt)
    text_run.place(relx=0.69, rely=0.1, relwidth=0.2, relheight=0.4)


def insert_text(e):
    global male, age, txt, info
    age = e.get()
    if age == '':
        info = "还没输入年龄,请输入年龄!!!"
    txt = "性别:" + str(male) + "\n年龄:" + str(age) + "\n选用:" + str(select) + "\n\n" + str(info)

    right_info()


def select0():
    global info, male, age, select, txt
    select = 0
    txt = "性别:" + str(male) + "\n年龄:" + str(age) + "\n选用:" + str(select) + "\n\n" + str(info)
    right_info()


def select1():
    global info, male, age, select, txt
    select = 1
    txt = "性别:" + str(male) + "\n年龄:" + str(age) + "\n选用:" + str(select) + "\n\n" + str(info)
    right_info()


def male0():
    global info, male, age, select, txt
    male = 0
    txt = "性别:" + str(male) + "\n年龄:" + str(age) + "\n选用:" + str(select) + "\n\n" + str(info)
    right_info()


def male1():
    global info, male, age, select, txt
    male = 1
    txt = "性别:" + str(male) + "\n年龄:" + str(age) + "\n选用:" + str(select) + "\n\n" + str(info)
    right_info()


def button_command(x):
    global info, male, age, select, txt, save_flag
    print("hello" + str(x + 1))
    if age == '':
        info = "还没输入年龄,请输入年龄!!!"
    elif int(str(age)) < 0:
        info = "年龄不在0~100,请重新输入"
    elif int(str(age)) > 100:
        info = "年龄不在0~100,请重新输入"
    else:
        info = "开始拍照辣"
        save_flag = True
    txt = "性别:" + str(male) + "\n年龄:" + str(age) + "\n选用:" + str(select) + "\n\n" + str(info)
    right_info()


def next_one():
    initface(win)


def open_video():
    global Flag
    if not Flag:
        Flag = True
    else:
        Flag = False
    initface(win)


def video_demo():
    capture = cv2.VideoCapture(0)  # 1是摄像头的ID,这里我有两个摄像头,分别是0和1
    global Flag, save_flag, path, info, image_name
    while Flag:
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        if save_flag:
            # 保存照片
            cv2.imwrite(str(path)+"/"+str(image_name)+".png", frame)
            print("hallo", info)
            save_flag = False
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        image = cv2.resize(cv2image, (500, 300))
        img = Image.fromarray(image)
        image_file = ImageTk.PhotoImage(image=img)
        canvas = tk.Canvas(win, width=500, height=300)
        canvas.place(relx=0, rely=0.15)
        canvas.create_image(0, 0, anchor='nw', image=image_file)
        obr = image_file  # 很重要,去掉视频会闪烁
        win.update_idletasks()
        win.update()


if __name__ == '__main__':
    win = tk.Tk()
    global Flag, txt, male, age, select, info, save_flag, path, image_name
    Flag = True
    save_flag = False
    male = 1
    age = ''
    select = 0
    info = "初始配置是男性,22岁,俯拍,请选择"
    txt = "性别:" + str(male) + "\n年龄:" + str(age) + "\n选用:" + str(select) + "\n\n" + str(info)
    path =r'C:\Users\75400\Desktop'
    image_name = '1'
    basebesk(win)
    win.mainloop()
