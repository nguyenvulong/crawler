from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
driver.get("https://scholar.google.com/")


# try:
#     element = WebDriverWait(driver, 3).until(
#         EC.presence_of_element_located((By.ID, "gs_hdr_frm"))
#     )
# finally:
#     driver.quit()

# inputElement = driver.find_element_by_id("gs_in_txt gs_in_ac")
# inputElement = driver.find_element_by_class_name("gs_in_txt gs_in_ac")
# inputElement = driver.find_element_by_id("gs_hdr_frm")
inputElement = driver.find_elements(By.ID,"gs_hdr_frm" )
print(len(inputElement))
inputElement[0].send_keys("hello")
inputElement[0].send_keys(Keys.ENTER)
inputElement[0].submit()
driver.close()