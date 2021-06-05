import math
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from typing import List
import speech_recognition as sr
import pyttsx3
import webbrowser

expression = ""


def speak(_text):
    VIE_voice = (
        "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
    )
    engine = pyttsx3.init()
    engine.setProperty("voice", VIE_voice)
    engine.say(text=_text)
    engine.runAndWait()


def speechInput():
    global expression
    mic = sr.Microphone(device_index=1)
    rec = sr.Recognizer()
    with mic:
        rec.adjust_for_ambient_noise(mic)
        speak("Hãy đọc ra một phép tính")
        audio = rec.listen(mic)

        try:
            expression = rec.recognize_google(audio_data=audio, language="vi-VN")
            print("input:", expression)
            parseExpression()
            if "=" in expression:
                expression = expression.replace("=", "")
                equation.set(expression)
                expression = expression.replace(" ", "")
                equalpress()
            else:
                equation.set(expression)
                expression = expression.replace(" ", "")
        except:
            pass


def parseExpression():
    global expression
    expression = expression.replace("cộng", "+")
    expression = expression.replace("trừ", "-")
    expression = expression.replace("nhân", "*")
    expression = expression.replace("lần", "*")
    expression = expression.replace("chia", "/")
    expression = expression.replace("không", "0")
    expression = expression.replace("một", "1")
    expression = expression.replace("hai", "2")
    expression = expression.replace("ba", "3")
    expression = expression.replace("bốn", "4")
    expression = expression.replace("năm", "5")
    expression = expression.replace("sáu", "6")
    expression = expression.replace("bảy", "7")
    expression = expression.replace("tám", "8")
    expression = expression.replace("chín", "9")
    expression = expression.replace("bằng", "=")
    expression = expression.replace("mở ngoặc", "(")
    expression = expression.replace("đóng ngoặc", ")")
    expression = expression.replace("âm", "-")

    # sin
    expression = expression.replace("sin", "sin(")
    expression = expression.replace("xin", "sin(")
    # cos
    expression = expression.replace("cos", "cos(")
    expression = expression.replace("code", "cos(")
    expression = expression.replace("cốt", "cos(")
    # tan
    expression = expression.replace("tan", "tan(")
    expression = expression.replace("tang", "tan(")
    # pi
    expression = expression.replace("pi", "π")
    expression = expression.replace("số pi", "π")
    # bình phương
    expression = expression.replace("bình", "**2")
    # căn
    expression = expression.replace("căn", "**0.5")
    # mũ
    expression = expression.replace("mũ", "**")
    print("parse:", expression)


# Function to update expression in the text entry box
def press(num):
    global expression
    expression = str(expression) + str(num)
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        print("expression to calc:", expression)
        l = len(str(expression))
        if "sin" in expression:
            # num = expression[4 : l - 1]
            num = expression[4::]
            result = round(math.sin(math.radians(float(num))))
        elif "cos" in expression:
            # num = expression[4 : l - 1]
            num = expression[4::]
            result = round(math.cos(math.radians(float(num))))
        elif "tan" in expression:
            # num = expression[4 : l - 1]
            num = expression[4::]
            result = round(math.tan(math.radians(float(num))))

        else:
            result = eval(str(expression))
            print(result)

        equation.set(result)
        expression = ""
    except:
        equation.set("ERROR")
        expression = ""


def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def negative():
    global expression
    temp = eval(expression)
    negative = temp * -1
    equation.set(negative)
    expression = equation.get()
    print(expression, type(expression))


def calcPI():
    global expression
    temp = eval(expression)
    calcPI = temp * math.pi
    equation.set(calcPI)
    expression = equation.get()
    print(expression, type(expression))


# def calcSQRT():
#     global expression
#     temp = eval(expression)
#     sqrt = math.sqrt(temp)
#     equation.set(sqrt)
#     expression = equation.get()
#     print(expression, type(expression))


def percent():
    global expression
    temp = eval(expression)
    percent = temp / 100
    equation.set(percent)
    expression = equation.get()
    print(expression, type(expression))


def clear():
    global expression
    expression = ""
    equation.set("0")


