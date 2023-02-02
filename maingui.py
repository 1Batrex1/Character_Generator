import random

from PyQt5 import QtCore, QtGui, QtWidgets
from Warhammer import *


class Dialog(QtWidgets.QDialog):

    def __init__(self, hero):
        super().__init__()
        self.setWindowTitle("Twój Bohater")
        self.layout = QtWidgets.QVBoxLayout()
        self.herotext = QtWidgets.QTextEdit()
        self.herotext.setText(hero.__str__())
        self.button = QtWidgets.QPushButton("OK")
        self.button.clicked.connect(self.accept)
        self.resize(300, 1000)
        self.layout.addWidget(self.herotext)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 749)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Imie = QtWidgets.QLabel(self.centralwidget)
        self.Imie.setEnabled(True)
        self.Imie.setGeometry(QtCore.QRect(80, 90, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Imie.setFont(font)
        self.Imie.setObjectName("Imie")
        self.Imie_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Imie_2.setEnabled(True)
        self.Imie_2.setGeometry(QtCore.QRect(360, 90, 261, 101))
        self.Imie_2.setObjectName("Imie_2")
        self.Rasa = QtWidgets.QLabel(self.centralwidget)
        self.Rasa.setEnabled(True)
        self.Rasa.setGeometry(QtCore.QRect(80, 190, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Rasa.setFont(font)
        self.Rasa.setObjectName("Rasa")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 280, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Generator = QtWidgets.QPushButton(self.centralwidget)
        self.Generator.setGeometry(QtCore.QRect(230, 440, 311, 101))
        self.Generator.setObjectName("Generator")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 10, 841, 691))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 841, 691))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Butt1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Butt1.setGeometry(QtCore.QRect(30, 60, 251, 71))
        self.Butt1.setObjectName("Butt1")
        self.SystemSelektor = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.SystemSelektor.setGeometry(QtCore.QRect(270, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.SystemSelektor.setFont(font)
        self.SystemSelektor.setObjectName("SystemSelektor")
        self.Butt2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Butt2.setEnabled(False)
        self.Butt2.setGeometry(QtCore.QRect(300, 60, 241, 71))
        self.Butt2.setCheckable(False)
        self.Butt2.setObjectName("Butt2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.rasy = QtWidgets.QGroupBox(self.centralwidget)
        self.rasy.setEnabled(True)
        self.rasy.setGeometry(QtCore.QRect(320, 190, 421, 101))
        self.rasy.setCheckable(False)
        self.rasy.setObjectName("rasy")
        self.Fuj = QtWidgets.QRadioButton(self.rasy)
        self.Fuj.setEnabled(True)
        self.Fuj.setGeometry(QtCore.QRect(11, 56, 181, 31))
        self.Fuj.setObjectName("Fuj")
        self.LilBoy = QtWidgets.QRadioButton(self.rasy)
        self.LilBoy.setEnabled(True)
        self.LilBoy.setGeometry(QtCore.QRect(190, 50, 221, 31))
        self.LilBoy.setObjectName("LilBoy")
        self.Kras = QtWidgets.QRadioButton(self.rasy)
        self.Kras.setEnabled(True)
        self.Kras.setGeometry(QtCore.QRect(191, 16, 221, 31))
        self.Kras.setObjectName("Kras")
        self.Lud = QtWidgets.QRadioButton(self.rasy)
        self.Lud.setEnabled(True)
        self.Lud.setGeometry(QtCore.QRect(10, 20, 181, 31))
        self.Lud.setObjectName("Lud")
        self.plcie = QtWidgets.QGroupBox(self.centralwidget)
        self.plcie.setGeometry(QtCore.QRect(320, 290, 421, 71))
        self.plcie.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.plcie.setObjectName("plcie")
        self.Chlop = QtWidgets.QRadioButton(self.plcie)
        self.Chlop.setGeometry(QtCore.QRect(230, 0, 191, 81))
        self.Chlop.setObjectName("Chlop")
        self.Baba = QtWidgets.QRadioButton(self.plcie)
        self.Baba.setGeometry(QtCore.QRect(10, 0, 211, 81))
        self.Baba.setObjectName("Baba")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 360, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Wynik = QtWidgets.QLabel(self.centralwidget)
        self.Wynik.setGeometry(QtCore.QRect(90, 580, 611, 91))
        self.Wynik.setObjectName("Wynik")
        self.Wynik.raise_()
        self.label_2.raise_()
        self.plcie.raise_()
        self.rasy.raise_()
        self.Imie.raise_()
        self.Imie_2.raise_()
        self.Rasa.raise_()
        self.label.raise_()
        self.Generator.raise_()
        self.scrollArea.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Butt1.clicked.connect(self.SystemSelektor.hide)  # type: ignore
        self.Butt1.clicked.connect(self.Butt2.hide)  # type: ignore
        self.Butt1.clicked.connect(self.Butt1.hide)  # type: ignore
        self.Butt1.clicked.connect(self.scrollArea.hide)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Butt1, self.Kras)
        MainWindow.setTabOrder(self.Kras, self.Butt2)
        MainWindow.setTabOrder(self.Butt2, self.Imie_2)
        MainWindow.setTabOrder(self.Imie_2, self.LilBoy)
        MainWindow.setTabOrder(self.LilBoy, self.Fuj)
        MainWindow.setTabOrder(self.Fuj, self.Lud)

        self.Generator.clicked.connect(self.Hero_Warhammer)  # TU będzie generacja

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Imie.setText(_translate("MainWindow", "Podaj imię postaci"))
        self.Rasa.setText(_translate("MainWindow", "Wybierz rasę"))
        self.label.setText(_translate("MainWindow", "Wybierz płeć"))
        self.Generator.setText(_translate("MainWindow", "Generuj Postać"))
        self.Butt1.setText(_translate("MainWindow", "Warhammer"))
        self.SystemSelektor.setText(_translate("MainWindow", "Wybierz System"))
        self.Butt2.setText(_translate("MainWindow", "Zew Cthulhu"))
        self.rasy.setTitle(_translate("MainWindow", "GroupBox"))
        self.Fuj.setText(_translate("MainWindow", "Elf ):"))
        self.LilBoy.setText(_translate("MainWindow", "Niziołek"))
        self.Kras.setText(_translate("MainWindow", "Krasnolód"))
        self.Lud.setText(_translate("MainWindow", "Człowiek"))
        self.plcie.setTitle(_translate("MainWindow", "GroupBox"))
        self.Chlop.setText(_translate("MainWindow", "Mężczyzna"))
        self.Baba.setText(_translate("MainWindow", "Kobieta"))
        self.label_2.setText(_translate("MainWindow", "Wybierz profesję"))
        self.Wynik.setText(_translate("MainWindow", "TextLabel"))

    def Check_race(self):
        if self.Kras.isChecked():
            return "Krasnolud"
        if self.LilBoy.isChecked():
            return "Niziołek"
        if self.Lud.isChecked():
            return "Człowiek"
        if self.Fuj.isChecked():
            return "Elf"
        return None

    def Check_gender(self):
        if self.Chlop.isChecked():
            return "Mężczyzna"
        if self.Baba.isChecked():
            return "Kobieta"
        return None

    def Hero_Warhammer(self):

        skills = Warhammer.Initialize.load_skills()
        talens = Warhammer.Initialize.load_talents()
        professions = Warhammer.Initialize.load_profession()
        weapons = Warhammer.Initialize.load_weapons()
        items = Warhammer.Initialize.load_items()
        name = self.Imie_2.toPlainText()
        race = self.Check_race()
        gender = self.Check_gender()
        prof_id = random.randint(0, 4)
        if race is None or gender is None or name == "":
            return
        hero = Warhammer.Hero.Hero(name, race, professions[prof_id].name, gender, professions[prof_id].skills,
                                   professions[prof_id].talents, professions[prof_id].items,
                                   professions[prof_id].weapons)
        dial = Dialog(hero)
        dial.exec_()
