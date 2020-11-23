# import os
# import sys
# import urllib.request
# import json
# client_id = "Z7yRwPXHYKA9P4sJINTn"
# client_secret = "AgOcWdg0NL"
# encText = urllib.parse.quote("가을")
# url = "https://openapi.naver.com/v1/search/movie.json?start=1&display=100&query=" + encText # json 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result=response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
# dic=json.loads(result)
# print(dic)

# import os
# import sys
# import urllib.request
# client_id = "Z7yRwPXHYKA9P4sJINTn"
# client_secret = "AgOcWdg0NL"
# encText = urllib.parse.quote("금요일이네요")
# data = "source=ko&target=en&text=" + encText
# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

# i have a dream 을 검색하여 한국어로 번역

# with open(os.path.join('data','dream.txt'), 'r', encoding='utf-8') as f:
#     str = f.read()

# import os
# import sys
# import urllib.request
# client_id = "Z7yRwPXHYKA9P4sJINTn" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "AgOcWdg0NL" # 개발자센터에서 발급받은 Client Secret 값
# encText = urllib.parse.quote("반갑습니다")
# data = "source=ko&target=en&text=" + encText
# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

# -------------------
import os
import sys
import json
import urllib.request
client_id = "Lm6AY8QBy7cISOmNlGHi"
client_secret = "V75lfkmPvT"
with open('data\\dream.txt', 'r', encoding='utf-8') as f:
    str = f.read()
encText = urllib.parse.quote(str)
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
else:
    print("Error Code:" + rescode)

print(response_body.decode('utf-8'))
# print(json.loads(response_body.decode('utf-8'))['message']['result']['translatedText'])
with open(os.path.join('data','j.js'), 'w', encoding='utf-8') as f:
    f.write(response_body.decode('utf-8'))