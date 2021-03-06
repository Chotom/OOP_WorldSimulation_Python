from tkinter import *
from World import World


class MainWindow(object):

    def __init__(self):
        self.__mainWindow = Tk()

        self.__mainWindow.resizable(False, False)
        self.__mainWindow.title("Tomasz Czochanski")
         
        # Set Board (0, 0)
        self.__boardWindow = LabelFrame(self.__mainWindow, text="Board")
        self.__boardWindow.grid(row=0, column=0, columnspan=10, rowspan=10)
        self.__worldView = Canvas(self.__boardWindow, height=600, width=600, border=1, bg="white")
        self.__worldView.grid(row=0, column=0)
        

        
        # Set Size area (0, 1)
        self.__setSizeWindow = LabelFrame(self.__mainWindow, text="Change size:") 
        self.__setSizeWindow.grid(row=0, column=10, columnspan=6)
        self.__xSizeSpinner = Spinbox(self.__setSizeWindow, from_=2, to=50, width=20)
        self.__xSizeSpinner.grid(row=0, column=0)
        self.__ySizeSpinner = Spinbox(self.__setSizeWindow, from_=2, to=50, width=20)
        self.__ySizeSpinner.grid(row=0, column=1)
        self.__setWorldSizeButton = Button(self.__setSizeWindow, text="Set world size", width=21, command=self.__changeSize)
        self.__setWorldSizeButton.grid(row=0, column=3)

        # Set addOrg area (1, 1)
        self.__addOrgWindow = LabelFrame(self.__mainWindow, text="Add Organism:") 
        self.__addOrgWindow.grid(row=1, column=11, columnspan=6)
        self.__addOrgText = Label(self.__addOrgWindow, text="Click left button on board to add chosen organism", width=60) 
        self.__addOrgText.grid(row=0, column=0, columnspan=6)
        self.__organismToChoose = StringVar(self.__addOrgWindow, "Antelope")
        organisms = ("Antelope", "Fox", "Sheep", "CyberSheep", "Turtle", "Wolf", "Dandelion", "DeadlyNightshade", "Grass", "Guarana", "SosnowskyHogweed")
        self.__organismChooser = OptionMenu(self.__addOrgWindow, self.__organismToChoose, *organisms)
        self.__organismChooser.grid(row=1, column=0, columnspan=6, rowspan=1)

        # Set TextBox (2, 1)
        self.__textBoxWindow = LabelFrame(self.__mainWindow, text="Actions:") 
        self.__textBoxWindow.grid(row=2, column=11, columnspan=6)
        self.__labelText = StringVar()
        self.__labelText.set("Arrows - move as Human\nR - special ability\nClick tile to add selected organism\nPress New Turn to start\n")
        self.__messagesOutput = Label(self.__textBoxWindow, textvariable=self.__labelText, height=22, width=60, bg="white", fg="black", relief=GROOVE)
        self.__messagesOutput.grid(row=0, column=0)

        # Add world
        self.__world = World.World(self.__worldView, 10, 10, self.__labelText)

        # Set Buttons (3, 1)
        self.__saveWorldButton = Button(self.__mainWindow, text="Save", width=29, height=4, command=self.__world.saveToFile)
        self.__saveWorldButton.grid(row=3, column=10, columnspan=3, rowspan=1)
        self.__loadWorldButton = Button(self.__mainWindow, text="Load", width=29, height=4, command=self.__world.loadFile)
        self.__loadWorldButton.grid(row=3, column=13, columnspan=3, rowspan=1)
        self.__newTurnButton = Button(self.__mainWindow, text="New Turn", width=60, height=4, command=self.__world.setNextTurn)
        self.__newTurnButton.grid(row=4, column=10, columnspan=6, rowspan=1)

        # Key binds for events
        self.__worldView.bind("<Left>", lambda e: self.__world.setHumanZn("w"))
        self.__worldView.bind("<Up>",  lambda e: self.__world.setHumanZn("a"))
        self.__worldView.bind("<Right>", lambda e: self.__world.setHumanZn("s"))
        self.__worldView.bind("<Down>", lambda e: self.__world.setHumanZn("d"))
        self.__worldView.bind("r", lambda e: self.__world.setHumanZn("r"))
        self.__worldView.bind("<Button-1>", self.__addOrganismOnClick)
        self.__worldView.focus_set()

       
        self.__world.drawWorld()
        self.__mainWindow.mainloop()

    def __changeSize(self):
        self.__world.changeSize(int(self.__xSizeSpinner.get()), int(self.__ySizeSpinner.get()))
        self.__worldView.focus_set()

    def __addOrganismOnClick(self, event):
        self.__world.addOnClick(self.__organismToChoose.get(), event.x, event.y)
        self.__worldView.focus_set()

window = MainWindow()