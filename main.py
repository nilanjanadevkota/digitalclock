import time
from tkinter import Label, Tk


window=Tk()
window.title('digital clock')
window.geometry('200x100')
window.resizable(False,False)
window.configure(bg='black')
window.overrideredirect(1)

clock_label=Label(window,bg='black',fg='cyan',font=("ds-digital",25,'bold'),relief='flat')
clock_label.place(x=10 , y=20)

def update_label():
    current_time=time.strftime('%H:%M:%S %p')
    clock_label.configure(text=current_time)
    clock_label.after(80,update_label)


update_label()
window.mainloop()