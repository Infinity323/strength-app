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
    """The main screen manager.

    Args:
        Screen (kivy.uix.screenmanager.ScreenManager): A kivy ScreenManager object.
    """
    pass

class MainMenuScreen(Screen):
    """The Main Menu screen.

    Args:
        Screen (kivy.uix.screenmanager.Screen): A kivy Screen object.
    """
    pass

class AboutScreen(Screen):
    """The About screen.

    Args:
        Screen (kivy.uix.screenmanager.Screen): A kivy Screen object.
    """
    pass

kv = Builder.load_file("StrengthApp.kv")

class StrengthApp(App):
    """The app driver.

    Args:
        App (kivy.app.App): A kivy App object.
    """
    def build(self):
        """Build the app from the .kv file.

        Returns:
            kivy.uix.widget: The app instance.
        """
        self.icon = "images/icon.png"
        
        return kv

if __name__ == "__main__":
    StrengthApp().run()
