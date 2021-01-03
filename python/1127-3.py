import time
from  selenium import webdriver
def getPW():
    with open('d:\\pw.txt') as f:
        pw=f.readline()
    return pw.strip()
driver=webdriver.PhantomJS('data\\phantomjs')
url='https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(url)
idbox=driver.find_element_by_css_selector('#id')
idbox.send_keys('bee1st')
time.sleep(1)
pwbox=driver.find_element_by_css_selector('#pw')
pwbox.send_keys(getPW())
time.sleep(1)
btn=driver.find_element_by_css_selector('input[type=submit]')
btn.click()
time.sleep(1)
driver.get('https://mail.naver.com/')
time.sleep(1)
# print(driver.page_source)