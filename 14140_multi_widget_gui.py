import tkinter

window = tkinter.Tk()

def kg_to_grams_pounds_onces():
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462
    ounces=float(e1_value.get())*35.274
    t1.delete("1.0",tkinter.END)
    t2.delete("1.0",tkinter.END)
    t3.delete("1.0",tkinter.END)
    t1.insert(tkinter.END,grams)
    t2.insert(tkinter.END,pounds)
    t3.insert(tkinter.END,ounces)

b1 = tkinter.Button(window,text="Convert",command=kg_to_grams_pounds_onces)
b1.grid(row=0,column=2)

e1_value=tkinter.StringVar()
e1 = tkinter.Entry(window, width=15,textvariable=e1_value)
e1.grid(row=0,column=1)

t0 = tkinter.Label(window, height=1,width=20,text="Kg")
t0.grid(row=0,column=0)

t1 = tkinter.Text(window, height=1,width=20)
t1.grid(row=1,column=0)

t2 = tkinter.Text(window, height=1,width=20)
t2.grid(row=1,column=1)

t3 = tkinter.Text(window, height=1,width=20)
t3.grid(row=1,column=2)

if __name__ == '__main__':
    window.mainloop()
