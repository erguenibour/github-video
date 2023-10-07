import tkinter
from tkinter import messagebox
app = tkinter.Tk()
#check_widget = tkinter.Checkbutton(app, text="publier?", offvalue=2, onvalue=5)
#radio_widget1 = tkinter.Radiobutton(app, text="Homme", value=1)
#radio_widget2 =tkinter.Radiobutton(app, text="Femme", value=0)
#check_widget.pack()
#radio_widget1.pack()
#radio_widget2.pack()

#scale_w = tkinter.Scale(app, from_=10, to=100)
#spin_w = tkinter.Spinbox(app, from_=1, to=10)
#spin_w.pack()
#scale_w.pack()  

#lb=tkinter.Listbox(app) 
#lb.insert(1,"window") 
#lb.insert(2,"ubuntu") 
#lb.insert(3,"debian")
#lb.pack() 
"""
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
asktrycancel
"""
def show_model_window():
    messagebox.askretrycancel("ERROR", "un problème est survenu")

btn=tkinter.Button(app, text="Déclanche une erreur", command=show_model_window)
btn.pack()    




app.mainloop()