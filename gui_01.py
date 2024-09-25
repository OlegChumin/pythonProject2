import tkinter as tk

is_hello = True
is_text_color = True


def change_text():
    global is_hello
    if is_hello:
        window_text.config(text="Привет Мир!")
    else:
        window_text.config(text="Hello, World!")
    is_hello = not is_hello

def change_color():
    global is_text_color
    if is_text_color:
        window_text.config(fg="lime", bg="black")
    else:
        window_text.config(fg="white", bg="blue")
    is_text_color = not is_text_color

def change_bg_color():
    global current_color
    if current_color == "lightblue":
        root.configure(bg="lightgreen")
        current_color = "lightgreen"
    else:
        root.configure(bg="lightblue")
        current_color = "lightblue"

root = tk.Tk()
root.title("Текст в окне")
root.geometry("600x400")

current_color = "lightblue"
root.configure(bg="lightblue")


window_text = tk.Label(root, text="Hello, World!", font=("Arial", 20), fg="white", bg="blue")
# window_text.pack(pady=40)
window_text.grid(row=0, column=0, padx=10, pady=40)

button_1 = tk.Button(root, text="Press me!", command=change_text)
button_1.grid(row=1, column=0, padx=10, pady=20)

# button_1.pack(pady=20)
# button.place(pady=20)
# button.grid(pady=20)

button_2 = tk.Button(root, text="Change bg color", command=change_bg_color)
button_2.grid(row=2, column=1, padx=10, pady=20)

button_3 = tk.Button(root, text="Change text color", command=change_color)
button_3.grid(row=3, column=2, padx=10, pady=20)


root.resizable(False, False)
root.mainloop()
