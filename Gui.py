from PyQt5.QtWidgets import QApplication, QWidget

class Gui:
    def run(self):
        app = QApplication([])

        # create a Qt widget (a window) 
        window = QWidget()
        window.show()  

        app.exec()  