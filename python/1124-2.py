import re #정규표현식
str="""
3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
"""
# re.findall(r'패턴', 문자열)
# r1 = re.findall('[0-9]', str)
# print(r1)
# r1 = re.findall(r'[0-9] + ', str)
# print(r1)
# r1 = re.findall(r'[A-Z]+', str)
# print(r1)
# r1 = re.findall(r'[a-z]+', str)
# print(r1)
# r1=re.findall(r'[A-Za-z]+',str)
# print(r1)
#---------------------
# *(0번이상), +(1번이상), ?(0또는 1), |(선택)
# [], {1,3} (1번이상 3번이하), {,3}(3번이하), {1,}(1번이상), {3}(3번)
# . 줄바꿈을 제외한 한글자
# print(re.match('a.b', 'aabbrrr'))
# print(re.match('a.b', 'a0brrr'))
# print(re.match('a.b', 'c0brrr'))
# print(re.findall('a.b', 'a0brrr'))
# print(re.search('a.b', 'aabrrr'))
str = '3pink dress'
print(re.match('[a-z]+', str))  #문자열 처음부터 정규식과 일치여부 확인
print(re.search('[a-z]+', str))  # 문자열 전체를 검색하여 일치여부 확인
print(re.findall('[a-z]+', str)) # 정규식에 일치하는 문자열 반환
# group() 정규식에 일치하는 문자열 추출
# print(re.match('[a-z]+', str).group()) #문자열 처음부터 정규식과 일치여부 확인
# print(re.search('[a-z]+', str).group()) #문자열 전체를 검색하여 일치여부 확인
str = 'pink333 dress444'
print(re.match('[a-z]+', str).group())
print(re.search('[a-z]+', str).group())
print(re.findall('[a-z]+', str))
str = 'My handphone number 010-3333-7890'
print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str))
print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str).group())
# print(re.match('\d\d\d-\d\d\d\d-\d\d\d\d',str).group())
print(re.findall('\d\d\d-\d\d\d\d-\d\d\d\d',str))
print(re.search('[0-9]{3,4}-[0-9]{3,4}-[0-9]{3,4}',str).group())
print('\n\n\n\n\n\n\n\n')
