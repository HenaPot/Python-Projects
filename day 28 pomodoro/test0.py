import tkinter

window = tkinter.Tk()

my_button = tkinter.Button(text="Tinki vinki")
my_button.pack()

print(my_button.cget("text"))

window.mainloop()