def openCalculator():
    calc = Toplevel()
    calc.configure(background="black")
    calc.resizable(0, 0)
    calc.geometry("445x558+100+100")
    calc.title("Calculator")
    entry_font = Font(size=25, weight="bold")
    equation.set("0")

    # load images
    img_clear = PhotoImage(file="IMG\\clear.png")
    img_backspace = PhotoImage(file="IMG\\Backspace.png")
    img_percent = PhotoImage(file="IMG\\percent.png")
    img_dot = PhotoImage(file="IMG\\dot.png")
    img_rec = PhotoImage(file="IMG\\REC.png")
    img_equal = PhotoImage(file="IMG\\equal.png")
    img_add = PhotoImage(file="IMG\\add.png")
    img_minus = PhotoImage(file="IMG\\minus.png")
    img_multiple = PhotoImage(file="IMG\\multiple.png")
    img_divide = PhotoImage(file="IMG\\divide.png")
    img_0 = PhotoImage(file="IMG\\0.png")
    img_1 = PhotoImage(file="IMG\\1.png")
    img_2 = PhotoImage(file="IMG\\2.png")
    img_3 = PhotoImage(file="IMG\\3.png")
    img_4 = PhotoImage(file="IMG\\4.png")
    img_5 = PhotoImage(file="IMG\\5.png")
    img_6 = PhotoImage(file="IMG\\6.png")
    img_7 = PhotoImage(file="IMG\\7.png")
    img_8 = PhotoImage(file="IMG\\8.png")
    img_9 = PhotoImage(file="IMG\\9.png")

    img_sin = PhotoImage(file="IMG\\sin.png")
    img_cos = PhotoImage(file="IMG\\cos.png")
    img_tan = PhotoImage(file="IMG\\tan.png")
    img_open = PhotoImage(file="IMG\\open.png")
    img_close = PhotoImage(file="IMG\\close.png")
    img_pi = PhotoImage(file="IMG\\pi.png")
    img_negative = PhotoImage(file="IMG\\negative.png")
    img_sqrt = PhotoImage(file="IMG\\sqrt.png")
    img_power = PhotoImage(file="IMG\\power.png")
    img_square = PhotoImage(file="IMG\\square.png")

    # ------------------------------------
    # buttons grid
    expression_field = Entry(
        calc,
        textvariable=equation,
        bd=2,
        fg="white",
        bg="black",
        font=entry_font,
    )

    # button row 1
    button_clear = Button(
        calc,
        bg="black",
        bd=0,
        width=75,
        height=75,
        image=img_clear,
        command=clear,
    )

    button_backspace = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_backspace,
        command=delete,
    )

    button_percent = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_percent,
        command=percent,
    )

    button_divide = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_divide,
        command=lambda: press("/"),
    )

    # button row 2
    button_7 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_7,
        command=lambda: press("7"),
    )

    button_8 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_8,
        command=lambda: press("8"),
    )

    button_9 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_9,
        command=lambda: press("9"),
    )

    button_multiple = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_multiple,
        command=lambda: press("*"),
    )

    # button row 3
    button_4 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_4,
        command=lambda: press("4"),
    )

    button_5 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_5,
        command=lambda: press("5"),
    )

    button_6 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_6,
        command=lambda: press("6"),
    )

    button_minus = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_minus,
        command=lambda: press("-"),
    )

    # button row 4
    button_1 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_1,
        command=lambda: press("1"),
    )

    button_2 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_2,
        command=lambda: press("2"),
    )

    button_3 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_3,
        command=lambda: press("3"),
    )

    button_add = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_add,
        command=lambda: press("+"),
    )

    # button row 5
    button_rec = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_rec,
        command=speechInput,
    )

    button_0 = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_0,
        command=lambda: press("0"),
    )

    button_dot = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_dot,
        command=lambda: press("."),
    )

    button_equal = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_equal,
        command=equalpress,
    )

    button_sin = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_sin,
        command=lambda: press("sin("),
    )

    button_cos = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_cos,
        command=lambda: press("cos("),
    )

    button_tan = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_tan,
        command=lambda: press("tan("),
    )

    button_open = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_open,
        command=lambda: press("("),
    )

    button_close = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_close,
        command=lambda: press(")"),
    )

    button_negative = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_negative,
        command=negative,
    )

    button_sqrt = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_sqrt,
        command=lambda: press("**0.5"),
    )

    button_power = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_power,
        command=lambda: press("**"),
    )

    button_square = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_square,
        command=lambda: press("**2"),
    )

    button_pi = Button(
        calc,
        bd=0,
        width=75,
        height=75,
        bg="black",
        image=img_pi,
        command=calcPI,
    )

    # ---------------------------------
    # place buttons
    expression_field.grid(row=0, column=0, columnspan=5, ipady=20, ipadx=40)
    button_sin.grid(row=1, column=0)
    button_cos.grid(row=1, column=1)
    button_tan.grid(row=1, column=2)
    button_open.grid(row=1, column=3)
    button_close.grid(row=1, column=4)

    button_sqrt.grid(row=2, column=0)
    button_clear.grid(row=2, column=1)
    button_backspace.grid(row=2, column=2)
    button_percent.grid(row=2, column=3)
    button_divide.grid(row=2, column=4)

    button_square.grid(row=3, column=0)
    button_7.grid(row=3, column=1)
    button_8.grid(row=3, column=2)
    button_9.grid(row=3, column=3)
    button_multiple.grid(row=3, column=4)

    button_power.grid(row=4, column=0)
    button_4.grid(row=4, column=1)
    button_5.grid(row=4, column=2)
    button_6.grid(row=4, column=3)
    button_minus.grid(row=4, column=4)

    button_pi.grid(row=5, column=0)
    button_1.grid(row=5, column=1)
    button_2.grid(row=5, column=2)
    button_3.grid(row=5, column=3)
    button_add.grid(row=5, column=4)

    button_rec.grid(row=6, column=0)
    button_negative.grid(row=6, column=1)
    button_0.grid(row=6, column=2)
    button_dot.grid(row=6, column=3)
    button_equal.grid(row=6, column=4)

    # --------------------------
    # reference images to buttons
    button_clear.image = img_clear
    button_backspace.image = img_backspace
    button_percent.image = img_percent
    button_divide.image = img_divide
    button_7.image = img_7
    button_8.image = img_8
    button_9.image = img_9
    button_multiple.image = img_multiple
    button_4.image = img_4
    button_5.image = img_5
    button_6.image = img_6
    button_minus.image = img_minus
    button_1.image = img_1
    button_2.image = img_2
    button_3.image = img_3
    button_add.image = img_add
    button_rec.image = img_rec
    button_0.image = img_0
    button_dot.image = img_dot
    button_equal.image = img_equal

    button_sin.image = img_sin
    button_cos.image = img_cos
    button_tan.image = img_tan
    button_open.image = img_open
    button_close.image = img_close
    button_negative.image = img_negative
    button_sqrt.image = img_sqrt
    button_power.image = img_power
    button_square.image = img_square
    button_pi.image = img_pi

    calc.mainloop()


