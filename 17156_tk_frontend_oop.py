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
from backend_oop import Database

class MainWindow:

    def __init__(self):
        self.db = Database('books.db')
        window = tk.Tk()
        window.wm_title('BookStore')

        l1 = tk.Label(window,text="Title")
        l1.grid(row=0, column=0)
        self.e1 = tk.Entry(window, textvariable=tk.StringVar())
        self.e1.grid(row=0, column=1)

        l2 = tk.Label(window,text="Author")
        l2.grid(row=0, column=2)
        self.e2 = tk.Entry(window, textvariable=tk.StringVar())
        self.e2.grid(row=0, column=3)

        l3 = tk.Label(window,text="Year")
        l3.grid(row=1, column=0)
        self.e3 = tk.Entry(window, textvariable=tk.StringVar())
        self.e3.grid(row=1, column=1)

        l4 = tk.Label(window,text="ISBN")
        l4.grid(row=1, column=2)
        self.e4 = tk.Entry(window, textvariable=tk.StringVar())
        self.e4.grid(row=1, column=3)

        self.list1 = tk.Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_listbox_row)
        sb1 = tk.Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command = self.list1.yview)

        self.b1 = tk.Button(window, text="View all", width=12, command=self.view_command)
        self.b1.grid(row=2, column=3)
        self.b2 = tk.Button(window, text="Search entry", width=12, command=self.search_command)
        self.b2.grid(row=3, column=3)
        self.b3 = tk.Button(window, text="Add entry", width=12, command=self.add_command)
        self.b3.grid(row=4, column=3)
        self.b4 = tk.Button(window, text="Update selected", width=12, command=self.update_command)
        self.b4.grid(row=5, column=3)
        self.b5 = tk.Button(window, text="Delete selected", width=12, command=self.delete_command)
        self.b5.grid(row=6, column=3)
        self.b6 = tk.Button(window, text="Close", width=12, command=window.destroy)
        self.b6.grid(row=7, column=3)

        window.mainloop()

    def get_selected_listbox_row(self, event):
        global selected_listbox_row
        try:
            index = self.list1.curselection()[0]
            selected_listbox_row = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(0,str(selected_listbox_row[1]))
            self.e2.delete(0,END)
            self.e2.insert(0,str(selected_listbox_row[2]))
            self.e3.delete(0,END)
            self.e3.insert(0,str(selected_listbox_row[3]))
            self.e4.delete(0,END)
            self.e4.insert(0,str(selected_listbox_row[4]))
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for row in self.db.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in self.db.search(title=self.e1.get(), author=self.e2.get(),
                            year=self.e3.get(), isbn=self.e4.get()):
            self.list1.insert(END, row)

    def add_command(self):
        if not all(x == '' for x in (self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get())):
            self.db.add(title=self.e1.get(), author=self.e2.get(), year=self.e3.get(), isbn=self.e4.get())
            self.view_command()

    def delete_command(self):
        try:
            self.db.delete(selected_listbox_row[0])
            self.view_command()
        except NameError:
            pass

    def update_command(self):
        try:
            self.db.update(id=selected_listbox_row[0], title=self.e1.get(),
                     author=self.e2.get(), year=self.e3.get(), isbn=self.e4.get())
            self.view_command()
        except NameError:
            pass

if __name__ == '__main__':
    window = MainWindow()
