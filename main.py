from tkinter import *
import random
import time
from tkinter import messagebox

start_time = None
dex = None

typing_test_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "In the end, we only regret the chances we didn’t take.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Success is not the key to happiness, happiness is the key to success.",
    "The early bird catches the worm.",
    "Better late than never.",
    "Actions speak louder than words.",
    "Knowledge is power.",
    "A picture is worth a thousand words.",
    "Time and tide wait for no man.",
    "When the going gets tough, the tough get going.",
    "Every cloud has a silver lining.",
    "Fortune favors the bold.",
    "Practice makes perfect.",
    "The pen is mightier than the sword.",
    "Honesty is the best policy.",
    "A watched pot never boils.",
    "You can’t judge a book by its cover.",
    "Absence makes the heart grow fonder.",
    "An apple a day keeps the doctor away.",
    "Curiosity killed the cat.",
    "Do unto others as you would have them do unto you.",
    "Don't count your chickens before they hatch.",
    "The grass is always greener on the other side.",
    "Haste makes waste.",
    "It takes two to tango."
]


def kickoff():
    global start_time, dex
    # Select a random sentence from the list
    random_sentence = random.choice(typing_test_sentences)

    # get random sentence index
    dex = typing_test_sentences.index(random_sentence)

    # config Label with new arguments
    word_label.config(text=random_sentence, font=('Arial', 12, 'bold'), wraplength=250)

    # delete any text in field when button is clicked and focus
    textarea.delete(1.0, END)
    textarea.focus()

    start_time = time.time()


# calculate typing speed
def calculate_speed(event):
    # check start_timer is set
    if start_time is not None:
        end_time = time.time()
        time_taken = end_time - start_time

    # get text entered

    typed_text = textarea.get(0.0, END)
    word = typing_test_sentences[dex]

    # check if typed word is same as random sentence and put out a message for GUI User

    if not typed_text == word:
        word_count = len(word.split())
        wpm = (word_count / time_taken) * 60
        messagebox.showinfo("Speed Test Result", f"Your typing speed is {wpm:.2f} words per minute.")
    else:
        messagebox.showerror("Speed Test Result", "Text does not match. Please try again.")


#_____________________________________GUI_______________________

# create and config window
window = Tk()
window.title('Typing Speed')
window.minsize(width=500, height=500)
window.config(pady=25, padx=20)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# create banner using canvas widget
canva = Canvas(width=500, height=100, bg='black', )
img = PhotoImage(file='TEST.png')
crtimg = canva.create_image(250, 50, image=img)
canva.grid(column=1, row=0)

# empty label to add to layout
time2 = Label(pady=50)
time2.grid(column=0, row=1, )

word_label = Label(text='')
word_label.grid(column=1, row=1)

textarea = Text(width=50, height=5, font=("Arial", 13))
textarea.bind("<Return>", calculate_speed)
textarea.grid(column=1, row=2)

time2 = Label(pady=20)
time2.grid(column=1, row=3, )

startbtn = Button(text='Start', width=10, height=2, highlightthickness=0, command=kickoff)
startbtn.grid(column=1, row=4, )

# keep the window open
window.mainloop()
