
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started!")
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(1)
driver.find_element_by_name("field-keywords").send_keys("s22")
time.sleep((1))
driver.find_element_by_name("nav-search-submit-button").click()
time.sleep(10)

driver.close()
print("Test case has sucessfully completed!")