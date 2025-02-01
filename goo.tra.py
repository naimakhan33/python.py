from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

def change(text, src, dest):
    return GoogleTranslator(source=src, target=dest).translate(text)

def data():
    s = comb_Sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Pink')

lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg="Pink")
lab_txt.place(x=100, y=40, height=50, width=300)

lab_source = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="black", bg="Pink")
lab_source.place(x=100, y=100, height=30, width=300)

Sor_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=140, height=150, width=480)

languages = GoogleTranslator().get_supported_languages()

comb_Sor = ttk.Combobox(root, value=languages)
comb_Sor.place(x=10, y=300, height=40, width=150)
comb_Sor.set("english")

button_change = Button(root, text="Translate", relief=RAISED, command=data)
button_change.place(x=180, y=300, height=40, width=150)

comb_dest = ttk.Combobox(root, value=languages)
comb_dest.place(x=340, y=300, height=40, width=150)
comb_dest.set("urdu")

lab_dest = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), fg="black", bg="pink")
lab_dest.place(x=100, y=360, height=30, width=300)

dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()




