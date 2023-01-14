from google.oauth2 import service_account
from googleapiclient.discovery import build

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.techstars.com/mentors?currentPage=1')
time.sleep(5)
string = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[6]/button/span[1]')
no = int(string.text)
mentorlist = []
print(no)
i=1
while i<=no:
    driver.get('https://www.techstars.com/mentors?currentPage={}'.format(i))
    time.sleep(3)
    mentorsurl = driver.find_elements(By.TAG_NAME,'a')
    mentors = driver.find_elements(By.CSS_SELECTOR,'.jss545.jss360.jss547.jss591.jss599.jss611')
    for c in mentors:
        txtsplt = c.text.split('\n')
        try:
            link = c.find_element(By.TAG_NAME,'a').get_attribute('href')
            if len (txtsplt) == 1 :
                mentorlist.append ([c.text, '', link])
            else :
                mentorlist.append ([txtsplt[0],txtsplt[1],link])
        except:
            pass
            if len(txtsplt) == 1:
                mentorlist.append([c.text,'',''])
            else:
                mentorlist.append([txtsplt[0],txtsplt[1],''])
    print(i)


    i+=1



SCOPES = ['https://www.googleapis.com/auth/spreadsheets']#readonly
SERVICE_ACCOUNT_FILE = 'Keys.json'
SAMPLE_SPREADSHEET_ID = '19CWatx2wiSDPzpBZ1gyeTnaZIjyOacAkssi-vi8bQxE'

credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets','v4',credentials = credentials)

sheet = service.spreadsheets()
#result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                   range='email!A1:F31').execute()
#values = result.get('values',[])

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='mentors!A1', valueInputOption='USER_ENTERED', body={'values':mentorlist}).execute()