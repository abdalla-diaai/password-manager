from tkinter import *
inserted_text = []
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("passwords.txt", "a") as file:
        file.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()} \n")
    website_entry.delete(first=0, last=END)
    username_entry.delete(first=0, last=END)
    password_entry.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", anchor="w")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
# to have cursor on the first entry
website_entry.focus()
username_label = Label(text="Email/Username:", anchor="w")
username_label.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
# to pre-populate user name or email
username_entry.insert(0, "abdalla.diaai@outlook.com")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
