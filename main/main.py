from bp import BookParser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineListItem

from kivy.core.window import Window

Window.size = (380, 780)

Builder.load_string("""
<StartScreen>:
    BoxLayout:
        orientation : "vertical"
        MDTopAppBar:
            title: "Demo Application"
            elevation : 0
        FloatLayout:
            MDTextField:
                font_size : "28dp"
                pos_hint : {"center_x":0.5,"center_y" : 0.7}
                size_hint : (0.8,0.11)
                id : textField

            MDRectangleFlatButton:
                text : "Search"
                font_size : "20dp"
                pos_hint : {"center_x":0.5,"center_y" : 0.6}
                size_hint : (0.6,0.08)
                on_press: 
                    root.search()
        
<SearchScreen>:
    FloatLayout:
        MDRectangleFlatButton:
            font_size: "32"
            halign : "left"
            pos_hint : {"center_x":0.5,"center_y" : 0.7}
            size_hint : (0.9,0.1)
            text : "Книги : 0"
            id :  booksBtn
        MDRectangleFlatButton:
            font_size: "32"
            halign : "left"
            pos_hint : {"center_x":0.5,"center_y" : 0.59}
            size_hint : (0.9,0.1)
            text : "Серии : 0"
            id :  seriesBtn
        MDRectangleFlatButton:
            font_size: "32"
            halign : "left"
            pos_hint : {"center_x":0.5,"center_y" : 0.48}
            size_hint : (0.9,0.1)
            text : "Авторы : 0"
            id :  authorsBtn
            

<BookScreen>:

    BoxLayout:
        size_hint : (0.9,0.4)
        pos_hint : {"center_x":0.5,"center_y" : 0.5}
        ScrollView:
            MDList:
                id : myList
""")


class StartScreen(Screen):
    def search(self):
        self.manager.current = "search"

        myParser.parse_site(self.ids.textField.text)


class SearchScreen(Screen):
    def on_enter(self):
        self.ids.booksBtn.text = f"Книги : {len(myParser.books)}"
        self.ids.seriesBtn.text = f"Серии : {len(myParser.series)}"
        self.ids.authorsBtn.text = f"Авторы : {len(myParser.authors)}"


class BookScreen(Screen):
    def on_enter(self):
        self.ids.cool.clear_widgets()
        print(self.manager.current)
        for i in range(1, 21):
            item = OneLineListItem(text="List " + str(i), on_press=self.change_screen)
            self.ids.myList.add_widget(item)

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
