from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import MelonData

class CreateClicked(QWidget):
    def __init__(self):
        super().__init__()
        self.InitCreateUI()

    def InitCreateUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('숨듣명 플레이리스트 생성기 - 플레이리스트 생성'))
        self.setWindowIcon(QIcon('img/playlistIcon.png'))

        self.vbox = QBoxLayout(QBoxLayout.TopToBottom)
        self.row1 = QVBoxLayout()
        self.row2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.row3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.optionVbox = QGroupBox("옵션 선택")
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
        self.subtitle = QLabel("- 플레이리스트 생성 -", self)

        self.title.setMaximumHeight(50)
        self.subtitle.setMaximumHeight(50)

        self.titleLabel = QLabel('플레이리스트 이름: ')
        #self.genreLabel = QLabel()
        self.eraLabel = QLabel()
        self.songNumLabel = QLabel()

        #genreCB = QComboBox(self)
        #genreCB.addItems(['발라드', '댄스', '랩/힙합', 'R&B/Soul', '인디음악', '록/메탈', '트로트', '포크/블루스'])

        self.playlistTitle = QLineEdit()
        self.playlistTitle.setFixedSize(100, 20)
        self.eraCB = QComboBox(self)
        self.eraCB.addItems(['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'])
        self.eraCB.currentIndexChanged.connect(self.PassEraValue)

        self.songNumCB = QComboBox(self)
        self.songNumCB.addItems(['10', '20', '30', '40', '50'])
        self.songNumCB.currentIndexChanged.connect(self.PassSongNumValue)

        self.createBtn = QPushButton('생성')
        self.createBtn.setFixedSize(200, 60)

        self.createBtn.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")
        self.title.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.titleLabel.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.subtitle.setStyleSheet("font-size:18px; color: #B39283; font-family: 카페24 써라운드")
        self.optionVbox.setStyleSheet("font-size:15px; color: #B39283; font-family: 카페24 써라운드")

        self.row1.addWidget(self.title, alignment=Qt.AlignHCenter)
        self.row1.addWidget(self.subtitle, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.optionVbox)
        #self.optionInnerBox.addWidget(genreCB)
        self.optionInnerBox.addWidget(self.titleLabel)
        self.optionInnerBox.addWidget(self.playlistTitle)
        self.optionInnerBox.addWidget(self.eraCB)
        self.optionInnerBox.addWidget(self.songNumCB)
        self.row3.addWidget(self.createBtn)
        self.optionVbox.setFixedSize(600, 150)

    def PassEraValue(self):
        print("passEra: ", str(self.eraCB.currentText()))
        return self.eraCB.currentText()

    def PassSongNumValue(self):
        print("passSong: ", str(self.songNumCB.currentText()))
        return self.songNumCB.currentText()

    def PassTitleValue(self):
        print("passTitle: ", str(self.playlistTitle.text()))
        return self.playlistTitle.text()
