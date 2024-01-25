from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD FINDER ---------------------------------- #
def find_password():
    website = web_entry.get().lower()
    try:
        with open("data.json", "r") as d:
            data = json.load(d)
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Email and Password", message=f"Email: {email}\n"
                                                                    f"Password: {password}")
        else:
            messagebox.showinfo(title="Not Found", message="No details for this website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    gen_password = [choice(letters) for _ in range(randint(8, 10))]
    gen_password += [choice(symbols) for _ in range(randint(2, 4))]
    gen_password += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(gen_password)
    gen_password = "".join(gen_password)
    pass_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = web_entry.get().lower()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        },
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Empty Fields", message="You left some field empty.")

    else:
        try:
            with open("data.json", "r") as d:
                # reading old data
                data = json.load(d)
        except FileNotFoundError:
            with open("data.json", "w") as d:
                json.dump(new_data, d, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as d:
                # saving updated data
                json.dump(data, d, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

web_entry = Entry(width=21, highlightcolor="blue")
web_entry.grid(row=1, column=1)
web_entry.focus()

# search button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

# email
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=40, highlightcolor="blue")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "thakurfalswaroop@gmail.com")

# password
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=21, highlightcolor="blue")
pass_entry.grid(row=3, column=1)

# Generate password Button
gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)

# add Button
add_button = Button(text="Add", width=34, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

# ----------------------- Created by Anuj Thakur ----------------------- #
