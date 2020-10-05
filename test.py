import sys
# 테스트의 개수
C = int(input())
for i in range(C):
    first = 0
    a = input().split()
    lst = []

    for i in a:
        lst.append(int(i))
    first = lst.pop(0)
    mean = sum(lst)/first
    cnt=0
    for i in lst:
        if i>mean:
            cnt += 1
    print(round(cnt/first*100,3),end='')
    print('%')