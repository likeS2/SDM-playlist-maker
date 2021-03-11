from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
#from SignUpUI import SignUpClicked

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 450)
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('숨듣명 플레이리스트 생성기'))
        self.setWindowIcon(QIcon('img/playlistIcon.png'))

        self.title = QLabel('추억 리스트를 만들어드려요! (｡･w･)ﾉﾞ', self)
        self.title.move(50, -20)
        self.title.resize(600, 250)
        self.title.setAlignment(Qt.AlignCenter)
        self.titleFont = self.title.font()
        self.titleFont.setFamily("카페24 써라운드")
        self.titleFont.setPointSize(20)
        self.title.setFont(self.titleFont)

        self.bottom = QLabel('▁ ▆ ▂ ▄ ▇ ▅ █   𝓟𝓵𝓪𝔂𝓵𝓲𝓼𝓽   ▆ ▁ ▇ ▅ ▄ █ ▂', self)
        self.bottom.move(0, 300)
        self.bottom.resize(700, 100)
        self.bottom.setAlignment(Qt.AlignCenter)
        self.bottom.setStyleSheet('font-size:100%')
        self.logInBtn = QPushButton('사용자 로그인', self)
        self.signUpBtn = QPushButton('사용자 등록', self)

        self.logInBtn.setFixedSize(200, 60)
        self.logInBtn.setStyleSheet('color: white; background-color: #B39283; font-family: 카페24 써라운드')
        self.signUpBtn.setFixedSize(200, 60)
        self.signUpBtn.setStyleSheet('color: white; background-color: #B39283; font-family: 카페24 써라운드')

        vbox = QGridLayout()
        vbox.addWidget(self.logInBtn, 0, 0)
        vbox.addWidget(self.signUpBtn, 0, 1)
        self.setLayout(vbox)

        self.setFixedSize(700, 450)
        self.show()
