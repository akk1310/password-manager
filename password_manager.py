# from tkinter import *
# from tkinter import messagebox
# import random
# import pyperclip
# import json
import json
import os
import sys
from tkinter import Tk, Label, Entry, Button, messagebox, PhotoImage, Canvas,END
import random
import pyperclip

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


## ---------------------------- PASSWORD GENERATOR ------------------------------- #
## Password Generator Project
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    pass_inp.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():
#     website = web_inp.get()
#     email = email_inp.get()
#     password = pass_inp.get()
#     new_data = {
#         website: {
#             "email": email,
#             "password": password,
#         }
#     }

#     if len(password) == 0 or len(website) == 0:
#         messagebox.showinfo(title="Retry", message="Please fill the required fields")
#     else:
#         try:
#             with open("data.json", "r") as data_file:
#                     data = json.load(data_file)
#                 # try:
#                 #     data = json.load(data_file)
#                 # except json.JSONDecodeError:
#                 #     data = {}
#         except FileNotFoundError:
#             # data = {}
#             with open("data.json", "w") as data_file:
#                 json.dump(new_data, data_file, indent=4)
#         else:
#             data.update(new_data)
#             with open("data.json", "w") as data_file:
#                 json.dump(data, data_file, indent=4)
        
#         finally:
#             web_inp.delete(0, END)
#             pass_inp.delete(0, END)

# def find_password():
#     website = web_inp.get()
#     try:
#         with open("data.json") as data_file:
#             data=json.load(data_file)
#     except FileNotFoundError:
#         print("err")
#         messagebox.showinfo(title="Error",message="No Data File Found")
#     else:      
#         if website in data:
#             email=data[website]["email"]
#             password=data[website]["password"]
#             messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
#             pass_inp.insert(0,password)
#             # email_inp.insert(0,email)
#         else:  # Handle the case where the website is not found in the data
#             messagebox.showinfo(title="Error", message=f"No details for the {website} exist")
       
    
    

# # ---------------------------- UI SETUP ------------------------------- #
# window=Tk()
# window.title("Password Manager")
# window.config(padx=20, pady=20)

# # window.iconphoto(False, PhotoImage(file='logo.png'))


# canvas = Canvas(width=200, height=200, highlightthickness=1)
# # logo_img = PhotoImage(file=resource_path("tomato.png"))
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# # timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=0)


# #Website
# web_lab=Label(text="Website")
# web_lab.grid(column=0,row=1)

# web_inp=Entry(width=15)
# web_inp.grid(column=1,row=1,columnspan=2,sticky="EW")
# web_inp.focus()

# #search btn
# srch_btn=Button(text="Search",command=find_password)
# srch_btn.grid(column=2,row=1,sticky="EW")


# #email/username
# email_lab=Label(text="Email/Username")
# email_lab.grid(column=0,row=2,sticky="EW")

# email_inp=Entry(width=45)
# email_inp.grid(column=1,row=2,columnspan=2,sticky="EW")
# email_inp.insert(0,"kundlikadnan64@gmail.com")

# #pass
# pass_lab=Label(text="Password")
# pass_lab.grid(column=0,row=3,sticky="EW")

# pass_inp=Entry(width=10)
# pass_inp.grid(column=1,row=3,sticky="EW")

# pass_btn=Button(text="Generate Password",command=gen_pass)
# pass_btn.grid(column=2,row=3,sticky="EW")

# #addbtn
# add_btn=Button(text="Add",width=40,command=save)
# add_btn.grid(column=1,row=4,columnspan=2,sticky="EW")






# window.mainloop()

def find_password():
    website = web_inp.get()
    try:
        with open(resource_path("data.json")) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        print("err")
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pass_inp.insert(0, password)
        else:  # Handle the case where the website is not found in the data
            messagebox.showinfo(title="Error", message=f"No details for the {website} exist")

# Update the `save` function similarly to use `resource_path`
def save():
    website = web_inp.get()
    email = email_inp.get()
    password = pass_inp.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Retry", message="Please fill the required fields")
    else:
        try:
            with open(resource_path("data.json"), "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(resource_path("data.json"), "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(resource_path("data.json"), "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_inp.delete(0,END)
            pass_inp.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# window.iconphoto(False, PhotoImage(file=resource_path('logo.png')))

canvas = Canvas(width=200, height=200, highlightthickness=1)
logo_img = PhotoImage(file=resource_path("logo.png"))
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website
web_lab = Label(text="Website")
web_lab.grid(column=0, row=1)

web_inp = Entry(width=15)
web_inp.grid(column=1, row=1, columnspan=2, sticky="EW")
web_inp.focus()

# Search button
srch_btn = Button(text="Search", command=find_password)
srch_btn.grid(column=2, row=1, sticky="EW")

# Email/Username
email_lab = Label(text="Email/Username")
email_lab.grid(column=0, row=2, sticky="EW")

email_inp = Entry(width=45)
email_inp.grid(column=1, row=2, columnspan=2, sticky="EW")
email_inp.insert(0, "kundlikadnan64@gmail.com")

# Password
pass_lab = Label(text="Password")
pass_lab.grid(column=0, row=3, sticky="EW")

pass_inp = Entry(width=10)
pass_inp.grid(column=1, row=3, sticky="EW")

pass_btn = Button(text="Generate Password", command=gen_pass)
pass_btn.grid(column=2, row=3, sticky="EW")

# Add button
add_btn = Button(text="Add", width=40, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
