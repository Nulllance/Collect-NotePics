import tkinter as tk
from PIL import Image, ImageTk
import cv2
import threading
import os


def right_info():
    text_run = tk.Label(window, text=txt)
    text_run.place(relx=0.69, rely=0.1, relwidth=0.2, relheight=0.4)


def insert_text(e):
    global age, info, txt
    age_get = e.get()
    if age_get == '':
        info = "还没输入年龄,请输入年龄!!!"
    else:
        age = int(age_get)
    txt = "当前的参数\n" + "性别:" + str(malelist.get(male)) + "\n年龄:" + str(age) + "\n选用:" + str(
            selectlist.get(select)) + "\n\n" + str(info)
    print(txt)
    right_info()


def select0():
    global info, male, age, select, txt
    select = 0
    txt = "当前的参数\n" + "性别:" + str(malelist.get(male)) + "\n年龄:" + str(age) + "\n选用:" + str(
        selectlist.get(select)) + "\n\n" + str(info)
    right_info()


def select1():
    global info, male, age, select, txt
    select = 1
    txt = "当前的参数\n" + "性别:" + str(malelist.get(male)) + "\n年龄:" + str(age) + "\n选用:" + str(
        selectlist.get(select)) + "\n\n" + str(info)
    right_info()


def male0():
    global info, male, age, select, txt
    male = 0
    txt = "当前的参数\n" + "性别:" + str(malelist.get(male)) + "\n年龄:" + str(age) + "\n选用:" + str(
        selectlist.get(select)) + "\n\n" + str(info)
    right_info()


def male1():
    global info, male, age, select, txt
    male = 1
    txt = "当前的参数\n" + "性别:" + str(malelist.get(male)) + "\n年龄:" + str(age) + "\n选用:" + str(
        selectlist.get(select)) + "\n\n" + str(info)
    right_info()


def button_command(x):
    global info, male, age, select, txt, save_flag, gesture, count
    gesture = x + 1
    print("hello" + str(x + 1))
    if age == '':
        info = "还没输入年龄,请输入年龄!!!"
    elif int(str(age)) < 0:
        info = "年龄不在0~100,请重新输入"
    elif int(str(age)) > 100:
        info = "年龄不在0~100,请重新输入"
    else:
        save_flag = True
    if not Flag:
        info = "请打开摄像头"
    txt = "当前的参数\n" + "性别:" + str(malelist.get(male)) + "\n年龄:" + str(age) + "\n选用:" + str(
        selectlist.get(select)) + "\n\n" + str(info)
    right_info()
    count = count + 1


def save_config():
    global count, total_count
    root1 = os.getcwd()
    txt_dir1 = os.path.join(root1 + '/total_count.txt')
    file = open(txt_dir1, 'w', encoding='utf-8')
    file.write(str(total_count))
    file.close()

    root2 = os.getcwd()
    txt_dir2 = os.path.join(root2 + '/count.txt')
    file = open(txt_dir2, 'w', encoding='utf-8')
    file.write(str(count))
    file.close()


def next_one():
    global count, people_num
    people_num = people_num + 1
    count = 0
    right_info()


def open_video():
    global Flag
    if not Flag:
        Flag = True
    else:
        Flag = False
    run_video()


def run_video():
    video_thread = threading.Thread(target=video_demo, args=())
    video_thread.start()


def video_demo():
    capture = cv2.VideoCapture(1)  # 1是摄像头的ID,这里我有两个摄像头,分别是0和1
    global save_flag, path, info, image_name, select, gesture, count, people_num, male, age
    while Flag:
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        # 保存照片
        if save_flag:
            # 图片名字：拍摄角度_手势类别_年龄_性别_num
            image_name = str(selectlist.get(select)) + "_" + str(age) + "_" + str(malelist.get(male)) + "_" + str(
                count % 10 + people_num * 10)
            # 路径/拍摄角度/手势
            select_name = "side" if select == 0 else "pitch"
            photo_path = str(path) + "/" + select_name + "/" + str(gesture)
            if not os.path.exists(photo_path):
                os.makedirs(photo_path)
            cv2.imwrite(str(photo_path) + "/" + str(image_name) + ".png", frame)
            info = "成功存储到手势" + str(gesture) + "文件中,第" + str(count % 10 + people_num * 10) + "张！\n已收集" + str(
                people_num) + "个人,共" + str(count + 1) + "张"
            save_flag = False
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        image = cv2.resize(cv2image, (500, 300))
        img = Image.fromarray(image)
        image_file = ImageTk.PhotoImage(image=img)
        canvas_video.create_image(0, 0, anchor='nw', image=image_file)
        obr = image_file  # 很重要,去掉视频会闪烁
        canvas_video.delete(all)
        del cv2image, image, img, image_file, frame, ret
        window.update_idletasks()
        window.update()
    capture.release()


