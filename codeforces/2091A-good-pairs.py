# Problem: 2091A - Good Pairs
# Link: https://codeforces.com/problemset/problem/2091/A
# Tags: 
# Date: 2025-03-27


#import sys
#sys.stdin = open('input.txt', 'r')

#submit after this

t = int(input())
for _ in range(t):
    #01.03.2025
    d = {0:3, 1:1, 2:2, 3:1, 5:1}
    n = int(input())
    a = list(map(int, input().split()))
    total = 5
    for i,x in enumerate(a):
        if x in d and d[x] > 0:
            d[x]-=1
            if d[x] == 0:
                total-=1
            if total == 0:
                print(i+1)
                break
    if total != 0:
        print(0)