from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (400,600)
#Builder String
helper_string = '''
ScreenManager:
    Hello:
    Bye:

<Hello>:
    name: 'hello'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'


                Image:
                    source:'doremon.jpg'
                MDLabel:
                    text: '  Amazon Price Tracker'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Ravi'
                            IconLeftWidget:
                                icon: 'airballon'
                        OneLineIconListItem:
                            text: 'Shunham'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:
                            text:'BINOD'
                            IconLeftWidget:
                                icon: 'arrow-right'


<Bye>
    name: 'bye'
    MDLabel: 
        text: 'Good Bye'




'''
class Hello(Screen):
    pass
class Bye(Screen):
    pass

sm = ScreenManager()

sm.add_widget(Hello(name = 'hello'))
sm.add_widget(Bye(name='bye'))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        help_str = Builder.load_string(helper_string)

        screen.add_widget(help_str)
        return screen

DemoApp().run()
