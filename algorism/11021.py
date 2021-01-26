import sys
T = list(map(int, sys.stdin.readline().split()))

for i in range(T[0]):
    hap = list(map(int, sys.stdin.readline().split()))
    print("Case #{}: {}".format(i+1, hap[0]+hap[1]))
    # print("Case #"+(str(i + 1))+":",(hap[0] + hap[1]))