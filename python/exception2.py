# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1
name = ['kim', 'lee', 'park']

try:
    z = 'kim'
    x = name.index(z)
    print('{} found it! in name'.format(z, x + 1))
except ValueError:
    print('Not Found it -Occurred ValueError')

else :
    print('Ok! sure!') 

try:
    z = 'cho'
    x = name.index(z)
    print('{} found it! in name'.format(z, x + 1))
except ValueError:
    print('Not Found it -Occurred ValueError')

# 예제 2

try:
    z = 'jin'
    x = name.index(z)
    print('{} found it! in name'.format(z, x + 1))
except ValueError:
    print('Not Found it -Occurred ValueError')
else :
    print('Ok! sure!')

# 예제 3
try:
    z = 'jin'
    x = name.index(z)
    print('{} found it! in name'.format(z, x + 1))
except ValueError:
    print('Not Found it -Occurred ValueError')
else :
    print('Ok! sure!')
finally: #무조건 적인 실행
    print('finally ok')

# 예제 4
# 예외처리는 하지 않지만 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('Ok finally!!!')

# 예제 5
try:
    z = 'jin'
    x = name.index(z)
    print('{} found it! in name'.format(z, x + 1))
except ValueError as l:
    print('Not Found it -ValueError ValueError')
except IndexError:
    print('Not Found it -IndexError IndexError')
except Exception:
    print('Not Found it -Exception Exception')
else :
    print('Ok! sure!')
finally: #무조건 적인 실행
    print('finally ok')

# 예제 6
# 예외를 직접 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'kim'
    if a == 'kim':
        print('허가')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('ok')
