import string
from random import randint, choice
from tkinter import *


def generate_password():
    password_min = 7
    password_max = 14
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# window config
window = Tk()
window.title("Generator Of Password ")
window.geometry("330x480")
window.iconbitmap("logo_d.ico")
window.config(background='#4065A4')

# create the frame
frame: Frame = Frame(window, bg='#4065A4')

# create the image
width = 300
height = 300
image = PhotoImage(file='computer.png').zoom(35).subsample(32)
canvas = Canvas(window, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# sub box
right_frame = Frame(frame, bg='#4065A4')

# create title
label_title = Label(right_frame, text='Password', font=("Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

# create an input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

# create the button
generate_password_button = Button(right_frame, text="Generate", font=("Helvetica", 20), bg='#4065A4', command=generate_password)
generate_password_button.pack(fill=X)

# place the sub box right the frame
right_frame.grid(row=0, column=1, sticky=W)


# create menu bar
menu_bar = Menu(window)
# create first menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=generate_password)
file_menu.add_command(label="Quit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# config window to add the menu bar
window.config(menu=menu_bar)

# show the frame
frame.grid()
# problem here why i can`t use
# frame.pack(expands=YES)

# launch the window
window.mainloop()
