import tkinter
from tkinter import messagebox
import random
import pyperclip
from datetime import date


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

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    today = date.today()
    date_variable = today.strftime("%d/%m/%Y")

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open('data.txt', "a") as file:
                file.seek(0, 0)
                file.write(f"{website} | {username} | {password} | {date_variable}\n")

                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)

            website_entry.focus()
            pyperclip.copy(password)


def rearrange_backwards():
    global reps
    reps += 1

    # DO NOT CHANGE THIS PART OF CODE --> IF REPS = 1 IT DELETES THE CONTENT OF THE FILE WITH ALL THE PASSWORDS
    if reps == 1:
        return

    with open('data.txt', "r") as file:
        # you read through last 3 appended lines and reverse them
        polished_file = file.readlines()[-1:-reps:-1]

        # MUST PUT CURSOR ON BEGINNING AGAIN
        file.seek(0, 0)

        # you get the difference between lastly added lines and the ones that are already reversed above
        beginning = file.readlines()[0:(len(file.readlines())-(reps-1))]

    with open('data.txt', "w") as file:
        for line in polished_file:
            file.write(line)

    with open('data.txt', "a") as file:
        for line in beginning:
            file.write(line)


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
password_entry.grid(row=4, column=2, pady=6)

# Buttons
generate_button = tkinter.Button(width=10, font=MY_FONT, text="Generate", command=generate_password)
generate_button.grid(row=4, column=4, pady=6, padx=10)

add = tkinter.Button(width=20, font=MY_FONT, text="ADD", bg="#C04000", fg="white", command=save)
add.grid(row=5, column=2, pady=6)


window.mainloop()
rearrange_backwards()
