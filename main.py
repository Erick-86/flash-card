from tkinter import *

root = Tk()
BACKGROUND_COLOR = "#B1DDC6"

root.title("Flash Card")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# CARDS
# Front card
front_card = PhotoImage(file="./images/card_front.png")

# Back card
back_card = PhotoImage(file="./images/card_back.png")

card = canvas.create_image(400, 263, image=back_card)

# Tracking which card is active/showing
active_card = True

def toggle_cards():
    global active_card

    if active_card:
        canvas.itemconfig(card, image=back_card)
    else:
        canvas.itemconfig(card, image=front_card)

    active_card = not active_card

    root.after(3000, toggle_cards)

root.after(3000, toggle_cards)

#  BUTTONS
# Cancel Btns
cancel_btn_icon = PhotoImage(file="./images/wrong.png")
cancel_btn = Button(
    image=cancel_btn_icon,
    highlightthickness=0,
    borderwidth=0
)
cancel_btn.grid(row=1, column=0)

# Correct Btns
correct_btn_icon = PhotoImage(file="./images/right.png")
correct_btn = Button(
    image=correct_btn_icon,
    highlightthickness=0,
    borderwidth=0
)
correct_btn.grid(row=1, column=1)

root.mainloop()