from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/BTM-FACULTY/PycharmProjects/Automation/drivers/chromedriver.exe")
driver.get("file:///C:/Users/BTM-FACULTY/Desktop/qspwebtable.html")
driver.maximize_window()
driver.implicitly_wait(30)

val1 = driver.find_element_by_xpath("//*[@id='cric']/tbody/tr[3]/td[1]")
print(type(val1))#webelement
print(val1.text)#Sehwag


val = driver.find_elements_by_xpath("//*[@id='cric']/tbody/tr/td")
print(type(val))#List
print(len(val))#9
#
for i in val:   #iterate through each and every item of list
    print(i.text)#fetch text from each webelement