# DB 기본 연결 정보
from bs4 import BeautifulSoup
import requests
import pandas
import mysql.connector
config = {
    "user": "root",
    "password": "1234",
    "host": "sarte.kr", #local
    "database": "food", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306)
}

# food_name을 입력받아 2차원 리스트로 반환
def get_food_name():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        sql = f"SELECT food_name from food"
        cursor.execute(sql)
        resultList = cursor.fetchall() 
        food_list = []
        for result in resultList:
            food_list.append(list(result))
        return food_list
    except mysql.connector.Error as err:
        return False

foods = get_food_name()
for food in foods:
    result_list = food[0].split(',')


def makeContent(pageUrl):
    recvd=requests.get(pageUrl)
    dom=BeautifulSoup(recvd.text,'lxml')
    title=dom.find('div',class_="view2_summary st3").find('h3').text
    # 재료
    view_step=dom.find('div',class_='view_step')
    divs=view_step.find_all('div',{'class':"media-body"})
    i=0
    contents=[]
    for div in divs:
        i=i+1
        contents.append(str(i)+']'+div.text)
    print('{}\n\n조리순서\n{}'.format(title,'\n'.join(contents)))

def main(url):
    recvd=requests.get(url)
    dom=BeautifulSoup(recvd.text,'lxml')
    lis=dom.find_all('li',{'class':"common_sp_list_li"})
    for li in lis:
        pageUrl='https://www.10000recipe.com'+li.find('a')['href']
        # print(pageUrl)
        makeContent(pageUrl)
        break
url='https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=63&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
if __name__=='__main__':
    main(url)

