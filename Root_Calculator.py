import sys
from pathlib import Path
import os

import PyQt5.QtCore
import PyQt5.QtGui

from PyQt5.QtCore import Qt, QThread, pyqtSignal,QObject, pyqtSlot, QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QComboBox,QMessageBox,
                             QLabel, QWidget, QBoxLayout, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QFrame)
from PyQt5.QtGui import QLinearGradient
from PyQt5.QtGui import QFont, QPixmap, QImage

from RootTheorem import RootTheorem

class MainWindow(QMainWindow):
    videoSignal = pyqtSignal(int)
    sendCropSignal = pyqtSignal()
    translateSignal = pyqtSignal(bool)
    stopSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Language Translator")

        self.setFixedSize(600, 450)


        self.initUI()
        self.style()

        self.ButtonCalculate.pressed.connect(self.calculate_pressed)

    def initUI(self):
        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        self.InputBox = QTextEdit()
        self.OutputBox = QTextEdit()

        self.InputBox.setFixedSize(500,50)
        self.OutputBox.setReadOnly(True)

        self.OutputBox.setFixedSize(500,50)

        self.ButtonCalculate = QPushButton("Calculate")
        self.ButtonCalculate.setFixedSize(250,50)

        self.TitleLabel = QLabel("Root Calculator")
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.LabelOutput = QLabel("Output")
        self.LabelInput = QLabel("Input")

        self.LabelInput.setFixedHeight(20)

        #INPUTCONTAINER-----------------------------
        self.InputContainer  = QWidget()
        LayoutInput = QVBoxLayout()

        LayoutInput.addWidget(self.LabelInput)
        LayoutInput.addWidget(self.InputBox,alignment=Qt.AlignmentFlag.AlignHCenter)
        LayoutInput.addWidget(self.ButtonCalculate,alignment=Qt.AlignmentFlag.AlignHCenter)

        self.InputContainer.setLayout(LayoutInput)
        #-----------------------------

        self.master = QVBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        self.Container1 = QFrame()
        self.Container2 = QFrame()

        col1.addWidget(self.TitleLabel)
        col2.addWidget(self.InputContainer)
        col2.addWidget(self.LabelOutput)
        col2.addWidget(self.OutputBox,alignment=Qt.AlignmentFlag.AlignHCenter)

        self.Container1.setLayout(col1)
        self.Container2.setLayout(col2)

        self.master.addWidget(self.Container1,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.master.addWidget(self.Container2)

        central_widget.setLayout(self.master)

    def calculate_pressed(self):
        solveRoot = RootTheorem(self.InputBox.toPlainText() or "")

        rootToText = ", ".join(solveRoot) if not type(solveRoot) == str else solveRoot

        self.OutputBox.setText(rootToText)

    def style(self):
        self.TitleLabel.setStyleSheet("""font-size: 20px;
                                        padding: 5px;""")

        self.LabelOutput.setStyleSheet("font-size: 15px; font-weight: bold; background-color: #ecd9ff; padding:0 5px;")
        self.LabelInput.setStyleSheet("font-size: 15px; font-weight: bold; background-color: #ecd9ff; padding:0 5px;")


        self.Container1.setObjectName("Container")
        self.Container2.setObjectName("Container")

        self.Container1.setFixedSize(280,100)

        self.ButtonCalculate.setStyleSheet("""
                            QPushButton {
                                background-color: #7e5c94;
                                color: #e8e8e8;
                                font-weight: bold;
                                font-size: 15px;
                                border-radius: 5px;
                                border: 2px solid #5d436e;
                                padding: 5px;
                            }
                            QPushButton:hover {
                                background-color: #5d436e;
                                color: grey
                            }
                            QPushButton:pressed {
                                background-color: #3c2c47;

                            }
                        """)

        self.setStyleSheet("""
            #Container {
                border: 1px outset grey;
                border-radius: 5px;
            }
            """)

        self.InputBox.setStyleSheet("border-bottom: none;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()