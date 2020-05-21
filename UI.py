from tkinter import *
from Backend import *
from FrontEnd import *


class UI():
    def __init__(self):
        self.backend = Backend()
        self.person = self.backend.getPerson()
        self.currentLocation = self.backend.getCurrentLocation()
        self.currentMob = self.backend.getCurrentMob()
        self.bgColor = "RoyalBlue4" #"cyan4" #'DeepSkyBlue4'
        self.boxColor = 'gold3'
        self.window = Tk()
        self.window.title("Anima")
        self.window.geometry("720x600")
        self.window.configure(bg = self.bgColor)
        # self.input = StringVar()

        self.topFrame = Frame(self.window, relief = RIDGE, width = 100, height = 50, bg = self.bgColor)
        self.middleFrame = Frame(self.window, relief = RIDGE, bg = self.bgColor)
        self.bottomFrame = Frame(self.window, relief = RIDGE, cursor = "dot", bg = self.bgColor)

        self.locationInfoBar = Label(self.topFrame, text= "Welcome to the World of Anima", relief = RIDGE, padx = 10, pady = 10, width = 40, bg = self.boxColor)

        self.actionInfobar = Label(self.topFrame, text = "The world is filled with monsters. Vanquish evil from this World.\n Hit New Game or Load to start",  relief = RIDGE, padx = 10, pady = 10, width = 50, bg = self.boxColor)

        self.mobInfoBar = Label(self.middleFrame, text="", relief= RIDGE, padx=10, width=20, bg = self.boxColor)
        self.mobHealthBar = Label(self.middleFrame, text="Health: ", relief=RIDGE, padx=5, pady=3, width=20, bg = self.boxColor)
        self.mobAttackBar = Label(self.middleFrame, text="Attack: ", relief=RIDGE, padx=5, pady=3, width=20, bg = self.boxColor)
        self.mobDefenseBar = Label(self.middleFrame, text="Defense: ", relief=RIDGE, padx=5, pady=3, width=20, bg = self.boxColor)

        self.playerInfoBar = Label(self.bottomFrame, text= "", relief=RIDGE, padx=5, pady = 3, width = 16, bg = self.boxColor)
        self.playerHealthBar = Label(self. bottomFrame, text ="Health: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width = 16,bd = 3,  bg = self.boxColor)
        self.playerAttackBar = Label(self. bottomFrame, text ="Attack: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width = 16,bd = 3,  bg = self.boxColor)
        self.playerDefenseBar = Label(self.bottomFrame, text="Defense: ", relief = RIDGE, padx = 5, pady = 3, anchor = W, width =16, bd = 3,  bg = self.boxColor)

        self.MoveButton = Button(self.bottomFrame, text = "Next City", command = lambda :[self.backend.moveTo(), self.UIRefresh()] , relief = RIDGE, bd = 3, bg = self.boxColor, width = 16).grid(row = 1, column = 1)
        self.AttackButton = Button(self.bottomFrame, text='Attack', command=lambda:[FrontEnd.attackSequence(self, self.person, self.currentMob, self.currentLocation, self.backend), self.UIRefresh()], relief = RIDGE, width = 16, bd= 3, bg = self.boxColor).grid(row = 3, column = 1)
        self.HealButton = Button(self.bottomFrame, text='Heal', command=lambda :[FrontEnd.healSequence(self, self.person, self.currentMob), self.updatePlayerHealthBar()], relief=RIDGE, width=16, bd = 3, bg=self.boxColor).grid(row=2, column=1)

        self.NewGameButton = Button(self.bottomFrame, text='New Game', command= lambda:[FrontEnd.newGame(self, self.backend), self.UIRefresh()], relief = RIDGE, width = 16, bd = 3, bg = self.boxColor).grid(row = 1, column = 5)
        self.SaveButton = Button(self.bottomFrame, text ='Save', command= self.backend.save, relief = RIDGE, width = 16, bd =3,  bg = self.boxColor).grid(row = 2, column = 5)
        self.LoadButton = Button(self.bottomFrame, text='Load', command=lambda:[self.backend.load(), self.UIRefresh()], relief = RIDGE, width = 16, bd =3 , bg = self.boxColor).grid(row = 3, column = 5)

        self.locationInfoBar.grid(row = 0)
        self.actionInfobar.grid(row = 1)

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


    def updateActionInfoBar(self, message = 'null'):
        if message == 'null':
            message = self.backend.currentPerson.getName()
            self.actionInfobar.configure(text = "{} is loitering around.".format(message))
        self.actionInfobar.configure(text = message)
        return None

    def updateLocationInfoBar(self, message = 'null'):
        if message == 'null':
            message = self.backend.getCurrentLocation().getWelcomeMessage()
        self.locationInfoBar.configure(text  = message)
        return None

    def updatePlayerInfoBar(self, message = 'null'):
        if message == 'null':
            message = self.backend.currentPerson.getName()
        self.playerInfoBar.configure(text  = message)
        return None

    def updatePlayerHealthBar(self):
        health = self.backend.currentPerson.getHealth()
        self.playerHealthBar.configure(text ="Health: {:5.2f} ".format(health))
        return None

    def updatePlayerDefenseBar(self):
        defense = self.backend.currentPerson.getDefense()
        self.playerDefenseBar.configure(text ="Defense: {}".format(defense))

    def updatePlayerAttackBar(self):
        attack = self.backend.currentPerson.getAttack()
        self.playerAttackBar.configure(text ="Attack: {}".format(attack))

    def updateMobInfoBar(self, message = 'null'):
        if message == 'null':
            message = self.backend.getCurrentMob().getName()

        self.mobInfoBar.configure(text = message)

    def updateMobHealthBar(self):
        mobHealth = self.backend.getCurrentMob().getHealth()
        self.mobHealthBar.configure(text="Health: {}".format(mobHealth))

    def updateMobDefenseBar(self):
        mobDefense = self.backend.getCurrentMob().getDefense()
        self.mobDefenseBar.configure(text="Defense: {}".format(mobDefense))

    def updateMobAttackBar(self):
        mobAttack = self.backend.getCurrentMob().getAttack()
        self.mobAttackBar.configure(text="Attack: {}".format(mobAttack))

    def UIRefresh(self):
        self.person = self.backend.getPerson()
        self.currentLocation = self.backend.getCurrentLocation()
        self.currentMob = self.backend.getCurrentMob()


        self.updateMobDefenseBar()
        self.updatePlayerInfoBar()
        self.updatePlayerHealthBar()
        self.updatePlayerAttackBar()
        self.updatePlayerDefenseBar()
        self.updateLocationInfoBar()
        self.updateMobInfoBar()
        self.updateMobHealthBar()
        self.updateMobAttackBar()



