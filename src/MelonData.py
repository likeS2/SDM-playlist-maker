from selenium import webdriver

def GetMelonData(era, songNum):

      driver = webdriver.Chrome('/Users/ahhye/Desktop/Programming/DB_Project/chromedriver')
      driver.implicitly_wait(3)

      print("MElondata: ", era, songNum)

      url = 'https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate={0}'.format(era)
      driver.get(url)

      songs = []
      for item in range(0, songNum):
         temp = driver.find_elements_by_class_name('wrap_song_info')[item].text
         tempReplace = temp.replace('\n', ' | ')
         #tempReplace2 = tempReplace.replace(' | ', '')
         songs.append(tempReplace)

      return songs