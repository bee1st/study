from  selenium import webdriver
# 웹드라이버:크롤러와 브라우져를 연결시켜주는 프로그램
# 크롬드라이버 다운로드
# driver.find_element_by_class_name()
# driver.find_elements_by_class_name()
# driver.find_element_by_css_selector()
# driver.find_elements_by_css_selector()
# ...
# 마우스제어 click()
# 키보드제어 send_keys()
# 자바스크립트실행 execute_script()
import time
driver=webdriver.Chrome('data\\chromedriver')
url='https://pjt3591oo.github.io/'
driver.get(url)
a=driver.find_element_by_css_selector('body > main > div > div > div:nth-child(9) > h3 > a')
time.sleep(3)
seach = driver.find_element_by_css_selector('#search-box')

print(a.tag_name)
print(a.text)
a.click()