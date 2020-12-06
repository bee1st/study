# 파이썬 외부파일 처리
# 파이썬 excel, csv파일 읽기 및 쓰기

# import csv
# # 예제 1
# with open('./data/webtoon.csv', 'r', encoding="utf-8") as f:
#     reader = csv.reader(f)
#     next(reader) # header스킵
#     # print(type(reader)) 
#     # print(dir(reader))
#     for i in reader:
#         print(i)


# import csv
# # 예제 1
# with open('./data/webtoon.csv', 'r', encoding="utf-8") as f:
#     reader = csv.reader(f, delimiter="|")
#     next(reader) # header스킵
#     # print(type(reader)) 
#     # print(dir(reader))
#     for i in reader:
#         print(i)

import csv
with open('./data/webtoon.csv', 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f) # key : value 로 출력

    for i in reader:
        for j, k in i.items():
            print(j, k)

w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]
with open('./data/sample.csv', 'w', encoding='utf-8') as f:
    wt = csv.writer(f)

    for i in w:
        wt.writerow(i)

with open('./data/sample1.csv', 'w', encoding='utf-8') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas를 주로 사용
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas

xlsx = pandas.read_excel('./data/sample.xlsx')
print(xlsx.head())  
print(xlsx.tail())
print(xlsx.shape) #행, 열
xlsx.to_excel('./data/result.xlsx', index=False)
xlsx.to_csv('./data/result.xlsx', index=False)