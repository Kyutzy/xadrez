import tkinter as tk

root = tk.Tk()
root.title("Hello World")
root.geometry("300x200")

# create a text box
text_box = tk.Text(root, height=8, width=30)
text_box.pack()
# get the text from the text box
texto = text_box.get("1.0", "end-1c")

botao = tk.Button(root, command=lambda: exec(text_box.get("1.0", "end-1c")), text="Clique aqui")
botao.pack()
root.mainloop()