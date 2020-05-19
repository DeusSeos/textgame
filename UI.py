from tkinter import *
from Backend import *


class UI():

    def __init__(self):
        self.window = Tk()
        self.window.title("Anima")
        self.window.geometry("720x600")

        self.topFrame = Frame(self.window, relief = RIDGE)
        self.middleFrame = Frame(self.window, relief = RIDGE)
        self.bottomFrame = Frame(self.window, relief = RIDGE, cursor = "dot")

        self.image = Label(self.middleFrame, text="Welcome to the world of Anima", relief=RIDGE, padx=10)

        self.infoBar = Label(self.topFrame, text= "Welcome to the world of Anima", relief = RIDGE, padx = 10)

        self.playerHealthBar = Label(self. bottomFrame, text ="Health: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width = 10)
        self.playerAttackBar = Label(self. bottomFrame, text ="Attack: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width = 10)
        self.playerDefenseBar = Label(self.bottomFrame, text="Defense: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width =10)

        self.mobHealthBar = Label(self.middleFrame, text="Health: ", relief=RIDGE, padx=5, pady=3, anchor=W, width=10)
        self.mobAttackBar = Label(self.middleFrame, text="Attack: ", relief=RIDGE, padx=5, pady=3, anchor=W, width=10)
        self.mobDefenseBar = Label(self.middleFrame, text="Defense: ", relief=RIDGE, padx=5, pady=3, anchor=W, width=10)

        self.inBox = Entry(self.bottomFrame).grid(row = 1, column = 1)

        self.SaveButton = Button(self.bottomFrame, text ='Save', command=save(), relief = RIDGE, width = 10).grid(row = 2, column = 5)
        self.UpdateButton = Button(self.bottomFrame, text='Update', command= self.updateHealthBar(10, 20), relief = RIDGE, width = 10).grid(row = 1, column = 5)

        self.mobHealthBar.grid(row=0, column=0)
        self.mobAttackBar.grid(row=1, column=0)
        self.mobDefenseBar.grid(row=2, column=0)

        self.playerHealthBar.grid(row = 0, column = 0)
        self.playerAttackBar.grid(row = 1, column = 0)
        self.playerDefenseBar.grid(row=2, column=0)


        self.infoBar.pack()
        self.image.pack()



        self.topFrame.pack(side = TOP)
        self.middleFrame.pack()
        self.bottomFrame.pack(side = BOTTOM)

        self.window.mainloop()


    def updateInfoBar(self, newText = 'null'):
        self.infoBar.configure(text  = newText)

    def updateHealthBar(self, current, max ):
        self.playerHealthBar.configure(text ="Health: {}/{} ".format(current, max))

    def updateDefensebar(self, current):
        self.playerDefenseBar.configure(text ="Defense: {}".format(current))

    def updateAttackbar(self, current):
        self.playerAttackBar.configure(text ="Attack: {}".format(current))




root = UI()