if __name__ == '__main__':
    global Flag, txt, male, age, select, info, save_flag, path, image_name, gesture, count, total_count, people_num, malelist, selectlist
    malelist = {0: "female", 1: "male"}
    selectlist = {0: "side", 1: "pitch"}
    info = "请先选择性别,填写年龄,选择拍摄角度,\n按确认键。再按对应的拍摄键"
    path = r'C:\Users\75400\Desktop\PHG_Dataset'

    Flag = True
    save_flag = False
    male = 1
    age = 22
    select = 0
    gesture = 0
    count = 0
    total_count = 0
    image_name = ''
    people_num = 0

    txt = "当前的参数\n" + "性别:" + str(malelist.get(male)) + "\n年龄:" + str(age) + "\n选用:" + str(
        selectlist.get(select)) + "\n\n" + str(info)
    root = os.getcwd()
    try:
        txt_dir = os.path.join(root + '/total_count.txt')
        f = open(txt_dir, 'r')
        total_count = f.read()
        total_count = int(total_count)
        f.close()
    except IOError:
        f = open(txt_dir, 'w')
        f.write(str(total_count))
        f.close()

    try:
        txt_dir = os.path.join(root + '/count.txt')
        f = open(txt_dir, 'r')
        count = f.read()
        count = int(count)
        f.close()
    except IOError:
        f = open(txt_dir, 'w')
        f.write(str(count))
        f.close()

    window = tk.Tk()
    window.title("收集握手姿势")
    window.geometry('1200x800')
    window.config(bg='white')
    # -------------顶部文本介绍-------------
    introduction = "你好,这是一个手握笔姿势图片的收集小程序,可以用来收集握笔的9种姿势,分别标号为1~9,"

    text = tk.Text(window, width=20, height=5)
    text.place(relx=0, rely=0, relwidth=1, relheight=0.1)
    text.insert("insert", introduction)
    text.window_create("insert")

    # -------------中间的性别,年龄,拍摄角度的选择-------------
    lb_tip = tk.Label(window, text='请选择')
    lb_tip.place(relx=0.45, rely=0.15, relwidth=0.1, relheight=0.05)


    button_male0 = tk.Button(window, command=male0, text="女生", width=20, height=2)
    button_male0.place(relx=0.45, rely=0.2, relwidth=0.05, relheight=0.05)
    button_male1 = tk.Button(window, command=male1, text="男生", width=20, height=2)
    button_male1.place(relx=0.50, rely=0.2, relwidth=0.05, relheight=0.05)

    button_s0 = tk.Button(window, command=select0, text="侧拍", width=20, height=2)
    button_s0.place(relx=0.45, rely=0.25, relwidth=0.05, relheight=0.05)
    button_s1 = tk.Button(window, command=select1, text="俯拍", width=20, height=2)
    button_s1.place(relx=0.50, rely=0.25, relwidth=0.05, relheight=0.05)

    lb_age = tk.Label(window, text='age: ')
    lb_age.place(relx=0.45, rely=0.3, relwidth=0.05, relheight=0.05)
    age = tk.Entry(window)
    age.place(relx=0.50, rely=0.3, relwidth=0.05, relheight=0.05)

    button_insert = tk.Button(window, command=lambda x=age: insert_text(x), text="确认", width=20, height=2)
    button_insert.place(relx=0.45, rely=0.4, relwidth=0.1, relheight=0.1)
    # -------------右边输出框-------------
    right_info()
    button_save = tk.Button(window, command=save_config, text="保存配置信息", width=20,
                            height=2)
    button_save.place(relx=0.8, rely=0.56, relwidth=0.07, relheight=0.07)

    # -------------底部示例照片-------------
    lb_pics = tk.Label(window, text='示例手势:')
    lb_pics.place(relx=0, rely=0.69, relwidth=0.05, relheight=0.05)

    path = str(1) + '.png'
    photo1 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 0 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo1)

    path = str(2) + '.png'
    photo2 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 1 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo2)

    path = str(3) + '.png'
    photo3 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 2 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo3)

    path = str(4) + '.png'
    photo4 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 3 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo4)

    path = str(5) + '.png'
    photo5 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 4 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo5)

    path = str(6) + '.png'
    photo6 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 5 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo6)

    path = str(7) + '.png'
    photo7 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 6 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo7)

    path = str(8) + '.png'
    photo8 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 7 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo8)

    path = str(9) + '.png'
    photo9 = tk.PhotoImage(file=path)
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.place(relx=0.05 + 8 / 10, rely=0.65)
    canvas.create_image(50, 50, image=photo9)


    # -------------底部9种手势按钮-------------
    lb_butt = tk.Label(window, text='按下即拍照')
    lb_butt.place(relx=0, rely=0.8, relwidth=0.05, relheight=0.05)
    for i in range(0, 9):
        button = tk.Button(window, command=lambda x=i: button_command(x), text="手势" + str(i + 1), cursor="hand2",
                           width=25, height=2)
        button.place(relx=(i / 10 + 0.06), rely=0.8, relwidth=0.07, relheight=0.06)

    button_next = tk.Button(window, command=next_one, text="next one", width=20,
                            height=2)
    button_next.place(relx=0.45, rely=0.9, relwidth=0.07, relheight=0.07)

    # -------------视频展示部分-------------
    button_flag = tk.Button(window, command=open_video, text="打开摄像头", width=20,
                            height=2)
    button_flag.place(relx=0.1, rely=0.56, relwidth=0.07, relheight=0.07)
    global canvas_video
    canvas_video = tk.Canvas(window, width=500, height=300)
    canvas_video.place(relx=0, rely=0.15)
    run_video()
    window.mainloop()