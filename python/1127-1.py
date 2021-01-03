from selenium import webdriver
import time
driver=webdriver.Chrome('data\\chromedriver')
url='https://pjt3591oo.github.io/'
driver.get(url)    #해당 페이지 접속
# print("현재페이지소스",driver.page_source)
# print("현재url",driver.current_url)
# print("title태그",driver.title)
time.sleep(1)
search=driver.find_element_by_css_selector('body > header > div > nav > div > a:nth-child(4)')
search.click()
box=driver.find_element_by_css_selector('#search-box')
box.send_keys('python')
btn=driver.find_element_by_css_selector('input[type=submit]')
btn.click()
# 파랑제목들 출력하세요
h3s=driver.find_elements_by_css_selector('#search-results > li > a > h3')
print(h3s)
for h3 in h3s:
    print(h3.text)