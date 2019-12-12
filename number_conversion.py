from tkinter import *
from tkinter import font

root = Tk()
root.title("number conversion")

Label(root, text="Decimal").grid(row=1,column=0)
e = Entry(root, width=35, borderwidth=3)
e.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

Label(root, text="binary").grid(row=3,column=0)
f = Entry(root, width=35, borderwidth=3)
f.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

Label(root, text="octal").grid(row=5,column=0)
g = Entry(root, width=35, borderwidth=3)
g.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

Label(root, text="hex").grid(row=7,column=0)
h = Entry(root, width=35, borderwidth=3)
h.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

helv36 = font.Font(family='Helvetica', size=12, weight='bold')

def button_clear():
    e.delete(0, END)
    f.delete(0, END)
    g.delete(0, END)
    h.delete(0, END)

def button_click():
   
    
    if e.get() > str(0):
        decimal = e.get()
        binar_1 = bin(int(decimal))
        binar_2 = binar_1.lstrip('0b')
        f.insert(0, binar_2)
        octal_1 = int(binar_2, 2);
        octal_2 = oct(octal_1).strip('0o') 
        g.insert(0, octal_2)
        h.insert(0, hex(octal_1).lstrip('0x'))

    elif f.get() > str(0):
        binar = f.get()
        decimal_1 = int(binar, 2)
        e.insert(0, decimal_1)
        g.insert(0, oct(decimal_1).strip('0o'))
        h.insert(0,hex(decimal_1).lstrip('0x'))

    elif g.get() > str(0):
        octal = g.get()
        octal_1 = str(int(octal, 8)); 
        octal_2 = int(octal_1)     
        f.insert(0, bin(octal_2).lstrip('0b'))
        e.insert(0, octal_1)
        h.insert(0, hex(octal_2).lstrip('0x'))
    else:
        hexx = h.get()      
        dec = int(hexx, 16)
        binary = bin(dec).lstrip('0b')
        octal = oct(dec).lstrip('0o')
        e.insert(0 , dec)
        f.insert(0, binary)
        g.insert(0, octal)

button_convert = Button(root, text="Convert", padx=40, pady=20, font=helv36, command=button_click).grid(row=9,column=0,columnspan=3)
button_clear = Button(root, text="Clear", padx=40, pady=20, font=helv36, command=button_clear).grid(row=10,column=0,columnspan=3)
root.mainloop()