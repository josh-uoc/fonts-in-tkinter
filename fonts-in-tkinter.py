from tkinter import Tk, font
root = Tk()
root.withdraw()

fonts = [f.lower() for f in font.families()]

while True:
    text = input("Enter the font: ").lower()
    if text in fonts:
        print("yes")
    else:
        print("no")



