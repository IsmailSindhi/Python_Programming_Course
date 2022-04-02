import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("higgg")
# labels
name_label = ttk.Label(root,text="Name: ")
name_label.grid(row = 1, column=1)
email_label = ttk.Label(root,text="Email: ")
email_label.grid(row=2,column=1)
address_label = ttk.Label(root,text="Address")
address_label.grid(row=3,column=1)

# Entry box
name = tk.StringVar() # create variable
name_box = ttk.Entry(root,width=16, textvariable=name) # Entry box // varialbe
name_box.grid(row=1, column=2) # layout // position

email = tk.StringVar()
email_box = ttk.Entry(root, width=16, textvariable=email)
email_box.grid(row=2, column=2)

# Button
def action():
    print(" Button Pressed")

submit_button = ttk.Button(root, text='Submit', command= action)
submit_button.grid(row=4, column=1)
root.mainloop()