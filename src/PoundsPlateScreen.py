from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class PoundsPlateScreen(Screen):
    total = StringProperty("45")

    red = StringProperty("0")
    blue = StringProperty("0")
    yellow = StringProperty("0")
    green = StringProperty("0")
    ten = StringProperty("0")
    five = StringProperty("0")
    two = StringProperty("0")
    one = StringProperty("0")
    half = StringProperty("0")

    def updateTotal(self):
        self.total = str((int(self.red)*55+int(self.blue)*45+int(self.yellow)*35+int(self.green)*25+int(self.ten)*10+int(self.five)*5+int(self.two)*2.5+int(self.one)+int(self.half)*0.5)*2+45)
        return

    def updateRed(self, x):
        if self.red == "0" and x == -1: return
        self.red = str(int(self.red)+x)
        self.updateTotal()
        return

    def updateBlue(self, x):
        if self.blue == "0" and x == -1: return
        self.blue = str(int(self.blue)+x)
        self.updateTotal()
        return

    def updateYellow(self, x):
        if self.yellow == "0" and x == -1: return
        self.yellow = str(int(self.yellow)+x)
        self.updateTotal()
        return

    def updateGreen(self, x):
        if self.green == "0" and x == -1: return
        self.green = str(int(self.green)+x)
        self.updateTotal()
        return

    def updateTen(self, x):
        if self.ten == "0" and x == -1: return
        self.ten = str(int(self.ten)+x)
        self.updateTotal()
        return

    def updateFive(self, x):
        if self.five == "0" and x == -1: return
        self.five = str(int(self.five)+x)
        self.updateTotal()
        return

    def updateTwo(self, x):
        if self.two == "0" and x == -1: return
        self.two = str(int(self.two)+x)
        self.updateTotal()
        return

    def updateOne(self, x):
        if self.one == "0" and x == -1: return
        self.one = str(int(self.one)+x)
        self.updateTotal()
        return

    def updateHalf(self, x):
        if self.half == "0" and x == -1: return
        self.half = str(int(self.half)+x)
        self.updateTotal()
        return

    def reset(self):
        self.total = "45"
        self.red = "0"
        self.blue = "0"
        self.yellow = "0"
        self.green = "0"
        self.ten = "0"
        self.five = "0"
        self.two = "0"
        self.one = "0"
        self.half = "0"
        
        return


    def __init__(self, **kwargs):
        super().__init__(**kwargs)