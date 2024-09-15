import tkinter as tk
def show_text():
    user_text = entry.get()
    text_box.insert(tk.END, user_text + "\n")
    from tkinter import messagebox
    tk.messagebox.showinfo("Title", "This is a message")

window = tk.Tk()
window.title("Tkinter Widgets Example")
# Label
label = tk.Label(window, text="Enter some text:")
label.pack()
# Entry allows single line
entry = tk.Entry(window)
entry.pack()
# Button
button = tk.Button(window, text="Show Text", command=show_text)
button.pack()
# Text allows multi line
text_box = tk.Text(window, height=5, width=40)
text_box.pack()

listbox = tk.Listbox(window)
listbox.pack()
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")

checkbutton = tk.Checkbutton(window, text="Option 1")
checkbutton.pack()

radiobutton = tk.Radiobutton(window, text="Option 1", value=1)
radiobutton.pack()

menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open")
menubar.add_cascade(label="File", menu=file_menu)
window.config(menu=menubar)

window.mainloop()
