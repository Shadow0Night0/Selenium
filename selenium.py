from os import supports_bytes_environ
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=['Name','Number'])
df_pitch = pd.DataFrame(columns=['Name','Number'])
value1 = float(input("Enter Integer 0 : fielder, 1 : pitcher\n"))
Time =  input("Year : \n")



# if the user selects Fielder, which im assuming means all batting positions?
if value1 == 0:
    temp = 'Batting'
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=PATH)
    html = driver.page_source
    soup = BeautifulSoup(html)

    driver.get("https://en.cpbl.com.tw/stats/recordall")
    dropdown = driver.find_element_by_id("Position")
    dd = Select(dropdown)
    dropdown_year = driver.find_element_by_name('Year')
    dd_year = Select(dropdown_year)

    dd.select_by_visible_text(temp)
    dd_year.select_by_visible_text(Time)
    sleep(5)
    driver.find_element_by_xpath("//input[@value='Search']").click()

    driver.find_element_by_class_name('RecordTable')
    sleep(5)
    driver.find_element_by_xpath("//*[@id='PageListContainer']/div[1]/div/table/tbody/tr[1]/th[12]").click()
    sleep(5)
    table_id = driver.find_element_by_tag_name('tbody')
    rows = table_id.find_elements_by_tag_name('tr')
    i=0
    for row in rows:
        temp = row.find_element_by_class_name('sticky')
        try:
            name = temp.find_element_by_class_name('name').text
        except:
            continue
        col = row.find_elements_by_class_name('num')[10].text
        #print(name.text)
        #print(col.text)
        df.loc[i] = [name , col]
        i=i+1
#if user select pitching
elif value1 == 1:
    temp = 'Pitching'
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=PATH)
    html = driver.page_source
    soup = BeautifulSoup(html)

    driver.get("https://en.cpbl.com.tw/stats/recordall")
    dropdown = driver.find_element_by_id("Position")
    dd = Select(dropdown)
    dropdown_year = driver.find_element_by_name('Year')
    dd_year = Select(dropdown_year)

    dd.select_by_visible_text(temp)
    dd_year.select_by_visible_text(Time)
    sleep(5)
    driver.find_element_by_xpath("//input[@value='Search']").click()

    driver.find_element_by_class_name('RecordTable')
    sleep(5)
    driver.find_element_by_xpath("//*[@id='PageListContainer']/div[1]/div/table/tbody/tr[1]/th[8]").click()
    sleep(5)
    table_id = driver.find_element_by_tag_name('tbody')
    rows = table_id.find_elements_by_tag_name('tr')
    i = 0
    for row in rows:
        temp = row.find_element_by_class_name('sticky')
        try:
            name = temp.find_element_by_class_name('name').text
        except:
            continue
        col = row.find_elements_by_class_name('num')[6].text
        #print(name.text)
        #print(col.text)
        df.loc[i] = [name , col]
        i=i+1

#if the user selects pitcher

print(df.head(5))





#//*[@id="PageListContainer"]/div[1]/div/table/tbody/tr
#//*[@id="PageListContainer"]/div[1]/div/table/tbody/tr[2]