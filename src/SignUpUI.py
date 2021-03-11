from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

class SignUpClicked(QDialog):
    def __init__(self):
        super().__init__()
        self.InitSignUpUI()

    def InitSignUpUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('숨듣명 플레이리스트 생성기 - 사용자 등록'))
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
        self.title = QLabel("사용자 등록", self)
        self.nameLabel = QLabel("이름", self)
        self.nameInput = QLineEdit()
        self.IDLabel = QLabel("아이디", self)
        self.IDInput = QLineEdit()
        self.PWLabel = QLabel("비밀번호", self)
        self.PWInput = QLineEdit()
        self.submitBtn = QPushButton("확인", clicked=self.PassUserInfo)

        self.title.setFixedSize(120, 40)
        self.nameLabel.setFixedSize(200, 40)
        self.nameInput.setFixedSize(300, 40)
        self.IDLabel.setFixedSize(200, 40)
        self.IDInput.setFixedSize(300, 40)
        self.PWLabel.setFixedSize(200, 40)
        self.PWInput.setFixedSize(300, 40)
        self.submitBtn.setFixedSize(200, 60)

        self.title.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.nameLabel.setStyleSheet("font-size:20px; color: #B39283; font-family: 카페24 써라운드")
        self.IDLabel.setStyleSheet("font-size:20px; color: #B39283; font-family: 카페24 써라운드")
        self.PWLabel.setStyleSheet("font-size:20px; color: #B39283; font-family: 카페24 써라운드")
        self.submitBtn.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")

        self.row1.addWidget(self.title, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.nameLabel)
        self.row2.addWidget(self.nameInput)
        self.row3.addWidget(self.IDLabel)
        self.row3.addWidget(self.IDInput)
        self.row4.addWidget(self.PWLabel)
        self.row4.addWidget(self.PWInput)
        self.row5.addWidget(self.submitBtn)

        #self.nameValue = self.nameInput.text()
        #self.idValue = self.IDInput.text()
        #self.pwValue = self.PWInput.text()


    def PassUserInfo(self):
        name = self.nameInput.text()
        id = self.IDInput.text()
        pw = self.PWInput.text()
        #self.close()
        return id, pw, name

