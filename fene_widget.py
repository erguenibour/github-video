import tkinter

app = tkinter.Tk()
#label_welcome =tkinter.Label(app, text="Bienvenu a tous ! c'est la formationvideo")
#label_welcome.pack()
#entry_name = tkinter.Entry(app)
#entry_name.pack()
def hello():
    print("Hello sur le terminal")
button_quit = tkinter.Button(app, text="ok",command=hello)
button_quit.pack()
app.mainloop()