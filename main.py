import tkinter as tk
from tkinter import messagebox
import playsound
import time

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--.-.-",
    "?": "..--..",
    "!": "-.-.--",
    "/": "-..-.",
    "\"": ".--.  ",
    "-": "-....-",
    "@": ".--.-.",
    " ": " "  # فاصله بین کلمات
}

def convert_text_to_morse():
    text_input = text_entry.get()
    morse_output = ""

    for char in text_input.upper():
        if char in morse_code:
            morse_output += morse_code[char] + " "  # فاصله بین حروف
        else:
            morse_output += "**" + char + "** "  # نمایش کاراکترهای ناشناخته

    morse_output = morse_output[:-1]  # حذف فاصله اضافی در انتها
    morse_label.config(text=morse_output)

    # پخش صدای کد مورس
    play_morse_sound(morse_output)


def play_morse_sound(morse_text):
    dots = "."
    dashes = "-"
    pause = "."

    sound_file = "morse_beep.wav"  # فایل صوتی بوق برای هر نقطه یا خط تیره

    for char in morse_text:
        if char == dots:
            playsound(sound_file)
            time.sleep(0.1)  # تنظیم مدت زمان پخش نقطه
        elif char == dashes:
            playsound(sound_file)
            time.sleep(0.3)  # تنظیم مدت زمان پخش خط تیره
        else:
            time.sleep(0.2)  # تنظیم مدت زمان مکث بین حروف


# ایجاد رابط کاربری گرافیکی
root = tk.Tk()
root.title("مبدل متن به کد مورس")

# برچسب ورودی متن
text_label = tk.Label(root, text="متن مورد نظر خود را وارد کنید:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

# دکمه تبدیل
convert_button = tk.Button(root, text="تبدیل به کد مورس", command=convert_text_to_morse)
convert_button.pack(pady=5)

# برچسب نمایش کد مورس
morse_label = tk.Label(root, text="")
morse_label.pack()

# برچسب راهنما
help_label = tk.Label(root, text="**راهنما:**\n- کاراکترهای ناشناخته با **** مشخص می‌شوند.\n- برای پخش صدای کد مورس، دکمه تبدیل را فشار دهید.")
help_label.pack()

# اجرای برنامه
root.mainloop()
