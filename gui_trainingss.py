from tkinter import messagebox
import tkinter


window = tkinter.Tk()
window.wm_withdraw()
window.geometry("30x30+200+200")#remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
a1 = messagebox.showinfo("Title", "message")
a2 = messagebox.showinfo()
a3 = messagebox.showwarning()
a4 = messagebox.showerror()
a5 = messagebox.askquestion()
a6 = messagebox.askokcancel()
a7 = messagebox.askyesno()
a8 = messagebox.askretrycancel()

print(a1,a2,a3,a4,a5,a6,a7,a8)