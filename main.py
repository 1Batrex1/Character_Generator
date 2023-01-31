from Warhammer import *
import sys
from PyQt6 import QtWidgets, uic
from maingui import *

lista = Warhammer.Initialize.load_weapons()


hero = Warhammer.Hero.Hero("Bartek", "Niziołek", "Szlachcic", "Mężczyzna", "Cos", "Cos", "Cos", lista[0] , lista[1])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

print(hero)