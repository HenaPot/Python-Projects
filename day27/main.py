import tkinter


def button_clicked():
    try:
        miles_to_km = round(int(entry_variable.get()) * 1.609344, 2)
        if miles_to_km == "":
            variable_label.config(text="0")
            variable_label.grid(row=3, column=9)
        else:
            variable_label.config(text=miles_to_km)
            variable_label.grid(row=3, column=9)
    except ValueError:
        pass


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=150, width=300)

# Entry
entry_variable = tkinter.Entry(width=10)
entry_variable.insert(tkinter.END, string="type here")
entry_variable.focus()
entry_variable.grid(row=2, column=9, padx=10)

# Labels
text_label0 = tkinter.Label(text="Miles")
text_label0.grid(row=2, column=10, pady=10)
text_label1 = tkinter.Label(text="is equal to", padx=20)
text_label1.grid(row=3, column=7)
text_label2 = tkinter.Label(text="Km")
text_label2.grid(row=3, column=10)

variable_label = tkinter.Label(text="0")
variable_label.grid(row=3, column=9, pady=10)

# Buttons
my_button = tkinter.Button(text="Convert", command=button_clicked)
my_button.grid(row=4, column=9)



# entry_variable = tkinter.Entry(window, width=10)
# entry_variable.pack()

window.mainloop()
