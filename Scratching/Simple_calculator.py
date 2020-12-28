#Building a GUI calculator

from tkinter import *

root = Tk()
root.title('Simple Calculator')
#root.configure(background="black")
#root.iconbitmap('accessories_calculator.ico')

e = Entry(root ,width=45 ,borderwidth=5 ,bg='blue' ,fg='white')
e.grid(row=0 ,column=0 ,columnspan=3 ,padx=10 ,pady=10)

# ------------------- Functons ---------------------------- #

def myClick(num) :
    prev = e.get()
    e.delete(0,END)
    e.insert(0,str(prev)+str(num))

def myadd() :
    global fir
    global operation
    operation = 'add'
    fir = int(e.get())
    e.delete(0 ,END)

def mysub() :
    global fir
    global operation
    operation = 'sub'
    fir = int(e.get())
    e.delete(0 ,END)

def mymult() :
    global fir
    global operation
    operation = 'mult'
    fir = int(e.get())
    e.delete(0 ,END)

def mydivi() :
    global fir
    global operation
    operation = 'divi'
    fir = int(e.get())
    e.delete(0 ,END)

def myclr() :
    e.delete(0 ,END)

def myequ() :
    sec = int(e.get())
    e.delete(0 ,END)
    if operation == 'add' : e.insert(0 ,fir+sec)
    elif operation == 'sub' : e.insert(0 ,fir-sec)
    elif operation == 'mult' : e.insert(0 ,fir*sec)
    elif operation == 'divi' :
        if sec == 0 : e.insert(0,'INFY')
        else : e.insert(0 ,fir/sec)

# ------------------- Buttons ------------------------ #

butt_7 = Button(root ,text='7' ,padx=40 ,pady=20 ,command=lambda : myClick(7))
butt_8 = Button(root ,text='8' ,padx=40 ,pady=20 ,command=lambda : myClick(8))
butt_9 = Button(root ,text='9' ,padx=40 ,pady=20 ,command=lambda : myClick(9))

butt_4 = Button(root ,text='4' ,padx=40 ,pady=20 ,command=lambda : myClick(4))
butt_5 = Button(root ,text='5' ,padx=40 ,pady=20 ,command=lambda : myClick(5))
butt_6 = Button(root ,text='6' ,padx=40 ,pady=20 ,command=lambda : myClick(6))

butt_1 = Button(root ,text='1' ,padx=40 ,pady=20 ,command=lambda : myClick(1))
butt_2 = Button(root ,text='2' ,padx=40 ,pady=20 ,command=lambda : myClick(2))
butt_3 = Button(root ,text='3' ,padx=40 ,pady=20 ,command=lambda : myClick(3))

butt_0 = Button(root ,text='0' ,padx=40 ,pady=20 ,command=lambda : myClick(0))
butt_add = Button(root ,text='+' ,padx=40 ,pady=20 ,command=myadd)
butt_sub = Button(root ,text='-' ,padx=41 ,pady=20 ,command=mysub)

butt_mult = Button(root ,text='*' ,padx=40 ,pady=20 ,command=mymult)
butt_div = Button(root ,text='/' ,padx=43 ,pady=20 ,command=mydivi)
butt_clr = Button(root ,text='DEL' ,padx=32 ,pady=20 ,bg='red' ,fg='black' ,command=myclr)

butt_equ = Button(root ,text='=' ,padx=100 ,pady=20 ,bg='green' ,fg='white' ,command=myequ)


# -------------------- Grid ---------------------------------- #
butt_7.grid(row=1 ,column=0)
butt_8.grid(row=1 ,column=1)
butt_9.grid(row=1 ,column=2)

butt_4.grid(row= 2,column=0)
butt_5.grid(row= 2,column=1)
butt_6.grid(row= 2 ,column=2)

butt_1.grid(row= 3,column=0)
butt_2.grid(row= 3,column=1)
butt_3.grid(row= 3,column=2)

butt_0.grid(row= 4,column=0)
butt_add.grid(row= 4,column=1)
butt_sub.grid(row= 4,column=2)

butt_mult.grid(row= 5,column=0)
butt_div.grid(row= 5,column=1)
butt_clr.grid(row= 5,column=2)

butt_equ.grid(row=6 ,column=0 ,columnspan = 3)


root.mainloop()
