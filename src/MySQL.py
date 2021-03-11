
def InsertUserInfo(cursor, id, pw, lname, fname):
    sql = "INSERT INTO user VALUES (%s, %s, %s, %s);"
    cursor.execute(sql, (id, pw, lname, fname))

def CheckingIDPW(cursor, id, pw):
    sql = "SELECT COUNT(*) FROM user WHERE userid = %s AND userpw = %s;"
    cursor.execute(sql, (id, pw))
    row = cursor.fetchone()
    check = int(row[0])
    if check:
        return True
    else:
        return False

def GetUserName(cursor, id):
    sql = "SELECT userfirstname FROM user WHERE userid = %s;"
    cursor.execute(sql, (id,))
    row = cursor.fetchone()
    name = str(row[0])
    return name

def GetUserID(cursor, fname):
    sql = "SELECT userid FROM user WHERE userfirstname = %s;"
    cursor.execute(sql, (fname,))
    row = cursor.fetchone()
    uid = int(row[0])
    return uid

def CreatePlaylist(cursor, index, pname, songNum, year):
    sql = "INSERT INTO playlists (playlistid, playlistname, playlistsongnum, year) VALUES (%s, %s, %s, %s);"
    cursor.execute(sql, (index, pname, songNum, year))

def GetPlaylistID(cursor, pname):
    sql = "SELECT playlistid FROM playlists WHERE playlistname = %s;"
    cursor.execute(sql, (pname,))
    row = cursor.fetchone()
    pid = int(row[0])
    return pid

def AddPlaylistToHave(cursor, pid, uid):
    sql = "INSERT INTO have VALUES (%s, %s);"
    cursor.execute(sql, (pid, uid))

def DeletePlaylist(cursor, pid):
    sql1 = "SET FOREIGN_KEY_CHECKS = 0;"
    sql2 = "DELETE FROM playlists WHERE playlistid = %s;"
    sql3 = "DELETE FROM have WHERE playlistid = %s;"
    cursor.execute(sql1)
    cursor.execute(sql2, pid)
    cursor.execute(sql3, pid)

def EditPlaylist(cursor, snum, year, pid):
    sql = "UPDATE playlists SET playlistsongnum = %s, year = %s WHERE playlistid = %s;"
    cursor.execute(sql, (snum, year, pid))

def GetPlaylists(cursor, uid):
    sql = "SELECT * FROM playlists WHERE playlistid IN (SELECT playlistid FROM have WHERE userid = %s);"
    cursor.execute(sql, (uid,))
    row = cursor.fetchall()
    list = []
    for i in row:
        list.append(str(i))
    return list

def CountPlaylists(cursor):
    sql = "SELECT COUNT(*) FROM playlists;"
    cursor.execute(sql)
    row = cursor.fetchone()
    pnum = int(row[0])
    return pnum
