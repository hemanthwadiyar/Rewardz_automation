import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()

chromeOptions.add_experimental_option("prefs",{"download.default_directory":"/Users/mac/Downloads"})
#driver = webdriver.Chrome(executable_path="/Users/mac/Desktop/RewardzProject/Driver/chromedriver",chrome_options=chromeOptions)

driver = webdriver.Chrome(executable_path="/Users/mac/Desktop/Drivers/chromedriver",chrome_options=chromeOptions)

driver.get("https://cerrapoints.com/Dashboard")
time.sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-default login-top']").click()
time.sleep(1)
username = driver.find_element_by_xpath("//body[@class='modal-open']/div[@id='main_container']/div[@id='LoginModal']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/div[@class='form-sec']/div[contains(@class,'row')]/div[@class='col-sm-8 ng-scope']/form[@id='login-form']/input[1]")
username.send_keys("nonhemanthwadiyar@gmail.com")
driver.maximize_window()

driver.find_element_by_xpath("//input[@type='password']").send_keys("pass")
driver.find_element_by_xpath("//button[contains(text(),'Sign In')]").click()
time.sleep(5)
driver.find_element_by_xpath("//img[@class='user-image']").click()
time.sleep(2)
driver.find_element_by_xpath("//trn[contains(text(),'Admin Functions')]").click()
time.sleep(1)

driver.execute_script("window.scrollTo(0, 4000)")
time.sleep(2)

x = driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[1]/div[1]/div[2]/select[1]")
time.sleep(2)
drop = Select(x)
drop.select_by_visible_text("Users")
time.sleep(2)


y = driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[1]/div[1]/div[3]/div[1]/select[1]")

drop2 = Select(y)
drop2.select_by_visible_text("Overall")
time.sleep(2)

driver.find_element_by_xpath("//trn[contains(text(),'Export as CSV')]").click()

time.sleep(5)

driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[2]/div[1]/div[1]/div[2]/a[1]").click()
