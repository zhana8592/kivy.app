from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import Screen, ScreenManager

class MyScreen(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)

class MyApp(App):

    def build(self):
        sm = ScreenManager()
        first = FirstScr()
        second = SecondScr()
        sm.add_widget(first)
        sm.add_widget(second)

        sm.current = "first"

        return sm

class FirstScr(Screen):
    def __init__ (self, name = "first"):
        super().__init__ (name = name)
        buttons = []
        for i in range (5):
            buttons.append(Button(text='No', font_size=14))
        self.vertical = BoxLayout(orientation = "vertical", padding = 5, spacing = 5)
        self.vertical2 = BoxLayout(orientation = "vertical", padding = 5, spacing = 5)
        horizontal = BoxLayout()
        label = Label(text = "Do you want free money", font_size = "20sp")
        for i in buttons:
            self.vertical.add_widget(i)
            i.on_press = self.test

        secondscr = Button(text = "2nd screen", font_size=14)
        secondscr.on_press = self.next

        horizontal.add_widget (label)
        self.vertical.add_widget (secondscr)
        horizontal.add_widget (self.vertical2)
        horizontal.add_widget(self.vertical)
        self.add_widget(horizontal)

    def test(self):
        congrats = Label(text="its so preppy in here")
        self.vertical2.add_widget(congrats)

    def next(self):
        self.manager.transition.direction = "left"
        self.manager.current = "second"

class SecondScr(Screen):
    def __init__ (self, name = "second"):
        super().__init__ (name = name)
        secondscr = Label (text = "second Screen")
        goback = Button(text = "back", font_size = 15)
        goback.on_press = self.back

        self.vertical = BoxLayout(orientation = "vertical", padding = 5, spacing = 5)
        self.vertical.add_widget (secondscr)
        self.vertical.add_widget(goback)
        self.add_widget(self.vertical)
    
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "first"

app = MyApp()
app.run()