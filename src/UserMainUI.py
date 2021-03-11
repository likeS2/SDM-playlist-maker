from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SubmitClicked(QWidget):
    def __init__(self):
        super().__init__()
        self.InitSubmitUI()


    def InitSubmitUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('숨듣명 플레이리스트 생성기 - 사용자 메인'))
        self.setWindowIcon(QIcon('img/playlistIcon.png'))

        self.vbox = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.row1 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row4 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row5 = QBoxLayout(QBoxLayout.LeftToRight)

        self.vbox.addLayout(self.row1)
        self.vbox.addLayout(self.row2)
        self.vbox.addLayout(self.row3)
        self.vbox.addLayout(self.row4)
        self.vbox.addLayout(self.row5)

        self.setLayout(self.vbox)
        self.InitWidgets()

        self.setFixedSize(700, 450)

    def InitWidgets(self):
        self.title = QLabel("숨듣명 플레이리스트 생성기", self)

        self.userImage = QLabel()
        self.userName = QLabel()
        self.pixmapVar = QPixmap()
        self.pixmapVar.load("img/user.png")
        self.pixmapVar = self.pixmapVar.scaledToWidth(50)
        self.userImage.setPixmap(self.pixmapVar)

        self.createBtn = QPushButton('플레이리스트 생성', self)
        self.listBtn = QPushButton('플레이리스트 목록', self)
        self.editBtn = QPushButton('플레이리스트 수정', self)
        self.deleteBtn = QPushButton('플레이리스트 삭제', self)

        self.userImage.setFixedSize(50, 50)
        self.InitButtons(self.createBtn)
        self.InitButtons(self.listBtn)
        self.InitButtons(self.editBtn)
        self.InitButtons(self.deleteBtn)

        self.title.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.userName.setStyleSheet("font-size:20px; color: #B39283; font-family: 카페24 써라운드; text-decoration: underline")
        self.userName.setAlignment(Qt.AlignHCenter)
        self.row1.addWidget(self.title, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.userImage)
        self.row3.addWidget(self.userName)
        self.row4.addWidget(self.createBtn)
        self.row4.addWidget(self.listBtn)
        self.row5.addWidget(self.editBtn)
        self.row5.addWidget(self.deleteBtn)

    def InitButtons(self, button):
        button.setFixedSize(200, 60)
        button.setStyleSheet('color: white; background-color: #B39283; font-family: 카페24 써라운드')