#Scrape sportstats.ca
#Ensure selenium is installed: pip install selenium

from selenium import webdriver
import time
import csv

driver=webdriver.Chrome('/usr/local/bin/chromedriver')
myfile = open('melissas_results.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
csv_heading=["","","BIB","NAME","CATEGORY","RANK","GENDER PLACE","CAT. PLACE","GUN TIME"]
wr.writerow(csv_heading)
count=0
try:
    url="https://www.sportstats.ca/display-results.xhtml?raceid=40521"
    driver.get(url)
    while count <=54:
        table_tr=driver.find_elements_by_xpath("//table[@class='results overview-result']/tbody/tr[@role='row']")
        for tr in table_tr:
            lst=[]
            table_td=tr.find_elements_by_tag_name("td")
            for td in table_td:
                lst.append(td.text.encode('utf-8'))
            wr.writerow(lst)
        count=count+1
        print count
        driver.find_element_by_id('mainForm:j_idt366').click()
        time.sleep(5)
    time.sleep(5)
    driver.quit()
except Exception as e:
    print e
    driver.quit()
