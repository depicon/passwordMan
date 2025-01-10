import kivy
kivy.require('2.3.0')

from kivymd.app import MDApp

from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton, MDTextButton

class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return (
            MDScreen(
                MDRoundFlatButton(
                    MDTextButton ()
                )
            )
        )


if __name__ == '__main__':
    MyApp().run()