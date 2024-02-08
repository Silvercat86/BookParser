username_helper = """
MDTextField:
    hint_text : "Enter Username"
    helper_text : "or click on forgot username"
    helper_text_mode : "on_focus"
    icon_right : "android"
    pos_hint : {"center_x":0.5,"center_y" : 0.5}
    size_hint : (0.5,None)
"""
screen_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: "Demo Application"
                        left_action_items : [["menu",lambda x: nav_drawer.set_state('toggle')]]
                        elevation : 0
                    MDLabel:
                        text: "Content"
                        halign: "center"
        MDNavigationDrawer:
            id: nav_drawer

"""
list_helper = """
Screen: 
    BoxLayout:
        size_hint : (0.9,0.4)
        pos_hint : {"center_x":0.5,"center_y" : 0.5}
        ScrollView:
            MDList:
                id : container
"""


"""def on_start(self):
    for i in range(1, 21):
        item = OneLineListItem(text="List " + str(i))
        self.root.ids.container.add_widget(item)"""
