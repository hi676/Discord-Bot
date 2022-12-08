from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pytz import timezone
import time
import os


def getclass(str):
  tz = timezone('EST')
  if datetime.now(tz).hour > 2 and datetime.now(tz).hour < 6:
    return "Webreg is down right now"
  else:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
      "https://cas.rutgers.edu/login?service=https%3A%2F%2Fsims.rutgers.edu%2Fwebreg%2Fj_spring_cas_security_check"
    )
    myuser = os.environ['username']
    mypass = os.environ['password']
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys(myuser)
    password.send_keys(mypass)
    submit = driver.find_element(By.NAME, "submit")
    submit.send_keys(Keys.RETURN)
    time.sleep(10)
    submit = driver.find_element(By.NAME, "submit")
    submit.send_keys(Keys.RETURN)
    course = driver.find_element(By.NAME, "coursesToAdd[0].courseIndex")
    course.send_keys(str)
    submit = driver.find_element(By.ID, "submit")
    submit.send_keys(Keys.RETURN)
    message = driver.find_element(By.CLASS_NAME, "first")
    message = message.text
    print(message)
    if "This section is closed" in message or "no open sections" in message:
      return "Did not get class"
    else:
      return "Got class"
      # server = smtplib.SMTP('smtp.gmail.com',587)
      # server.starttls()
      # server.login("anirudh.pappu007@gmail.com","egfvrfloiineyeph")
      # server.sendmail("anirudh.pappu007@gmail.com", "6096132972@vtext.com", "Did not get class")
      # server.quit()
