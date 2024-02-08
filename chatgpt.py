from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Определение кода Kivy в строке
kv_string = '''
<MyScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: my_label
            text: 'Hello, I am a label!'
        Button:
            id: my_button
            text: 'Click me!'
            on_press: root.on_button_click()
'''

# Загрузка кода Kivy из строки
Builder.load_string(kv_string)

class MyScreen(Screen):
    def on_button_click(self):
        # Получение доступа к виджетам по их id
        label_text = self.ids.my_label.text
        print(f"Button clicked! Label text: {label_text}")

class MyApp(App):
    def build(self):
        # Создаем ScreenManager
        sm = ScreenManager()

        # Создаем экземпляр MyScreen с использованием Builder
        screen = MyScreen()
        sm.add_widget(screen)

        return sm

if __name__ == '__main__':
    MyApp().run()