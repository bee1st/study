import re #정규표현식
# str="""
# 3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534
# """
# # 옵션
# # re.IGNORECASE(I) : 대소문자 구분x
# # re.DOTALL(S) : 줄바꿈 포함
# # re.VERBOSE(X) : 정규식에 주석을 사용할 수 있다

# print(re.findall('[a-z]+', str, re.I))


# str="""
# 3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534
# """
# print(re.findall('[a-z]+',str,re.I))
# t1=re.compile('[a-z]+', re.I)
# print(t1.findall(str)

#--------------
# import pyperclip
# # pyperclip.copy('hello python!')
# print(pyperclip.paste())
# ------------------
# https://namu.wiki/w/%EC%9D%B4%EB%A9%94%EC%9D%BC

# import pyperclip
# email_regex = re.compile(r'''(
#     [a-zA-Z0-9_.-]+     #username
#     @                   #@ 기호
#     [a-zA-Z0-9_.-]+     #도메인주소
#     (\.[a-zA-Z]{2,4}){1,2} #dot-
# )''', re.VERBOSE)
# text = pyperclip.paste()
# print(text)
# result = email_regex.findall(text)
# print(result) #[(),(),....] 
# for r in result:
#     print(r[0])

f = open('data\\test.html', encoding='utf-8')
text = f.read()
# print(text)
# tag = re.compile('<.+>')  #탐욕적 방식
tag=re.compile('<.+?>')   #게으른 방식
print(tag.match(text))
print(tag.search(text))
print(tag.findall(text))
print('-' * 50)
tag=re.compile('<(.+?)>')
print(tag.findall(text))
print('-')

# i로 시작하고 n으로 끝나는 모든 문자
str='internationalization'
test = re.compile(r'i.+n')
print(test.findall(str))  #탐욕적 방식
test = re.compile(r'i.+?n')
print(test.findall(str)) #게으른 방식