import easygui

easygui.msgbox("Hello world")

answer = easygui.buttonbox("What is my favourite color?", choices = ["green", "red", "blue"])

if answer is "red":
    easygui.msgbox("Damn, you got it right")
else:
    easygui.msgbox("Huhu, you know nothing bout me")
