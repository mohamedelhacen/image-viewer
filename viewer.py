import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import glob

root = tk.Tk()
root.title('Image Viewer')
root.iconbitmap('cartoons/sample.jpg')
root.geometry("720x800")

images_list = []

def open():
    global images_list
    global label
    root.filename = filedialog.askopenfilenames(initialdir='', title='Select a folder or image',
                                                filetypes=(('PNG files', ['*.png', '*.PNG']), ('JPEG files', ['*.jpg', '*.jpeg'])))
    for image_file in root.filename:
        image = Image.open(image_file)
        image = image.resize((720, 720))
        image = ImageTk.PhotoImage(image)
        images_list.append(image)

    label = tk.Label(root, image=images_list[0])
    label.grid(row=0, column=0, columnspan=4)

    button_forward = create_button('next', lambda: forward(2))
    button_exit = create_button('Exit', root.quit)
    button_add = create_button('Add more', command=open)
    button_back = create_button('back', state='disabled')

    button_forward.grid(row=1, column=3)
    button_exit.grid(row=1, column=1)
    button_back.grid(row=1, column=0)
    button_add.grid(row=1, column=2)


def create_button(text, command=None, state='active'):
    return tk.Button(root, text=text, command=command, state=state, padx=10, pady=5)


def forward(image_number):
    global label
    global  button_forward
    global button_back
    global button_add

    label.grid_forget()
    label = tk.Label(root, image=images_list[image_number-1])
    button_forward = create_button('next', lambda: forward(image_number+1))
    button_add = create_button('Add more', command=open)
    button_back = create_button('back', lambda: back(image_number-1))

    if image_number == len(images_list):
        button_forward = create_button('next', state='disabled')

    grid()


def back(image_number):
    global label
    global  button_forward
    global button_back
    global button_add

    label.grid_forget()
    label = tk.Label(root, image=images_list[image_number-1])
    button_forward = create_button('next', lambda: forward(image_number+1))
    button_add = create_button('Add more', command=open)
    button_back = create_button('back', lambda: back(image_number-1))

    if image_number == 1:
        button_back = create_button('back', state='disabled')

    grid()


def grid():
    label.grid(row=0, column=0, columnspan=4)
    button_forward.grid(row=1, column=3)
    button_back.grid(row=1, column=0)
    button_add.grid(row=1, column=2)


btt = create_button('Add folder', command=open)
btt.grid(row=0, column=1)

root.mainloop()