ytb_link = "https://youtu.be/6DJXUUAqrRE"
git_link = "https://github.com/minhquan54772/XLTN-Voice-Calculator"


def openLink(_link):
    webbrowser.open_new_tab(_link)


def openUserguide():
    guide = Toplevel()
    guide.title("Hướng dẫn sử dụng")
    guide.geometry("500x500+50+50")
    guide.config(background="light gray")

    buoc1 = LabelFrame(
        guide,
        text="Bước 1:",
        font=("Helvetica", 16),
    )
    buoc2 = LabelFrame(
        guide,
        text="Bước 2:",
        font=("Helvetica", 16),
    )
    commands = LabelFrame(
        guide,
        text="Các lệnh có thể sử dụng:",
        font=("Helvetica", 16),
    )

    buoc1.pack(fill="both", expand=True, padx=5, pady=5)
    buoc2.pack(fill="both", expand=True, padx=5, pady=5)
    commands.pack(fill="both", expand=True, padx=5, pady=5)

    b1 = Label(
        buoc1,
        text=(
            'Nhấn nút "Bắt đầu sử dụng" tại màn hình Chào mừng. Một giao diện máy tính xuất hiện)'
        ),
        wraplength=400,
    )
    b2 = Label(
        buoc2,
        text='Tại giao diện máy tính, bấm nút "🎙" để bắt đầu ghi âm. Hãy nói ra một phép tính, kết thúc với dấu \=, màn hình sẽ hiển thị kết quả. Sau mỗi phép tính, hãy bấm lại nút "🎙" để ghi nhận phép tính tiếp theo',
        wraplength=400,
    )

    cmd = Label(
        commands,
        text="Ứng dụng hỗ trợ các lệnh như cộng, trừ, nhân, chia, sin, cos, tan, căn bậc 2, bình phương, mũ, âm",
        wraplength=400,
    )
    example = Label(
        commands, text='Ví dụ: "1 cộng 1 bằng", "2 mũ 4 bằng", "3 bình bằng",... '
    )

    b1.pack(fill="both", expand=True)
    b2.pack(fill="both", expand=True)
    cmd.pack(fill="both", expand=True)
    example.pack(fill="both", expand=True)
    guide.mainloop()


if __name__ == "__main__":
    app = Tk()
    app.title("Voice Calculator")
    app.geometry("550x500+50+50")
    app.config(background="gray")
    equation = StringVar()

    welcome = Label(
        app,
        fg="black",
        bg="gray",
        font=("Helvetica", 20),
        text="WELCOME TO VOICE CALCULATOR!",
    )
    slogan = Label(
        app,
        fg="black",
        bg="gray",
        font=("Helvetica", 15),
        text='"Give your hands a break, and make your voice go to work"',
    )
    openCalc = Button(app, text="Bắt đầu sử dụng", command=openCalculator)
    guide = Button(app, text="Hướng dẫn sử dụng", command=openUserguide)

    img_youtube = PhotoImage(file="IMG\\youtube.png")
    img_github = PhotoImage(file="IMG\\github.png")
    button_ytb = Button(
        app,
        bg="gray",
        bd=0,
        width=75,
        height=75,
        image=img_youtube,
        command=lambda: openLink(ytb_link),
    )
    button_git = Button(
        app,
        bg="gray",
        bd=0,
        width=75,
        height=75,
        image=img_github,
        command=lambda: openLink(git_link),
    )
    author = Label(
        app,
        text="Nguyễn Minh Quân - Trần Thu Phương - 2021",
        bg="gray",
        fg="light gray",
        font=("Helvetica", 10),
    )

    welcome.grid(row=0, column=0, columnspan=4, padx=20, pady=30)
    slogan.grid(row=1, column=0, columnspan=4, pady=30, padx=10)
    openCalc.grid(row=2, column=1, pady=60)
    guide.grid(row=2, column=2, pady=60)
    button_ytb.grid(row=3, column=1)
    button_git.grid(row=3, column=2)
    author.grid(row=4, columnspan=4, pady=60)

    app.mainloop()
