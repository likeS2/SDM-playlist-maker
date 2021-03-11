from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ListClicked(QWidget):
    def __init__(self):
        super().__init__()
        self.InitListUI()

    def InitListUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('숨듣명 플레이리스트 생성기 - 플레이리스트 목록'))
        self.setWindowIcon(QIcon('img/playlistIcon.png'))

        self.vbox = QBoxLayout(QBoxLayout.TopToBottom)
        self.row1 = QVBoxLayout()
        self.row2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.listVbox = QVBoxLayout()
        self.labels = QHBoxLayout()
        self.temp = QBoxLayout(QBoxLayout.TopToBottom)
        self.listWidgets = QListWidget()

        self.vbox.addLayout(self.row1)
        self.vbox.addLayout(self.row2)
        self.vbox.addLayout(self.listVbox)
        self.listVbox.addLayout(self.labels)
        self.temp.addWidget(self.listWidgets)
        self.listVbox.addLayout(self.temp)

        self.InitWidgets()
        self.setLayout(self.vbox)
        self.setFixedSize(700, 450)

    def InitWidgets(self):
        #self.lists = []
        #print("list-list: ", self.lists)
        self.title = QLabel("숨듣명 플레이리스트 생성기", self)
        self.subtitle = QLabel("- 플레이리스트 목록 -", self)

        self.title.setMaximumHeight(50)
        self.subtitle.setMaximumHeight(50)

        self.createBtn = QPushButton('생성')
        self.createBtn.setFixedSize(50, 30)
        self.editBtn = QPushButton('수정')
        self.editBtn.setFixedSize(50, 30)
        self.deleteBtn = QPushButton('삭제')
        self.deleteBtn.setFixedSize(50, 30)

        self.label = QLabel('목록 번호 | 목록 이름 | 곡 수 | 장르 | 시대', self)

        self.title.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.subtitle.setStyleSheet("font-size:18px; color: #B39283; font-family: 카페24 써라운드")

        self.label.setStyleSheet("font-size:15px; color: #B39283; font-family: 카페24 써라운드")
        self.createBtn.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")
        self.editBtn.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")
        self.deleteBtn.setStyleSheet("color: white; background-color: #B39283; font-family: 카페24 써라운드")
        self.listWidgets.setStyleSheet("font-size:13px; color: black; font-family: 카페24 써라운드")

        self.row1.addWidget(self.title, alignment=Qt.AlignHCenter)
        self.row1.addWidget(self.subtitle, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.createBtn, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.editBtn, alignment=Qt.AlignHCenter)
        self.row2.addWidget(self.deleteBtn, alignment=Qt.AlignHCenter)
        self.labels.addWidget(self.label, alignment=Qt.AlignHCenter)



        self.listWidgets.itemSelectionChanged.connect(self.PassSelectedItemValue)

    def PassSelectedItemValue(self):
        print("selected: ", str(self.listWidgets.selectedItems()))
        print("selected: ", self.listWidgets.currentItem().text())

        return self.listWidgets.currentItem().text()
