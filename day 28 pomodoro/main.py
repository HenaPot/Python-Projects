from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✅"
ticks = ""
reps = 0
timer_functionality = None

# ------------------------------ PAUSE MECHANISM ---------------------------#


def pause_timer():
    pass

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    start.config(state="normal")
    reset.config(state="disabled")

    global reps, ticks
    reps = 0

    try:
        window.after_cancel(timer_functionality)
    except ValueError:
        pass
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(fg=GREEN, text="Timer", font=(FONT_NAME, 50, "bold"), background=YELLOW)

    ticks = ""
    tick.config(text=ticks)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    def window_to_front():
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)

    global reps
    reps += 1

    start.config(state="disabled")
    reset.config(state="normal")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        window_to_front()
        timer.config(text="Break", foreground=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        window_to_front()
        timer.config(text="Break", foreground=PINK)
        countdown(short_break_sec)
    else:
        timer.config(text="Work", foreground=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    global ticks
    count_min = count // 60
    count_sec = count % 60

    # if count_sec < 10:
    if count_sec == 0 or len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_functionality
        timer_functionality = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            ticks += TICK
        tick.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Labels
timer = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 50, "bold"), background=YELLOW)
timer.grid(row=0, column=1)

tick = Label(text="", bg=YELLOW, fg="green", highlightthickness=0)
tick.grid(row=3, column=1)

# Buttons
start = Button(text="Start", width=10, command=start_timer, font=(FONT_NAME, 15, "bold"))
reset = Button(text="Reset", width=10, font=(FONT_NAME, 15, "bold"), command=reset_timer)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)

window.mainloop()