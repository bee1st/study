import requests
import re
url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd = requests.get(url)
# print(recvd)
# reg = re.compile(r'<location wl_ver="3">(.+?)</location>')
# reg.findall(recvd.text, re.DOTALL))
locations = re.findall(r'<location wl_ver="3">(.+?)</location>', recvd.text, re.DOTALL)
print(len(locations))
for location in locations:
    # print(location)
    province = re.findall(r'<province>(.+?)</province>', location, re.DOTALL)
    # print(province)
    pc = re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>', location, re.DOTALL)
    # print(pc) # pc[0] = ('서울ㆍ인천ㆍ경기도', '서울')
    province = pc[0][0]
    city = pc[0][1]
    # print(province, city)s
    datas = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)
    # print(len(datas))
    for data in datas:
        # print(data)
        temps = re.findall(r'<mode>(.+?)</mode>.+?<tmEf>(.+?)</tmEf>.+?<wf>(.+?)</wf>.+?<tmn>(.+?)</tmn>.+?tmx>(.+?)</tmx>.+?<reliability>(.*?)</reliability>.+?<rnSt>(.+?)</rnSt>', 
                            data, re.DOTALL)
        # print(temps)
        mode = temps[0][0]
        tmEf = temps[0][1]
        wf = temps[0][2]
        tmn = temps[0][3]
        tmx = temps[0][4]
        reliability = temps[0][5]
        rnSt = temps[0][6]
        str = '{},{},{},{},{},{},{},{},{}'
        print(str.format(province, city, mode, tmEf, wf, tmn, tmx, reliability, rnSt))

