
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.flipkart.com")
driver.implicitly_wait(10)

xpath_close_popup="//div[@class='mCRfo9']/div/div/button"
xpath_electronics="//div[@id='container']/div/div[2]/div/ul/li/span[contains(text(),'Electronics')]"
xpath_mi="//*[@id='container']/div/div[2]/div/ul/li[1]/ul/li/ul/li[1]/ul/li[2]/a"
ac=ActionChains(driver)
element=driver.find_element_by_xpath(xpath_close_popup)
element.click()


element1=driver.find_element_by_xpath(xpath_electronics)
element2=driver.find_element_by_xpath(xpath_mi)
ac.move_to_element(element1).move_to_element(element2).click().perform()
