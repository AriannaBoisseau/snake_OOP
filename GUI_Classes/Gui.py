from PyQt5.QtWidgets import QApplication

from GUI_Classes.WelcomeWindow import WelcomeWindow

class Gui:
    def run(self):
        app = QApplication([])

        window = WelcomeWindow()
        window.show()

        app.exec()