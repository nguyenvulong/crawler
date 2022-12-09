from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)



driver.implicitly_wait(0.5)
driver.get("https://scholar.google.com/")

#identify element
element = driver.find_element_by_name("q")
# l = driver.find_element_by_class_name("gs_in_txtw gs_in_txtb gs_in_acw")
# l = driver.find_element_by_xpath("//div[contains(@class, 'gs_in_txtw gs_in_txtb gs_in_acw')]")

element.send_keys("Martin Luther King Jr.")


#get_attribute() to get value of input box
print("Value of input box: " + element.get_attribute('value'))
element.submit()

time.sleep(5)
print(driver.page_source)
driver.close()