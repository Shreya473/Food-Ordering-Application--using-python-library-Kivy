from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from screens.home_page import HomePage


class AaharApp(MDApp):

    def build(self):
        Window.size = [300, 600]
        self.load_all_kv_files()
        return HomePage()


    def load_all_kv_files(self):
        Builder.load_file('screens/home_page.kv')
        Builder.load_file('libs/components/tool_bar.kv')
        Builder.load_file('libs/components/profile_pic.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/components/postcard.kv')




if __name__ == "__main__":
    AaharApp().run()
