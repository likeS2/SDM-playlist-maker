from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CreateUI import CreateClicked
import MelonData

class SongList(QWidget):
    def __init__(self):
        super().__init__()
        self.InitSongListUI()

    def InitSongListUI(self):
        self.setStyleSheet("background-color: #FFF7EF")
        self.setWindowTitle(('숨듣명 플레이리스트 생성기 - 플레이리스트 노래 목록'))
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

        self.title = QLabel("숨듣명 플레이리스트 생성기", self)
        self.subtitle = QLabel("- 플레이리스트 노래 목록 -", self)

        self.title.setMaximumHeight(50)
        self.subtitle.setMaximumHeight(50)

        self.label = QLabel('노래 제목 | 가수 | 수록 앨범', self)

        self.title.setStyleSheet("font-size:22px; color: #B39283; font-family: 카페24 써라운드")
        self.subtitle.setStyleSheet("font-size:18px; color: #B39283; font-family: 카페24 써라운드")

        self.label.setStyleSheet("font-size:15px; color: #B39283; font-family: 카페24 써라운드")
        self.listWidgets.setStyleSheet("font-size:13px; color: black; font-family: 맑은 고딕")

        self.row1.addWidget(self.title, alignment=Qt.AlignHCenter)
        self.row1.addWidget(self.subtitle, alignment=Qt.AlignHCenter)
        self.labels.addWidget(self.label, alignment=Qt.AlignHCenter)



"""
    def UpdateList(self):
        era, songNum = CreateClicked.CreateBtnClicked(CreateClicked())
        lists = MelonData.GetMelonData(era, songNum)
        print("upSongList:", era, songNum)
        self.listWidgets.clear()
        #("first: ", self.listWidgets[0])
        for i in range(0, len(lists)):
            item = QListWidgetItem()
            item.setText("{0}".format(lists[i]))
            item.setTextAlignment(Qt.AlignHCenter)
            self.listWidgets.addItem(item)
        print("second: ", self.listWidgets[0])
        #print("upSongList:", era, songNum)
        print("upListSongs: ", lists)
"""
