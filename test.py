# importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

 
# using chrome driver
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)

# web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
 
# select class name where is input box are present
element = driver.find_elements(By.CLASS_NAME, "text_field")
 
# find number of input box
print(len(element))
 
# fill value in input box
driver.find_element_by_xpath('//*[@id="RESULT_TextField-1"]').send_keys("praveen")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-2"]').send_keys("yadav")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-3"]').send_keys("87871111")
 
# check status
x = driver.find_element_by_xpath('//*[@id="RESULT_TextField-1"]').is_displayed()
print(x)
driver.close()