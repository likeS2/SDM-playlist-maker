from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DeleteClicked(QWidget):
    def __init__(self):
        super().__init__()
        self.InitDeleteUI()

    def InitDeleteUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('숨듣명 플레이리스트 생성기 - 플레이리스트 삭제'))
        self.setWindowIcon(QIcon('img/playlistIcon.png'))

        self.vbox = QBoxLayout(QBoxLayout.TopToBottom)
        self.row1 = QVBoxLayout()
        self.row2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.optionVbox = QGroupBox("삭제") # 플레이리스트 이름
        self.optionInnerBox = QHBoxLayout()

        self.vbox.addLayout(self.row1)
        self.vbox.addLayout(self.row2)
        self.vbox.addLayout(self.row3)

        self.InitWidgets()
        self.setLayout(self.vbox)
        self.optionVbox.setLayout(self.optionInnerBox)
        self.setFixedSize(700, 450)

    def InitWidgets(self):
        self.title = QLabel("숨듣명 플레이리스트 생성기", self)
        self.subtitle = QLabel("- 플레이리스트 삭제 -", self)

        self.title.setMaximumHeight(50)
        self.subtitle.setMaximumHeight(50)

        self.itemInfoLabel = QLabel()

        self.deleteBtn = QPushButton('삭제')
        self.deleteBtn.setFixedSize(200, 60)

        self.deleteBtn.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")
        self.title.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.subtitle.setStyleSheet("font-size:18px; color: #B39283; font-family: 카페24 써라운드")
        self.optionVbox.setStyleSheet("font-size:15px; color: #B39283; font-family: 카페24 써라운드")

        self.row1.addWidget(self.title, alignment=Qt.AlignHCenter)
        self.row1.addWidget(self.subtitle, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.optionVbox)
        self.optionInnerBox.addWidget(self.itemInfoLabel, alignment=Qt.AlignHCenter)
        self.row3.addWidget(self.deleteBtn)
        self.optionVbox.setFixedSize(600, 150)


class Checking(QWidget):
    def __init__(self):
        super().__init__()
        self.InitCheckingUI()

    def InitCheckingUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('플레이리스트 삭제 확인'))
        self.setWindowIcon(QIcon('img/playlistIcon.png'))

        self.vbox = QBoxLayout(QBoxLayout.TopToBottom)
        self.row1 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row2 = QBoxLayout(QBoxLayout.LeftToRight)

        self.vbox.addLayout(self.row1)
        self.vbox.addLayout(self.row2)

        self.checkingLabel = QLabel('삭제하시겠습니까?', self)
        self.checkingYes = QPushButton('네')
        self.checkingNo = QPushButton('아니요')

        self.checkingLabel.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.checkingYes.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")
        self.checkingNo.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")

        self.checkingLabel.setMaximumHeight(50)
        self.checkingYes.setFixedSize(100, 50)
        self.checkingNo.setFixedSize(100, 50)

        self.row1.addWidget(self.checkingLabel, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.checkingYes)
        self.row2.addWidget(self.checkingNo)

        self.setLayout(self.vbox)
        self.setFixedSize(450, 300)
