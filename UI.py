from tkinter import *
from Backend import *


class UI():

    def __init__(self):
        self.bgColor = 'DeepSkyBlue4'
        self.boxColor = 'gold4'
        self.window = Tk()
        self.window.title("Anima")
        self.window.geometry("720x600")
        self.window.configure(bg = self.bgColor)

        self.topFrame = Frame(self.window, relief = RIDGE, width = 100, height = 50, bg = self.bgColor)
        self.middleFrame = Frame(self.window, relief = RIDGE, bg = self.bgColor)
        self.bottomFrame = Frame(self.window, relief = RIDGE, cursor = "dot", bg = self.bgColor)

        self.locationInfoBar = Label(self.topFrame, text= "Welcome to the world of Anima", relief = RIDGE, padx = 10, pady = 10, width = 40, bg = self.boxColor)

        self.mobInfoBar = Label(self.middleFrame, text="", relief=RIDGE, padx=10, width=20, bg = self.boxColor)
        self.mobHealthBar = Label(self.middleFrame, text="Health: ", relief=RIDGE, padx=5, pady=3, width=20, bg = self.boxColor)
        self.mobAttackBar = Label(self.middleFrame, text="Attack: ", relief=RIDGE, padx=5, pady=3, width=20, bg = self.boxColor)
        self.mobDefenseBar = Label(self.middleFrame, text="Defense: ", relief=RIDGE, padx=5, pady=3, width=20, bg = self.boxColor)

        self.playerInfoBar = Label(self.bottomFrame, text= "", relief=RIDGE, padx=10, bg = self.boxColor)
        self.playerHealthBar = Label(self. bottomFrame, text ="Health: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width = 10, bg = self.boxColor)
        self.playerAttackBar = Label(self. bottomFrame, text ="Attack: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width = 10, bg = self.boxColor)
        self.playerDefenseBar = Label(self.bottomFrame, text="Defense: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width =10, bg = self.boxColor)

        self.inBox = Entry(self.bottomFrame, relief = RIDGE, bd = 2, bg = self.boxColor).grid(row = 1, column = 1)
        self.NewGameButton = Button(self.bottomFrame, text='New Game', command= initializeGame, relief = RIDGE, width = 10, bg = self.boxColor).grid(row = 1, column = 5)
        self.SaveButton = Button(self.bottomFrame, text ='Save', command=save, relief = RIDGE, width = 10, bg = self.boxColor).grid(row = 2, column = 5)
        self.LoadButton = Button(self.bottomFrame, text='Load', command= load, relief = RIDGE, width = 10, bg = self.boxColor).grid(row = 3, column = 5)

        self.locationInfoBar.grid(row = 0)

        self.mobInfoBar.grid(row=1)
        self.mobHealthBar.grid(row=2)
        self.mobAttackBar.grid(row=3)
        self.mobDefenseBar.grid(row=4)

        self.playerInfoBar.grid(row = 0, column = 1)
        self.playerHealthBar.grid(row = 1, column = 0)
        self.playerAttackBar.grid(row = 2, column = 0)
        self.playerDefenseBar.grid(row=3, column=0)

        self.topFrame.pack(side = TOP, pady = 10)
        self.middleFrame.pack()
        self.bottomFrame.pack(side = BOTTOM)

        self.window.mainloop()

    def updateLocationInfoBar(self, newText = 'null'):
        self.locationInfoBar.configure(text  = newText)

    def updatePlayerInfoBar(self, newText = 'null'):
        self.playerInfoBar.configure(text  = newText)

    def updatePlayerHealthBar(self, current = 0, max = 20):
        self.playerHealthBar.configure(text ="Health: {}/{} ".format(current, max))

    def updatePlayerDefenseBar(self, current = 0):
        self.playerDefenseBar.configure(text ="Defense: {}".format(current))

    def updatePlayerAttackBar(self, current = 0 ):
        self.playerAttackBar.configure(text ="Attack: {}".format(current))

    def updateMobInfoBar(self, newText = 'null'):
        self.mobInfoBar.configure(text  = newText)

    def updateMobrHealthBar(self, current=0, max=20):
        self.MobHealthBar.configure(text="Health: {}/{} ".format(current, max))

    def updatePlayerDefenseBar(self, current=0):
        self.MobDefenseBar.configure(text="Defense: {}".format(current))

    def updatePlayerAttackBar(self, current=0):
        self.MobAttackBar.configure(text="Attack: {}".format(current))

