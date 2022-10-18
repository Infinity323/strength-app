from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class ORMPredictorScreen(Screen):
    """The 1RM predictor screen.

    Args:
        Screen (kivy.uix.screenmanager.Screen): A kivy Screen object.
    """
    e = StringProperty("0")

    def estimate(self):
        """Fill estimation values.
        """
        w = float(self.ids.weight.text)
        r = int(self.ids.reps.text)
        if (r == 1): p = 1
        elif (r == 2): p = 0.9722
        elif (r == 3): p = 0.9443
        elif (r == 4): p = 0.9166
        elif (r == 5): p = 0.8888
        elif (r == 6): p = 0.861
        elif (r == 7): p = 0.8332
        elif (r == 8): p = 0.8054
        elif (r == 9): p = 0.7776
        elif (r == 10): p = 0.75
        else: return
        self.e = str(round(w/p))
        
        return

    def __init__(self, **kwargs):
        """Init function.
        """
        super().__init__(**kwargs)
        
        