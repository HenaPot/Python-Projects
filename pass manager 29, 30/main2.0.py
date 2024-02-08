import tkinter
from tkinter import messagebox
import random
import pyperclip
from datetime import date
import json


MY_FONT = ("Arial", 13, "bold")
EMAIL = 'potogijahena@gmail.com'
reps = 0
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = random_letters + random_symbols + random_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    global reps
    reps += 1

    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()

    today = date.today()
    date_variable = today.strftime("%d/%m/%Y")

    new_data = {
        website: {
            "username": username,
            "password": password,
            "date": date_variable
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:

        try:
            with open('data.json', "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data
            data.update(new_data)

            with open('data.json', "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

            website_entry.focus()
            pyperclip.copy(password)


# ------------------------- FIND PASSWORD ----------------------------- #

def find_password():
    website = website_entry.get().title()
    try:
        with open('data.json', "r") as file:
            # reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="FileNotFoundError. Configure file path.")
        # you could just put all of this into one try-except statement to avoid returning
        return
    try:
        dictionary = data[website]
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No data for website called {website}.")
    else:
        password = dictionary["password"]
        username = dictionary["username"]
        messagebox.showinfo(title=f"{website} Data", message=f"username: {username}\n\n"
                                                             f"password: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("My Password Manager")
width = 700
height = 500
window.geometry(f"{width}x{height}")

# Canvas
my_canvas = tkinter.Canvas(width=200, height=200)
my_canvas.configure()
my_image = tkinter.PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=my_image)
my_canvas.grid(row=1, column=2, padx=50, pady=25)

# Labels
website_label = tkinter.Label(highlightthickness=0, text="Website:", font=MY_FONT)
website_label.grid(row=2, column=1, padx=60)

username_label = tkinter.Label(highlightthickness=0, text="Email/Username:", font=MY_FONT)
username_label.grid(row=3, column=1, padx=20)

password_label = tkinter.Label(highlightthickness=0, text="Password:", font=MY_FONT)
password_label.grid(row=4, column=1, padx=50)

# Entries
website_entry = tkinter.Entry(width=35, font=MY_FONT)
website_entry.focus()
website_entry.grid(row=2, column=2, pady=6)

v = tkinter.StringVar()
v.set(EMAIL)
username_entry = tkinter.Entry(width=35, font=MY_FONT, textvariable=v)
username_entry.grid(row=3, column=2, pady=6)

password_entry = tkinter.Entry(width=35, font=MY_FONT)
password_entry.grid(row=4, column=2, pady=6, padx=15)

# Buttons
generate_button = tkinter.Button(width=10, font=MY_FONT, text="Generate", command=generate_password)
generate_button.grid(row=4, column=3, pady=6, padx=10)

add = tkinter.Button(width=20, font=MY_FONT, text="ADD", bg="#C04000", fg="white", command=save)
add.grid(row=5, column=2, pady=6)

search_button = tkinter.Button(width=10, font=MY_FONT, text="Search", command=find_password)
search_button.grid(row=2, column=3, padx=10, pady=6)

window.mainloop()

# Note: In case user types in a website that already exists in the json file,
# it overrides the json entry --> IT CHANCES THE PASSWORD
# resolve this with a yes/cancel messagebox
