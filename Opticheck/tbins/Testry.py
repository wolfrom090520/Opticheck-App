from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
import subprocess  # To open and run external files
Window.size = (310, 580)

class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "003B6D"
        text_color_active: "669ACC"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Classes'
            icon: 'account-group-outline'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Answer Key'
            icon: 'cellphone-key'

            MDLabel:
                text: 'Answer Key'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Scanner'
            icon: 'line-scan'
            on_tab_press: app.open_omr_main()  # Call method to open OMR_Main.py when clicked

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Sheet'
            icon: 'printer-outline'

            MDLabel:
                text: 'Sheet'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 5'
            text: 'Profile'
            icon: 'account-outline'

            MDLabel:
                text: 'Profile'
                halign: 'center'
'''
        )

    def open_omr_main(self):
        # Define the path to your OMR_Main.py file
        omr_main_path = "../scrins/OMR_Main.py"

        # Run OMR_Main.py script using subprocess
        try:
            subprocess.run(["python", omr_main_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to open OMR_Main.py: {e}")



Test().run()