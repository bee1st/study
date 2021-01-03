import time
from  selenium import webdriver
def getPW():
    with open('d:\\pw.txt') as f:
        pw=f.readline()
    return pw.strip()
driver=webdriver.Chrome('data\\chromedriver')
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
print(driver.page_source)
pers=driver.find_elements_by_css_selector('#\31 _fol > span > a.system_folder._d6\(mcDragndrop\|html5DragOver\)._d7\(mcDragndrop\|html5Drop\)')
titles=driver.find_elements_by_css_selector('#list_for_view > ol > li.\32 7449_li.unmark._c1\(mrCore\|clickTitle\|27449\)._d2\(mcDragndrop\|html5DragStart\) > div > div.subject > a._d2\(mcDragndrop\|html5DragStart\) > span > strong')
for p,t in zip(pers,titles):
    print(p.text,t.text)


