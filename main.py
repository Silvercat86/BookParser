from bp import BookParser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineListItem

from kivy.core.window import Window

Window.size = (380, 780)

Builder.load_string("""
<StartScreen>:
    FloatLayout:
        MDTextField:
            font_size : "25dp"
            pos_hint : {"center_x":0.5,"center_y" : 0.75}
            size_hint : (0.8,0.1)

        MDRectangleFlatButton:
            text : "Search"
            pos_hint : {"center_x":0.5,"center_y" : 0.68}
            size_hint : (0.6,0.01)
            on_press: 
                root.manager.current = 'search'
                

<SearchScreen>:

    BoxLayout:
        size_hint : (0.9,0.4)
        pos_hint : {"center_x":0.5,"center_y" : 0.5}
        ScrollView:
            MDList:
                id : cool
""")


class StartScreen(Screen):
    def search(self, obj):
        myParser.parse_site("Огурец")



class SearchScreen(Screen):
    def on_enter(self):
        self.ids.cool.clear_widgets()
        print(self.manager.current)
        for i in range(1, 21):
            item = OneLineListItem(text="List " + str(i), on_press=self.change_screen)
            self.ids.cool.add_widget(item)

    def change_screen(self, obj):
        self.manager.current = "menu"
        print(self.manager.current)


class DemoApp(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='menu'))
        sm.add_widget(SearchScreen(name='search'))

        return sm


myParser = BookParser()

if __name__ == '__main__':
    DemoApp().run()
