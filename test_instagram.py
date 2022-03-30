import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
username= input("enter usernam")
password= input("enter password")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started!")
driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.find_element_by_name("username").send_keys(username)
time.sleep(1)
driver.find_element_by_name("password").send_keys(password)
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(1)

driver.close()
print("Test case has sucessfully completed!")