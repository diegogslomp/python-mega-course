import tkinter as tk

window = tk.Tk()

def km_to_miles():
    miles=float(e1_value.get())*1.6
    t1.insert(tk.END,miles)

b1 = tk.Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

e1_value=tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = tk.Text(window, height=1,width=20)
t1.grid(row=0,column=2)

if __name__ == '__main__':
    window.mainloop()
