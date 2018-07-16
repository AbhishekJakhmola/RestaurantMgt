from tkinter import *
import time

root = Tk()

time_string= time.asctime( time.localtime(time.time()) )


list=['Veg Burger:      32.00','Non Veg Burger:45.00 ','Veg Sandwich:   35.00 ','Cold coffee:     35.00 ','Coffee :           25.00' ]

class Heading:
    def __init__(self,master):
        self.h1 = Label(master, text="Restaurant Management System", height=2, font="Helvetica 12", foreground='red')
        self.h1.grid(row=0, column=2)
        self.h2 = Label(master, text=time_string)
        self.h2.grid(row=0, column=4)
        master.title("Restaurant Management")

    def reset(self):
        a_var.set('0')
        b_var.set('0')
        c_var.set('0')
        d_var.set('0')
        e_var.set('0')
        f_var.set('0')



    def printText(self):
        for i in range(5):
            lst = Label(root, text=list[i])
            lst.grid(row=2 + i, column=4)

    def Total(self):
        price = int((b_var.get() * 32) + (c_var.get() * 45) + (d_var.get() * 35) + (e_var.get() * 35) + (f_var.get() * 25))
        price2 = price + price * 0.06
        pp = Label(root, text=price2,width = 13)
        pp.grid(row=9, column=1)






h=Heading(root)

#entry part
a = Label(root, text='Order no: ')
a.grid(row=1, column=0)
a_var = IntVar()
a1 = Entry(root, textvariabl=a_var)
a1.grid(row=1, column=1)
message = Label(root, text='Enter Quantity ',foreground ='green')
message.grid(row=2, column=0)
b = Label(root, text='Veg Burger: ')
b_var = IntVar()
b.grid(row=3, column=0)
b1 = Entry(root,textvariable =b_var)
b1.grid(row=3, column=1)
c= Label(root, text='Non Veg Burger: ')
c.grid(row=4, column=0)
c_var = IntVar()
c1 = Entry(root,textvariable=c_var)
c1.grid(row=4, column=1)
d = Label(root, text='Veg Sandwich: ')
d.grid(row=5, column=0)
d_var = IntVar()
d1 = Entry(root,textvariable =d_var)
d1.grid(row=5, column=1)
e = Label(root, text='Cold coffee: ')
e.grid(row=6, column=0)
e_var = IntVar()
e1 = Entry(root,textvariable =e_var)
e1.grid(row=6, column=1)
f = Label(root, text='Coffee : ')
f.grid(row=7, column=0)
f_var = IntVar()
f1 = Entry(root,textvariable=f_var)
f1.grid(row=7, column=1)


#menu part
mss = Button(root, text = 'Price list(INR)', width = 25, command= h.printText ,background ='Green')
mss.grid(row = 1,column=4)

exit = Button(root, text='Exit', width=12, command=root.destroy,background ='blue')
exit.grid(row=9, column=4)

ref = Button(root, text='Reset', width=12, background ='orange',command = h.reset)
ref.grid(row=9, column=2)

tot = Button(root, text='Total(tax incl.INR)', width=16, background ='violet',command = h.Total)
tot.grid(row=9, column=0)

root.resizable(False, False)
root.mainloop()