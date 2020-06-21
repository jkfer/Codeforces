# https://codeforces.com/contest/1364/problem/C

import collections


def eval(n, L):
    Bexists = collections.defaultdict(bool)
    b = [-1] * n
    for i in range(1, n):
        if L[i] != L[i-1]:
            b[i] = L[i-1]
            D[L[i]] = True

    Bexists[L[n-1]] = True
    m = 0

    for i in rang(1, n)



# get input:
n = int(input())
L = list(map(int, input().split()))
print(eval(n, L))
