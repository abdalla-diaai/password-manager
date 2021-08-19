from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ERROR", message="Please don't leave any fields empty!")
    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"Email: {username} \nPassword: {password} "
    #                                                           f"\nDo you want to save these details?")
    #     if is_ok:
    #         with open("passwords.txt", "a") as file:
    #             file.write(f"{website} | {username} | {password} \n")
    #         website_entry.delete(first=0, last=END)
    #         username_entry.delete(first=0, last=END)
    #         password_entry.delete(first=0, last=END)
    else:
        try:
            with open("data.json", "r") as data_file:
                # read old data
                data = json.load(data_file)
                # update the data with new data

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # write the new entry in the file
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # write the new entry in the file
                json.dump(data, data_file, indent=4)

        website_entry.delete(first=0, last=END)
        username_entry.delete(first=0, last=END)
        password_entry.delete(first=0, last=END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("data.json", "r") as data_file:
            # read old data
            data = json.load(data_file)
            website = website_entry.get()

            if website.lower() in data.keys():
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {email} \nPassword: {password}")
            else:
                messagebox.showinfo(title="ERROR", message="No Details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:", anchor="w")
website_label.grid(row=1, column=0)
# to have cursor on the first entry
username_label = Label(text="Email/Username:", anchor="w")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
# to pre-populate user name or email
username_entry.insert(0, "abdalla.diaai@outlook.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# buttons
search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
