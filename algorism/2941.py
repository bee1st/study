import sys
x = sys.stdin.readline() 
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

print(x)
print("==== START ===")
for i in a:
    x = x.replace(i, '*')
    print(x)

# sum = 0
# for i in a:
#     sum += (x.count(i) * (len(i) - 1))

print(len(x) - 1)
