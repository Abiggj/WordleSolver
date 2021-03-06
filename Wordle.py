# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wordle.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from solver import Solver

# Single global Solver class instance
WordleSolve = Solver()

# Class for UI elements set[text, score buttons, done button]
# class WordleGuess:
#     global WordleSolve
#
#     def __init__(self, buttons, done, guess='arise'):
#         self.buttons = buttons
#         self.done = done
#         self.guess = guess
#         self.score = None
# # Get scores from set's button text attribute
#     def get_score(self):
#         self.score = [button.text() for button in self.buttons]
#
# # Sets the elements to enabled state for use
#     def setEnabled(self):
#         for button in self.buttons:
#             button.setEnabled(True)
#         self.guess.setEnabled(True)
#         self.done.setEnabled(True)
#
# # Diables elements after use or before chance of use
#     def setDisabled(self):
#         for button in self.buttons:
#             button.setEnabled(False)
#         self.guess.setEnabled(False)
#         self.done.setEnabled(False)
# # Actual solving procedure using solver class, uses new guess and score in each instance
#     def wordleTry(self):
#         pass


class Ui_MainWindow(QMainWindow, object):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

    def setupUi(self, MainWindow):

        class guess:
            global WordleSolve
            def __init__(self, tag, buttons, done, guessTxt):
                self.guessTxt = guessTxt
                self.tag = tag
                self.buttons = list(buttons)
                self.done = done
                self.guessTxt.setText(str(''))
                self.score = None
                for button in self.buttons:
                    button.setEnabled(False)
                self.guessTxt.setReadOnly(True)
                self.done.setEnabled(False)

            def score_trans(self, score):
                for index in range(0,5):
                    self.buttons[index].setText(str(score[index]))

            def getScore(self):
                self.score = [int(button.text()) for button in self.buttons]

            def test(self, guess):
                self.done.setEnabled(True)
                self.guessTxt.setEnabled(True)
                for button in self.buttons:
                    button.setEnabled(True)
                self.guessTxt.setText(guess)

            def donetest(self):
                self.getScore()
                return WordleSolve.solve(self.score, self.guessTxt.toPlainText())


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 492)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrbtnA1 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnA1.setGeometry(QtCore.QRect(180, 40, 41, 41))
        self.scrbtnA1.setObjectName("scrbtnA1")
        self.scrbtnA2 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnA2.setGeometry(QtCore.QRect(230, 40, 41, 41))
        self.scrbtnA2.setObjectName("scrbtnA2")
        self.scrbtnA3 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnA3.setGeometry(QtCore.QRect(280, 40, 41, 41))
        self.scrbtnA3.setObjectName("scrbtnA3")
        self.scrbtnA5 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnA5.setGeometry(QtCore.QRect(380, 40, 41, 41))
        self.scrbtnA5.setObjectName("scrbtnA5")
        self.scrbtnA4 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnA4.setGeometry(QtCore.QRect(330, 40, 41, 41))
        self.scrbtnA4.setObjectName("scrbtnA4")
        self.guessA = QtWidgets.QTextEdit(self.centralwidget)
        self.guessA.setGeometry(QtCore.QRect(10, 40, 131, 41))
        self.guessA.setObjectName("guessA")
        self.scrbtnB2 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnB2.setGeometry(QtCore.QRect(230, 100, 41, 41))
        self.scrbtnB2.setObjectName("scrbtnB2")
        self.scrbtnB5 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnB5.setGeometry(QtCore.QRect(380, 100, 41, 41))
        self.scrbtnB5.setObjectName("scrbtnB5")
        self.guessB = QtWidgets.QTextEdit(self.centralwidget)
        self.guessB.setGeometry(QtCore.QRect(10, 100, 131, 41))
        self.guessB.setObjectName("guessB")
        self.scrbtnB4 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnB4.setGeometry(QtCore.QRect(330, 100, 41, 41))
        self.scrbtnB4.setObjectName("scrbtnB4")
        self.scrbtnB3 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnB3.setGeometry(QtCore.QRect(280, 100, 41, 41))
        self.scrbtnB3.setObjectName("scrbtnB3")
        self.scrbtnB1 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnB1.setGeometry(QtCore.QRect(180, 100, 41, 41))
        self.scrbtnB1.setObjectName("scrbtnB1")
        self.scrbtnC2 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnC2.setGeometry(QtCore.QRect(230, 160, 41, 41))
        self.scrbtnC2.setObjectName("scrbtnC2")
        self.scrbtnC5 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnC5.setGeometry(QtCore.QRect(380, 160, 41, 41))
        self.scrbtnC5.setObjectName("scrbtnC5")
        self.guessC = QtWidgets.QTextEdit(self.centralwidget)
        self.guessC.setGeometry(QtCore.QRect(10, 160, 131, 41))
        self.guessC.setObjectName("guessC")
        self.scrbtnC4 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnC4.setGeometry(QtCore.QRect(330, 160, 41, 41))
        self.scrbtnC4.setObjectName("scrbtnC4")
        self.scrbtnC3 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnC3.setGeometry(QtCore.QRect(280, 160, 41, 41))
        self.scrbtnC3.setObjectName("scrbtnC3")
        self.scrbtnC1 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnC1.setGeometry(QtCore.QRect(180, 160, 41, 41))
        self.scrbtnC1.setObjectName("scrbtnC1")
        self.scrbtnD2 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnD2.setGeometry(QtCore.QRect(230, 220, 41, 41))
        self.scrbtnD2.setObjectName("scrbtnD2")
        self.scrbtnD5 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnD5.setGeometry(QtCore.QRect(380, 220, 41, 41))
        self.scrbtnD5.setObjectName("scrbtnD5")
        self.guessD = QtWidgets.QTextEdit(self.centralwidget)
        self.guessD.setGeometry(QtCore.QRect(10, 220, 131, 41))
        self.guessD.setObjectName("guessD")
        self.scrbtnD4 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnD4.setGeometry(QtCore.QRect(330, 220, 41, 41))
        self.scrbtnD4.setObjectName("scrbtnD4")
        self.scrbtnD3 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnD3.setGeometry(QtCore.QRect(280, 220, 41, 41))
        self.scrbtnD3.setObjectName("scrbtnD3")
        self.scrbtnD1 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnD1.setGeometry(QtCore.QRect(180, 220, 41, 41))
        self.scrbtnD1.setObjectName("scrbtnD1")

        self.scrbtnE2 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnE2.setGeometry(QtCore.QRect(230, 280, 41, 41))
        self.scrbtnE2.setObjectName("scrbtnE2")
        self.scrbtnE5 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnE5.setGeometry(QtCore.QRect(380, 280, 41, 41))
        self.scrbtnE5.setObjectName("scrbtnE5")
        self.guessE = QtWidgets.QTextEdit(self.centralwidget)
        self.guessE.setGeometry(QtCore.QRect(10, 280, 131, 41))
        self.guessE.setObjectName("guessE")
        self.scrbtnE4 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnE4.setGeometry(QtCore.QRect(330, 280, 41, 41))
        self.scrbtnE4.setObjectName("scrbtnE4")
        self.scrbtnE3 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnE3.setGeometry(QtCore.QRect(280, 280, 41, 41))
        self.scrbtnE3.setObjectName("scrbtnE3")
        self.scrbtnE1 = QtWidgets.QPushButton(self.centralwidget)
        self.scrbtnE1.setGeometry(QtCore.QRect(180, 280, 41, 41))
        self.scrbtnE1.setObjectName("scrbtnE1")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(440, 290, 112, 23))
        self.radioButton_5.setObjectName("radioButton_4")

        self.guessFinal = QtWidgets.QTextEdit(self.centralwidget)
        self.guessFinal.setGeometry(QtCore.QRect(180, 340, 131, 41))
        self.guessFinal.setObjectName("guessFinal")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(440, 50, 112, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(440, 110, 112, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(440, 170, 112, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(440, 230, 112, 23))
        self.radioButton_4.setObjectName("radioButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.guessList = []
        self.buttons = []
        self.done = []
        self.guessList.append(guess("A", (self.scrbtnA1, self.scrbtnA2, self.scrbtnA3, self.scrbtnA4, self.scrbtnA5), self.radioButton, self.guessA))
        self.guessList.append(
            guess("B", (self.scrbtnB1, self.scrbtnB2, self.scrbtnB3, self.scrbtnB4, self.scrbtnB5), self.radioButton_2,
                  self.guessB))
        self.guessList.append(
            guess("C", (self.scrbtnC1, self.scrbtnC2, self.scrbtnC3, self.scrbtnC4, self.scrbtnC5), self.radioButton_3,
                  self.guessC))
        self.guessList.append(
            guess("D", (self.scrbtnD1, self.scrbtnD2, self.scrbtnD3, self.scrbtnD4, self.scrbtnD5), self.radioButton_4,
                  self.guessD))
        self.guessList.append(
            guess("E", (self.scrbtnE1, self.scrbtnE2, self.scrbtnE3, self.scrbtnE4, self.scrbtnE5), self.radioButton_5,
                  self.guessE))
        for guess in self.guessList:
            self.done.append(guess.done)
            guess.done.installEventFilter(self)
            for button in guess.buttons:
                self.buttons.append(button)
                button.installEventFilter(self)

        self.guessList[0].test('arise')

    #todo Event filter to be based on WordleSolve class to reach instances easily
    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and object in self.buttons:
                if int(object.text()) < 2:
                    object.setText(str(int(object.text())+1))
                elif int(object.text()) == 2:
                    object.setText(str(int(object.text())-2))
        elif event.type() == QtCore.QEvent.MouseButtonPress and object in self.done:
            ind = self.done.index(object)
            next_guess = self.guessList[ind].donetest()
            if ind < 4:
                self.guessList[ind+1].test(next_guess)
                self.guessList[ind+1].score_trans(self.guessList[ind].score)
            else:
                self.guessFinal.setText(next_guess)
        return super(Ui_MainWindow, self).eventFilter(object, event)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WordleSolver"))
        self.scrbtnA1.setText(_translate("MainWindow", "0"))
        self.scrbtnA2.setText(_translate("MainWindow", "0"))
        self.scrbtnA3.setText(_translate("MainWindow", "0"))
        self.scrbtnA5.setText(_translate("MainWindow", "0"))
        self.scrbtnA4.setText(_translate("MainWindow", "0"))
        self.scrbtnB2.setText(_translate("MainWindow", "0"))
        self.scrbtnB5.setText(_translate("MainWindow", "0"))
        self.scrbtnB4.setText(_translate("MainWindow", "0"))
        self.scrbtnB3.setText(_translate("MainWindow", "0"))
        self.scrbtnB1.setText(_translate("MainWindow", "0"))
        self.scrbtnC2.setText(_translate("MainWindow", "0"))
        self.scrbtnC5.setText(_translate("MainWindow", "0"))
        self.scrbtnC4.setText(_translate("MainWindow", "0"))
        self.scrbtnC3.setText(_translate("MainWindow", "0"))
        self.scrbtnC1.setText(_translate("MainWindow", "0"))
        self.scrbtnD2.setText(_translate("MainWindow", "0"))
        self.scrbtnD5.setText(_translate("MainWindow", "0"))
        self.scrbtnD4.setText(_translate("MainWindow", "0"))
        self.scrbtnD3.setText(_translate("MainWindow", "0"))
        self.scrbtnD1.setText(_translate("MainWindow", "0"))
        self.scrbtnE2.setText(_translate("MainWindow", "0"))
        self.scrbtnE5.setText(_translate("MainWindow", "0"))
        self.scrbtnE4.setText(_translate("MainWindow", "0"))
        self.scrbtnE3.setText(_translate("MainWindow", "0"))
        self.scrbtnE1.setText(_translate("MainWindow", "0"))
        self.radioButton.setText(_translate("MainWindow", "A"))
        self.radioButton_2.setText(_translate("MainWindow", "B"))
        self.radioButton_3.setText(_translate("MainWindow", "C"))
        self.radioButton_4.setText(_translate("MainWindow", "D"))
        self.radioButton_5.setText(_translate("MainWindow", "E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
