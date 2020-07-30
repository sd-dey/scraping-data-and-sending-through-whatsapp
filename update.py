import schedule
from selenium import webdriver

import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.mohfw.gov.in/").text
t=BeautifulSoup(r,'html.parser')

for x in t.find_all('tbody'):
	y=x.get_text()

y=y[1:]
z=y.split('\n\n')

states=['West Bengal','Uttar Pradesh','Gujarat']
myMessage=""
for i in z[:35]:
	j=i.split('\n')
	if j[2] in states:
	    myMessage+= "*State *"+j[2]+" has "+j[3]+"* Active cases *"+j[4]+"* Cured/Discharged *"+j[5]+"* Deaths and *"+j[6]+"* Total Cases *"

drive = webdriver.Chrome("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe")
drive.get("https://web.whatsapp.com/")
input("Press ENTER after scanning the code")

def message():
  name="Saptashwa"
  msg=myMessage
  

  user=drive.find_element_by_xpath('//span[@title = "{}"]'.format(name))
  user.click()

  msg_box=drive.find_element_by_class_name('_3uMse')

  
  msg_box.send_keys(msg)
  button=drive.find_element_by_class_name('_1U1xa')
  button.click()

schedule.every(5).seconds.do(message)

while True:
	schedule.run_pending()

drive.quit()

