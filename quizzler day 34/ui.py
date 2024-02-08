from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = "Arial 20 italic"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("400x550")
        self.window.config(background=THEME_COLOR)

        self.canvas = Canvas(height=300, width=350, background="white", borderwidth=0)
        self.question_text = self.canvas.create_text(
            175,
            150,
            width=315,
            text="Placeholder",
            fill=THEME_COLOR,
            font=FONT,
        )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20, padx=20)

        self.score = Label(text="Score: 0", background=THEME_COLOR, foreground="white", font=FONT)
        self.score.grid(row=1, column=2, pady=(10, 0))

        green_image = PhotoImage(file="images/true.png")
        self.green_button = Button(image=green_image, highlightthickness=0, command=self.true)
        self.green_button.grid(row=3, column=1, pady=(15, 0))

        red_image = PhotoImage(file="images/false.png")
        self.red_button = Button(image=red_image, highlightthickness=0, command=self.false)
        self.red_button.grid(row=3, column=2, pady=(15, 0))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white", highlightbackground="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(background="green", highlightbackground="green")
        else:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(background="red", highlightbackground="red")
        self.window.after(1000, func=self.get_next_question)