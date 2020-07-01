# https://codeforces.com/contest/1364/problem/C


def eval(n, a):
    b = set(a)
    k, t = 0, 0
    not_in_set = []

    for j in range(1, n+1):
        if j not in b:
            not_in_set.append(j)

    for i in range(n):
        if a[i] > i+1:
            print(-1)
            break
        elif a[i] != k:
            print(k, end=' ')
            k = a[i]
        else:
            print(not_in_set[t], end=' ')
            t += 1


# get input:
n = int(input())
L = list(map(int, input().split()))
eval(n, L)
