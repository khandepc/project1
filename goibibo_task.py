from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe",options=options)

driver.get("https://www.goibibo.com")
expected_title="Online flight booking, Hotels, Bus &amp; Holiday Packages at Goibibo"
assert driver.title==expected_title,"expected title is not matching with"+driver.title

id_from_input_box="gosuggest_inputSrc"
id_destination="gosuggest_inputDest"
xpath_departure="//div[@id='searchWidgetCommon']/div[1]/div[1]/div[1]/div/div[5]/input"
xpath_return="//*[@id='searchWidgetCommon']/div[1]/div[1]/div[1]/div/div[7]/input[1]"
id_search_button="gi_search_btn"

element=driver.find_element_by_id(id_from_input_box)
element.send_keys("Pune")
text=element.text
print(text)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ENTER)

element=driver.find_element_by_id(id_destination)
element.send_keys("Mumbai")
text=element.text
print(text)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ENTER)




