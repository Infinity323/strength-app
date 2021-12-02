from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

MAX_WEIGHT = 2000

class NippardStrengthStandardScreen(Screen):
    # "Enumerate" strength category names
    rankings = ["Crippled", "Noob", "Beginner", "Intermediate", "Advanced", "Elite", "Freak"]
    s_div = []
    b_div = []
    d_div = []

    total = StringProperty("0")
    g = "m"
    bw = 0
    s = 0
    b = 0
    d = 0
    bw_times = StringProperty("0")
    s_times = StringProperty("0")
    b_times = StringProperty("0")
    d_times = StringProperty("0")
    s_level_name = StringProperty("N/A")
    b_level_name = StringProperty("N/A")
    d_level_name = StringProperty("N/A")
    s_level = 0
    b_level = 0
    d_level = 0
    s_progress = StringProperty("0")
    b_progress = StringProperty("0")
    d_progress = StringProperty("0")

    def update(self):
        self.s_level_name = self.rankings[self.s_level]
        self.b_level_name = self.rankings[self.b_level]
        self.d_level_name = self.rankings[self.d_level]
        self.total = str(self.s + self.b + self.d)
        self.bw_times = str(round(float(self.total)/self.bw, 2))
        self.s_times = str(round(self.s/self.bw, 2))
        self.b_times = str(round(self.b/self.bw, 2))
        self.d_times = str(round(self.d/self.bw, 2))

        return

    def progress(self):
        if self.g is "m":
            self.s_div = [0, 45, 135, 1.25*self.bw, 1.75*self.bw, 2.5*self.bw, 3*self.bw, MAX_WEIGHT]
            self.b_div = [0, 45, 95, self.bw, 1.5*self.bw, 2*self.bw, 2.25*self.bw, MAX_WEIGHT]
            self.d_div = [0, 45, 135, 1.5*self.bw, 2.25*self.bw, 3*self.bw, 3.5*self.bw, MAX_WEIGHT]
        else:
            self.s_div = [0, 45, 95, self.bw, 1.5*self.bw, 1.75*self.bw, 2.25*self.bw, MAX_WEIGHT]
            self.b_div = [0, 0, 45, 0.5*self.bw, 0.75*self.bw, self.bw, 1.25*self.bw, MAX_WEIGHT]
            self.d_div = [0, 45, 135, 1.25*self.bw, 1.75*self.bw, 2.25*self.bw, 3*self.bw, MAX_WEIGHT]
        low = self.s_div[self.s_level]
        high = self.s_div[self.s_level+1]
        self.s_progress = str((self.s - low)/(high - low))
        low = self.b_div[self.b_level]
        high = self.b_div[self.b_level+1]
        self.b_progress = str((self.b - low)/(high - low))
        low = self.d_div[self.d_level]
        high = self.d_div[self.d_level+1]
        self.d_progress = str((self.d - low)/(high - low))

        return

    def classifyMale(self):
        if self.s < 45: self.s_level = 0
        elif self.s >= 45 and self.s < 135: self.s_level = 1
        elif self.s >= 135 and self.s < 1.25*self.bw: self.s_level = 2
        elif self.s > 1.25*self.bw and self.s < 1.75*self.bw: self.s_level = 3
        elif self.s >= 1.75*self.bw and self.s < 2.5*self.bw: self.s_level = 4
        elif self.s >= 2.5*self.bw and self.s < 3*self.bw: self.s_level = 5
        else: self.s_level = 6

        if self.b < 45: self.b_level = 0
        elif self.b >= 45 and self.b < 95: self.b_level = 1
        elif self.b >= 95 and self.b < self.bw: self.b_level = 2
        elif self.b >= 1*self.bw and self.b < 1.5*self.bw: self.b_level = 3
        elif self.b >= 1.5*self.bw and self.b < 2*self.bw: self.b_level = 4
        elif self.b >= 2*self.bw and self.b < 2.25*self.bw: self.b_level = 5
        else: self.b_level = 6

        if self.d < 45: self.d_level = 0
        elif self.d >= 45 and self.d < 135: self.d_level = 1
        elif self.d >= 135 and self.d < 1.5*self.bw: self.d_level = 2
        elif self.d > 1.5*self.bw and self.d < 2.25*self.bw: self.d_level = 3
        elif self.d >= 2.25*self.bw and self.d < 3*self.bw: self.d_level = 4
        elif self.d >= 3*self.bw and self.d < 3.5*self.bw: self.d_level = 5
        else: self.d_level = 6

        self.update()
        self.progress()

        return

    def classifyFemale(self):
        if self.s < 45: self.s_level = 0
        elif self.s >= 45 and self.s < 95: self.s_level = 1
        elif self.s >= 95 and self.s < self.bw: self.s_level = 2
        elif self.s >= self.bw and self.s < 1.5*self.bw: self.s_level = 3
        elif self.s >= 1.5*self.bw and self.s < 1.75*self.bw: self.s_level = 4
        elif self.s >= 1.75*self.bw and self.s < 2.25*self.bw: self.s_level = 5
        else: self.s_level = 6

        if self.b < 45: self.b_level = 1
        elif self.b >= 45 and self.b < 0.5*self.bw: self.b_level = 2
        elif self.b >= 0.5*self.bw and self.b < 0.75*self.bw: self.b_level = 3
        elif self.b >= 0.75*self.bw and self.b < 1*self.bw: self.b_level = 4
        elif self.b >= 1*self.bw and self.b < 1.25*self.bw: self.b_level = 5
        else: self.b_level = 6

        if self.d < 45: self.d_level = 0
        elif self.d >= 45 and self.d < 135: self.d_level = 1
        elif self.d >= 135 and self.d < 1.25*self.bw: self.d_level = 2
        elif self.d > 1.25*self.bw and self.d < 1.75*self.bw: self.d_level = 3
        elif self.d >= 1.75*self.bw and self.d < 2.25*self.bw: self.d_level = 4
        elif self.d >= 2.25*self.bw and self.d < 3*self.bw: self.d_level = 5
        else: self.d_level = 6

        self.update()
        self.progress()

        return

    def calculate(self):
        self.bw = float(self.ids.bw.text)
        self.s = float(self.ids.s.text)
        self.b = float(self.ids.b.text)
        self.d = float(self.ids.d.text)
        if self.ids.male.state == "down":
            self.g = "m"
            self.classifyMale()
        else:
            self.g = "f"
            self.classifyFemale()
        return

    def __init__(self, **kwargs):
        super().__init__(**kwargs)