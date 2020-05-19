import tkinter as tk
from Backend import *


class UI():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Anima")
        self.window.geometry("720x900")

        self.infoText = tk.StringVar()
        self.infoText.set("Welcome to the world of Anima")


        # self.topFrame = Frame(self.window).pack()
        # self.bottomFrame = Frame(self.window).pack(side='bottom')

        self.infoBar = tk.Button(self.window, text= "Welcome to the world of Anima")

        self.SaveButton = tk.Button(self.window, text ='Save', command=save())
        self.UpdateButton = tk.Button(self.window, text='Update', command= self.updateInfoBar)
        # self.Attack = Button()
        # self.Heal = Button()
        # self.PickUp = Button()
        # self.Interact = Button()

        self.SaveButton.pack(side = tk.LEFT)
        self.UpdateButton.pack(side = tk.RIGHT)
        self.infoBar.pack()

        self.window.mainloop()



    def updateInfoBar(self):
        self.infoBar.configure(text  = "Ree")



root = UI()
