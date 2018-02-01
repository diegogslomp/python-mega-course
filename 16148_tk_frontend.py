'''
This program stores book information:
    Title, Author
    Year, ISBN

User can:
    View all records
    Search entry
    Add entry
    Update entry
    Delete
    Close
'''
import tkinter as tk
from tkinter import END
import backend as be

def get_selected_listbox_row(event):
    global selected_listbox_row
    try:
        index = list1.curselection()[0]
        selected_listbox_row = list1.get(index)
        e1.delete(0,END)
        e1.insert(0,str(selected_listbox_row[1]))
        e2.delete(0,END)
        e2.insert(0,str(selected_listbox_row[2]))
        e3.delete(0,END)
        e3.insert(0,str(selected_listbox_row[3]))
        e4.delete(0,END)
        e4.insert(0,str(selected_listbox_row[4]))
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in be.search(title=e1.get(), author=e2.get(),
                        year=e3.get(), isbn=e4.get()):
        list1.insert(END, row)

def add_command():
    if not all(x == '' for x in (e1.get(), e2.get(), e3.get(), e4.get())):
        be.add(title=e1.get(), author=e2.get(), year=e3.get(), isbn=e4.get())#u
        view_command()

def delete_command():
    try:
        be.delete(selected_listbox_row[0])
        view_command()
    except NameError:
        pass

def update_command():
    try:
        be.update(id=selected_listbox_row[0], title=e1.get(),
                 author=e2.get(), year=e3.get(), isbn=e4.get())
        view_command()
    except NameError:
        pass

window = tk.Tk()
window.wm_title('BookStore')

l1 = tk.Label(window,text="Title")
l1.grid(row=0, column=0)
e1 = tk.Entry(window, textvariable=tk.StringVar())
e1.grid(row=0, column=1)

l2 = tk.Label(window,text="Author")
l2.grid(row=0, column=2)
e2 = tk.Entry(window, textvariable=tk.StringVar())
e2.grid(row=0, column=3)

l3 = tk.Label(window,text="Year")
l3.grid(row=1, column=0)
e3 = tk.Entry(window, textvariable=tk.StringVar())
e3.grid(row=1, column=1)

l4 = tk.Label(window,text="ISBN")
l4.grid(row=1, column=2)
e4 = tk.Entry(window, textvariable=tk.StringVar())
e4.grid(row=1, column=3)

list1 = tk.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
list1.bind('<<ListboxSelect>>', get_selected_listbox_row)
sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command = list1.yview)

b1 = tk.Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = tk.Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = tk.Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)
b4 = tk.Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = tk.Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = tk.Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
