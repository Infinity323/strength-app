from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class KilosBreakdownScreen(Screen):
    """The kilos plates breakdown screen.

    Args:
        Screen (kivy.uix.screenmanager.Screen): A kivy Screen object.
    """
    weight = StringProperty("0")

    norm_one_side = 0
    norm_red = StringProperty("0")
    norm_blue = StringProperty("0")
    norm_yellow = StringProperty("0")
    norm_green = StringProperty("0")
    norm_ten = StringProperty("0")
    norm_five = StringProperty("0")
    norm_two = StringProperty("0")
    norm_one = StringProperty("0")
    norm_half = StringProperty("0")

    comp_one_side = 0
    comp_red = StringProperty("0")
    comp_blue = StringProperty("0")
    comp_yellow = StringProperty("0")
    comp_green = StringProperty("0")
    comp_ten = StringProperty("0")
    comp_five = StringProperty("0")
    comp_two = StringProperty("0")
    comp_one = StringProperty("0")
    comp_half = StringProperty("0")

    def kilos(self):
        """Breakdown the weight in kilos without 25 or 15 kg plates.
        """
        w = round(float(self.ids.weight.text)*2)/2
        self.weight = str(w)
        self.norm_one_side = (w - 20)/2
        self.norm_one_side -= int(self.norm_red)*25
        self.norm_blue = str(int(self.norm_one_side / 20)) if self.norm_one_side >= 20 else str(0)
        self.norm_one_side -= int(self.norm_blue)*20
        self.norm_one_side -= int(self.norm_yellow)*15
        self.norm_green = str(int(self.norm_one_side / 10)) if self.norm_one_side >= 10 else str(0)
        self.norm_one_side -= int(self.norm_green)*10
        self.norm_ten = str(int(self.norm_one_side / 5)) if self.norm_one_side >= 5 else str(0)
        self.norm_one_side -= int(self.norm_ten)*5
        self.norm_five = str(int(self.norm_one_side / 2.5)) if self.norm_one_side >= 2.5 else str(0)
        self.norm_one_side -= int(self.norm_five)*2.5
        self.norm_two = str(int(self.norm_one_side / 1.25)) if self.norm_one_side >= 1.25 else str(0)
        self.norm_one_side -= int(self.norm_two)*1.25
        self.norm_one = str(int(self.norm_one_side/0.5)) if self.norm_one_side >= 0.5 else str(0)
        self.norm_one_side -= int(self.norm_one)*0.5
        self.norm_half = str(int(self.norm_one_side / 0.250))

        return

    def compKilos(self):
        """Breakdown the weight in kilos with all plates.
        """
        w = round(float(self.ids.weight.text)*2)/2
        self.weight = str(w)
        self.comp_one_side = (w - 20)/2
        self.comp_red = str(int(self.comp_one_side / 25)) if self.comp_one_side >= 25 else str(0)
        self.comp_one_side -= int(self.comp_red)*25
        self.comp_blue = str(int(self.comp_one_side / 20)) if self.comp_one_side >= 20 else str(0)
        self.comp_one_side -= int(self.comp_blue)*20
        self.comp_yellow = str(int(self.comp_one_side / 15)) if self.comp_one_side >= 15 else str(0)
        self.comp_one_side -= int(self.comp_yellow)*15
        self.comp_green = str(int(self.comp_one_side / 10)) if self.comp_one_side >= 10 else str(0)
        self.comp_one_side -= int(self.comp_green)*10
        self.comp_ten = str(int(self.comp_one_side / 5)) if self.comp_one_side >= 5 else str(0)
        self.comp_one_side -= int(self.comp_ten)*5
        self.comp_five = str(int(self.comp_one_side / 2.5)) if self.comp_one_side >= 2.5 else str(0)
        self.comp_one_side -= int(self.comp_five)*2.5
        self.comp_two = str(int(self.comp_one_side / 1.25)) if self.comp_one_side >= 1.25 else str(0)
        self.comp_one_side -= int(self.comp_two)*1.25
        self.comp_one = str(int(self.comp_one_side/0.5)) if self.comp_one_side >= 0.5 else str(0)
        self.comp_one_side -= int(self.comp_one)*0.5
        self.comp_half = str(int(self.comp_one_side / 0.250))

        return

    def __init__(self, **kwargs):
        """Init function.
        """
        super().__init__(**kwargs)