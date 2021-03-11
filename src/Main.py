import sys
import pymysql

from MainUI import Main
from SignUpUI import SignUpClicked
from LogInUI import *
from UserMainUI import SubmitClicked
from CreateUI import CreateClicked
from EditUI import EditClicked
from DeleteUI import *
from ListUI import ListClicked
from SongList import SongList
import MelonData
import MySQL


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.main = Main()
        self.signUp = SignUpClicked()
        self.logIn = LogInClicked()
        self.logInChecking = LogInChecking()
        self.userMain = SubmitClicked()
        self.create = CreateClicked()
        self.edit = EditClicked()
        self.delete = DeleteClicked()
        self.checking = Checking()
        self.list = ListClicked()
        self.songList = SongList()

        Main.show(self.main)

        self.main.signUpBtn.clicked.connect(self.SignUpFunction)
        self.main.logInBtn.clicked.connect(self.LogInFunction)
        self.signUp.submitBtn.clicked.connect(self.UserMainFunctionSignUp)
        self.logIn.submitBtn.clicked.connect(self.UserMainFunctionLogIn)
        self.userMain.createBtn.clicked.connect(self.ListCreateClicked)
        self.userMain.editBtn.clicked.connect(self.ListFunction)
        self.userMain.deleteBtn.clicked.connect(self.ListFunction)
        self.userMain.listBtn.clicked.connect(self.ListFunction)
        self.create.createBtn.clicked.connect(self.SongListFunction)
        self.delete.deleteBtn.clicked.connect(self.DeleteBtnClicked)
        self.checking.checkingYes.clicked.connect(self.CheckingYesClicked)
        self.checking.checkingNo.clicked.connect(self.CheckingNoClicked)
        self.edit.editBtn.clicked.connect(self.EditBtnClicked)
        self.list.createBtn.clicked.connect(self.ListCreateClicked)
        self.list.editBtn.clicked.connect(self.ListEditClicked)
        self.list.deleteBtn.clicked.connect(self.ListDeleteClicked)

        self.index = MySQL.CountPlaylists(mysqlCursor) + 1

    def SignUpFunction(self):
        self.signUp.show()

    def LogInFunction(self):
        self.logIn.show()

    def UserMainFunctionSignUp(self):
        values = self.signUp.PassUserInfo()
        lastname = str(values[2][0])
        firstname = str(values[2][1]+values[2][2])
        MySQL.InsertUserInfo(mysqlCursor, int(values[0]), values[1], lastname, firstname)
        mysqlConn.commit()

        self.signUp.close()
        self.userMain.userName.setText(firstname+" 님")
        self.userMain.show()
        Main.close(self.main)

    def UserMainFunctionLogIn(self):
        values = self.logIn.PassUserInfo()
        id = int(values[0])
        pw = str(values[1])
        if (MySQL.CheckingIDPW(mysqlCursor, id, pw)) == False:
            self.logInChecking.show()
        else:
            name = MySQL.GetUserName(mysqlCursor, id)
            self.logIn.close()
            self.userMain.userName.setText(str(name)+" 님")
            self.userMain.show()
            Main.close(self.main)

    def ListFunction(self):
        values = self.logIn.PassUserInfo()
        id = int(values[0])
        self.list.listWidgets.clear()
        playlists = MySQL.GetPlaylists(mysqlCursor, id)
        for i in range(0, len(playlists)):
            item = QListWidgetItem()
            item.setText("{0}".format(playlists[i]))
            self.list.listWidgets.addItem(item)
            item.setTextAlignment(Qt.AlignHCenter)
        self.list.show()

    def SongListFunction(self):
        values = self.logIn.PassUserInfo()
        id = int(values[0])

        pname = str(self.create.PassTitleValue())
        era = int(self.create.PassEraValue())
        songNum = int(self.create.PassSongNumValue())
        lists = MelonData.GetMelonData(era, songNum)
        for i in range(0, len(lists)):
            item = QListWidgetItem()
            item.setText("{0}".format(lists[i]))
            item.setTextAlignment(Qt.AlignHCenter)
            self.songList.listWidgets.addItem(item)
        print(lists)
        MySQL.CreatePlaylist(mysqlCursor, self.index, pname, songNum, era)
        mysqlConn.commit()

        MySQL.AddPlaylistToHave(mysqlCursor, self.index, id)
        mysqlConn.commit()
        self.index += 1

        #mysqlCursor.close()

        self.create.close()
        self.songList.show()

    def DeleteBtnClicked(self):
        self.checking.show()

    def CheckingYesClicked(self):
        info = self.list.PassSelectedItemValue()
        temp = info.split(',')[0]
        pid = int(temp.replace('(', ''))
        MySQL.DeletePlaylist(mysqlCursor, pid)
        mysqlConn.commit()

        self.checking.close()
        self.delete.close()
        self.list.close()

    def CheckingNoClicked(self):
        self.checking.close()

    def EditBtnClicked(self):
        info = self.list.PassSelectedItemValue()
        temp = info.split(',')
        pid = int(temp[0].replace('(', ''))
        snum = int(self.edit.PassSongNumValue())
        year = int(self.edit.PassEraValue())
        MySQL.EditPlaylist(mysqlCursor, snum, year, pid)
        mysqlConn.commit()

        self.edit.close()
        self.list.close()

    def ListCreateClicked(self):
        self.create.show()
        self.list.close()

    def ListEditClicked(self):
        self.edit.show()
        self.list.close()

    def ListDeleteClicked(self):
        self.delete.itemInfoLabel.setText(self.list.PassSelectedItemValue())
        self.delete.show()
        self.list.close()

if __name__ == '__main__':
    mysqlConn = pymysql.connect(host='localhost', user='root',
                                        password='password', db='playlist_db', charset='utf8')
    mysqlCursor = mysqlConn.cursor()

    app = QApplication(sys.argv)
    ex = MainWindow()
    #mysqlConn.close()
    #mysqlCursor.close()
    sys.exit(app.exec_())


"""
        #self.stackedWidgets.addWidget(self.main)
        self.stackedWidgets.addWidget(self.signUp)
        self.stackedWidgets.addWidget(self.logIn)

        self.centralWidget.setLayout(self.stackedWidgets)
        self.setCentralWidget(self.centralWidget)

        #self.stackedWidgets.setCurrentWidget(self.main)

        
"""

"""
    def switchingWindows(self):
        if self.stackedWidgets.currentWidget() == self.main:
            self.main.show()
            
            self.logIn.hide()
            self.signUp.hide()
            if self.main.signUpBtn.clicked:
                self.stackedWidgets.setCurrentWidget(self.signUp)
            elif self.main.logInBtn.clicked:
                self.stackedWidgets.setcurrentIndex(self.logIn)
        elif self.stackedWidgets.currentWidget() == self.signUp:
            self.main.hide()
            self.logIn.hide()
            self.signUp.show()
            #self.stackedWidgets.setCurrentWidget()
        else:
            self.main.hide()
            self.logIn.show()
            self.signUp.hide()
            #self.stackedWidgets.setcurrentIndex(3)
"""

"""
    def SwitchToSignUp(self):
        #self.signUp.InitSignUpUI()
        #self.setWindowTitle('숨듣명 플레이리스트 생성기 - 사용자 등록')
        self.setCentralWidget(self.signUp)
        Main().signUpBtn.clicked.connect(self.SignUpFunction)
        self.show()
"""

