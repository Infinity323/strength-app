from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import NippardStrengthStandardScreen
import PoundsBreakdownScreen
import KilosBreakdownScreen
import PoundsPlateScreen
import KilosPlateScreen
import ORMPredictorScreen

class MainMenu(ScreenManager):
    pass

class MainMenuScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

kv = Builder.load_file("StrengthApp.kv")

class StrengthApp(App):
    def build(self):
        self.icon = "data/icon.png"
        return kv

if __name__ == "__main__":
    StrengthApp().run()
