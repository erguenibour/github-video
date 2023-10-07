import tkinter
from tkinter import messagebox
"""
StringVar() : chaine de charatère
IntVar() : nombre entier
DoubleVar() : nombre flotant
BooleanVar() : boolean[bool]
"""
#Fonction observateur
#def update_label(*args):
 #   var_label.set(var_entry.get())
def update_observer(*args):
    if var_gender.get():
        var_label_gender.set("c'est un homme")
    else:
        var_label_gender.set("c'est une femme")    
app = tkinter.Tk()
app.geometry("400x300")
app.title("variables tkinter")
#var_entry= tkinter.StringVar()
#var_entry.trace("w", update_label)
#entry =tkinter.Entry(app, textvariable=var_entry)
#var_label = tkinter.StringVar()
#label = tkinter.Label(app, textvariable= var_label)

#entry.pack()
#label.pack()
var_gender = tkinter.IntVar()
var_gender.trace("w", update_observer)
radio1= tkinter.Radiobutton(app, text="Homme", value=1, variable=var_gender)
radio2= tkinter.Radiobutton(app, text="Fomme", value=0, variable=var_gender)
var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable=var_label_gender)

radio1.pack()
radio2.pack()
label_gender.pack()
app.mainloop()