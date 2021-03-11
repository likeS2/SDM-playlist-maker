from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

class LogInClicked(QWidget):
    def __init__(self):
        super().__init__()
        self.InitLogInUI()

    def InitLogInUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('숨듣명 플레이리스트 생성기 - 로그인'))
        self.setWindowIcon(QIcon('img/playlistIcon.png'))

        self.vbox = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.row1 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row4 = QBoxLayout(QBoxLayout.LeftToRight)

        self.vbox.addLayout(self.row1)
        self.vbox.addLayout(self.row2)
        self.vbox.addLayout(self.row3)
        self.vbox.addLayout(self.row4)

        self.setLayout(self.vbox)
        self.InitWidgets()

        self.setFixedSize(700, 450)

    def InitWidgets(self):
        self.title = QLabel("로그인", self)
        self.IDLabel = QLabel("아이디", self)
        self.IDInput = QLineEdit()
        self.PWLabel = QLabel("비밀번호", self)
        self.PWInput = QLineEdit()
        self.submitBtn = QPushButton("확인", self)

        self.title.setFixedSize(90, 40)
        self.IDLabel.setFixedSize(200, 40)
        self.IDInput.setFixedSize(300, 40)
        self.PWLabel.setFixedSize(200, 40)
        self.PWInput.setFixedSize(300, 40)
        self.submitBtn.setFixedSize(200, 60)

        self.title.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.IDLabel.setStyleSheet("font-size:20px; color: #B39283; font-family: 카페24 써라운드")
        self.PWLabel.setStyleSheet("font-size:20px; color: #B39283; font-family: 카페24 써라운드")
        self.submitBtn.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")

        self.row1.addWidget(self.title, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.IDLabel)
        self.row2.addWidget(self.IDInput)
        self.row3.addWidget(self.PWLabel)
        self.row3.addWidget(self.PWInput)
        self.row4.addWidget(self.submitBtn)

    def PassUserInfo(self):
        id = self.IDInput.text()
        pw = self.PWInput.text()
        #self.close()
        return id, pw


class LogInChecking(QWidget):
    def __init__(self):
        super().__init__()
        self.InitLogInCheckingUI()

    def InitLogInCheckingUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('플레이리스트 로그인 확인'))
        self.setWindowIcon(QIcon('img/playlistIcon.png'))

        self.vbox = QBoxLayout(QBoxLayout.TopToBottom)
        self.row1 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row2 = QBoxLayout(QBoxLayout.LeftToRight)

        self.vbox.addLayout(self.row1)
        self.vbox.addLayout(self.row2)

        self.checkingLabel1 = QLabel('입력하신 정보와 일치하는 사용자가 없습니다.', self)
        self.checkingLabel2 = QLabel('다시 입력하시거나 사용자 등록을 해주세요.', self)

        self.checkingLabel1.setStyleSheet("font-size:18px; color: #B39283; font-family: 카페24 써라운드")
        self.checkingLabel2.setStyleSheet("font-size:18px; color: #B39283; font-family: 카페24 써라운드")

        self.checkingLabel1.setMaximumHeight(50)
        self.checkingLabel2.setMaximumHeight(50)

        self.row1.addWidget(self.checkingLabel1, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.checkingLabel2, alignment=Qt.AlignHCenter)

        self.setLayout(self.vbox)
        self.setFixedSize(450, 300)