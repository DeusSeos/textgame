from tkinter import *
from Backend import *


class UI():

    def __init__(self):
        self.window = Tk()
        self.window.title("Anima")
        self.window.geometry("720x900")

        self.infoText = StringVar()
        self.infoText.set("Welcome to the world of Anima")


        self.topFrame = Frame(self.window).pack()
        self.bottomFrame = Frame(self.window).pack(side='bottom')

        self.infoBar = Label(self.topFrame, text= "Welcome to the world of Anima")

        self.SaveButton = Button(self.bottomFrame, text ='Save', command=save())
        self.UpdateButton = Button(self.bottomFrame, text='Update', command= self.updateInfoBar)
        # self.Attack = Button()
        # self.Heal = Button()
        # self.PickUp = Button()
        # self.Interact = Button()
        #
        self.SaveButton.pack()
        self.UpdateButton.pack()
        self.infoBar.pack()

        self.window.mainloop()



    def updateInfoBar(self):
        self.infoBar.configure(text  = "Ree")



root = UI()
