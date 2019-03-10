import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:/Users/BTM-FACULTY/PycharmProjects/Automation/drivers/chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.maximize_window()
driver.implicitly_wait(30)

month_val="7"
year_val="2009"
date_val="15"

ele = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
#ele = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(ele)
driver.find_element_by_id("datepicker").send_keys(month_val+"/"+date_val+"/"+year_val)
driver.find_element_by_id("datepicker").send_keys(Keys.ENTER)
#
# xp1="//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[text()="
# xp2="'"
# xp3="'"
# xp4="]"
# fxp=xp1+xp2+date_val+xp3+xp4
#
# month = driver.find_element_by_class_name("ui-datepicker-month")
# sel_mon = Select(month)
# sel_mon.select_by_value(month_val)
#
# time.sleep(5)
# year = driver.find_element_by_class_name("ui-datepicker-year")
# sel_year = Select(year)
# sel_year.select_by_visible_text(year_val)
#
# driver.find_element_by_xpath(fxp).click()

#driver.switch_to.default_content()
# driver.switch_to.parent_frame()
# driver.find_element_by_xpath("//a[text()='Draggable']").click()