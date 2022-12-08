from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def anagrams(str):
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--ignore-certificate-errors-spki-list')
  chrome_options.add_argument('--ignore-ssl-errors')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://scrabblewordfinder.org/")
  search = driver.find_element(By.ID, "ltr")
  search.send_keys(str)
  submit = driver.find_element(By.ID, "finderBtn")
  submit.send_keys(Keys.RETURN)
  list = ""
  for element in driver.find_elements(By.CLASS_NAME, "wordWrapper"):
    list += ''.join(x for x in element.text if x.isalpha()) + "\t"
  return list


# anagrams("AGRINZ")
