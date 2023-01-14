from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
mentorlist = []

i=1
while True:
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
    for a in driver.find_elements (By.TAG_NAME, 'button') :
        print(a.text)
    print(i)
    try:
        driver.find_elements(By.TAG_NAME,'button')[-1].click()
    except:
        break

    i+=1

df = pd.DataFrame(mentorlist,columns=['Name','Department','Linkedin url'])
df.to_excel('mentor_data1.xlsx',sheet_name='mentors')