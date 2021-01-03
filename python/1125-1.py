import re
import requests
# print(re.search('ca{2}t', 'ct'))
# sub('바꿀문자열', 대상문자열)
color = re.compile('(blue|green|red)')
print(color.sub('pink','orange book and green dress and red socks'))
