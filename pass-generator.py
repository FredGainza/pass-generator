#!/usr/bin/env python
# coding: utf-8
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import string
import random
import base64
import os
import pyperclip

## You need to encode ico file to Base64 (for ico in tkinter wiondow)
## Go to https://www.motobit.com/util/base64-decoder-encoder.asp to convert your ico
icon = "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"

icondata = base64.b64decode(icon)
## The temp file is icon.ico
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()

## Possible options for the password
LOWERCASE = list(string.ascii_lowercase)
UPPERCASE = list(string.ascii_uppercase)
NUMBER = list(string.digits)
SYMBOLS = ['@', '#', '$', '%', '&', '_']
list_data = [LOWERCASE, UPPERCASE, NUMBER, SYMBOLS]


####################################################
#  START - Fonction to generate random password
####################################################

def generate():
    data = []
    password = ""
    
    ## error messages
    messages = {
        "msg_conditions": "No option for password characters has been selected.\nCheck at least one item.",
        "msg_pass_lenght": "The number of characters for the password is not valid (must be a number between 5 and 50)",
        "msg_pass_format": "The format specified for the number of characters is not valid.\nEnter a number between 5 and 50.",
        "msg_pass_empty": "The field 'number of characters' cannot be empty.\nEnter a number between 5 and 50."
    }

    # Selected options for the password
    conditions = [cond1, cond2, cond3, cond4]
    for i,c in enumerate(conditions):
        if c.get() == 1:
            data.extend(list_data[i])

    # Number of characters chosen for the password
    nb_car_str = nb.get()
    if nb_car_str != "":
        if nb_car_str.isdigit():
            nb_car = int(nb_car_str)
            if 5 <= nb_car <= 50:
                if len(data) != 0:
                    for i in range(nb_car):
                        password += data[random.randint(0, len(data)-1)]

                    pass_input.delete(0, tk.END)
                    pass_input.insert(0, password)
                    pyperclip.copy(password)

                else:
                    pass_input.delete(0, tk.END)
                    messagebox.showerror("Error Password Conditions", messages["msg_conditions"])
            else:
                pass_input.delete(0, tk.END)
                messagebox.showerror("Error Password Length", messages["msg_pass_lenght"])
        else:
            pass_input.delete(0, tk.END)
            messagebox.showerror("Error Password Format", messages["msg_pass_format"])
    else:
        pass_input.delete(0, tk.END)
        messagebox.showerror("Error Password Empty", messages["msg_pass_empty"])

####################################################
#  END - Fonction to generate random password
####################################################

## Window settings
root = tk.Tk()
root.title("Pass-Generator")
root.config(bg="#07566e")
root.iconbitmap(tempFile)
root.geometry("380x470")
root.maxsize(700,500)
root.minsize(380,470)

## Delete the tempfile
os.remove(tempFile)

## Fonts
helv12 = tkFont.Font(family='Source Sans Pro', size=12, weight="normal")
helv12_bold = tkFont.Font(family='Source Sans Pro', size=12, weight="bold")
helv14 = tkFont.Font(family='Source Sans Pro', size=14, weight="normal")
helv16_bold = tkFont.Font(family='Helvetica', size=16, weight="bold")

## Title
titre_glob = tk.Label(
    root, 
    text="GENERATE A PASSWORD", 
    font=helv16_bold, 
    fg="#14181a", 
    pady=16, 
    bg="#468ea4", 
    activebackground="#468ea4"
)
titre_glob.pack(fill='x')

## Number of characters - label
label_nb = tk.Label(
    root, 
    text="Nnumber of characters:   ",
    font=helv12, 
    fg="White",
    bg="#07566e", 
    activebackground="#07566e"
)
label_nb.pack(anchor="w", padx=(30,10), pady=(20,0))

## Number of characters - default value
nb_default = tk.StringVar(root)
nb_default.set(12)
nb = tk.Spinbox(root, font=helv12, from_=5, to=50, textvariable=nb_default)
nb.pack(anchor="w", padx=(33,10), pady=(5,20))

## Checkboxes
cond1 = tk.IntVar(value=1)
cond2 = tk.IntVar(value=1)
cond3 = tk.IntVar(value=1)
cond4 = tk.IntVar(value=0)

checks = [cond1, cond2, cond3, cond4]
checks_text = [
    "Lower case alpha characters",
    "Upper case alpha characters",
    "Numeric characters",
    "Special characters"
]

for i in range(4):
    z = tk.Checkbutton(
        root, 
        text=checks_text[i],
        anchor="w", 
        font=helv12, 
        onvalue=1, 
        offvalue=0, 
        variable=checks[i], 
        fg="white", 
        bg="#07566e", 
        activebackground="#07566e", 
        selectcolor="#0c232d"
    )
    z.pack(anchor="w", pady=1, padx=(30,10))

## Submit button
submit = tk.Button(
    root, 
    text="SUBMIT", 
    font=helv12,  
    bg="#022a3b", 
    fg="White", 
    activebackground="#07566e", 
    width=50, 
    relief="groove", 
    command=generate
)
submit.pack(padx=25, pady=(30,10))

ttk.Style().configure('TEntry', padding='2 5 2 5', foreground='darkred')
pass_input = ttk.Entry(root, font=helv12_bold)
pass_input.pack(pady=25, padx=25, fill='x')

root.mainloop()
