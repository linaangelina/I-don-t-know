from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

from second_win import *

class MainWin(QWidget):
    def __init__(self):
        '''окно, в котором находится приветсвие'''
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        ''' создает графические элементы'''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instructoin = QLabel(txt_instruction)

        self.Layout_line = QVBoxLayout()
        self.Layout_line.addWidget(self.hello_text, alignment = Qt.Alignment)
        self.Layout_line.addWidget(self.instruction, alignment = Qt.Alignment)
        self.Layout_line.addWidget(self.btn_next, alignment = Qt.Alignment)
        self.setLayout(self,layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.conect(self.next_click)

    ''' устанавливает, как будет выглядеть окно(надпись, размер, место)'''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_heiht)
        self.move(win_x, win_y)

    def main():
        app=QApplication([])
        mw=MainWin()
        app.exec_()

main()

app = QApplication(())
mv = MainWin()
app.exec_()
