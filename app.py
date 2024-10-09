import tkinter as tk
from tkinter import messagebox
import requests
import json

URL = 'http://127.0.0.1:8000/'

def login():
    global token_out
    email = username_entry.get()
    password = password_entry.get()
    print(email, password)
    if email == '' or password == '':
        messagebox.showerror(
            'Required Field', 'Email/Password is Required'
        )
    
    else:
        data = {
            "email": email,
            "password": password
        }
        try:
            response = requests.post(URL+'api/auth/token/', data=data)
            # print(response.text)
            response_dict = json.loads(response.text)
            # print(response_dict)
            token_out = response_dict['access']
            print(token_out)
        
        except Exception as e:
            messagebox.showerror(
                'Login Failed', 'Login Failed'
            )
        # retrieve_contacts()
            

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=login)
login_button.pack()


listbox = tk.Listbox(parent, height = 10, 
                  width = 15, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")
 

 
# Define a label for the list.  
label = tk.Label(parent, text = " MY CONTACTS")  
# pack the widgets
label.pack()
listbox.pack()
 
 
 

# Start the Tkinter event loop
parent.mainloop()