# https://codeforces.com/contest/1365/problem/C


import collections


def eval(N, D1, D2):
    d1 = dict()
    d2 = dict()

    for i in range(N):
        d1[D1[i]] = i
        d2[D2[i]] = i

    Da = collections.defaultdict(int)
    Db = collections.defaultdict(int)

    for i in D1:
        # right move
        dd = d1[i] - d2[i]
        if dd == 0:
            l1 = 0
        elif dd < 0:
            l1 = dd + N
        else:
            l1 = dd

        # Left move
        dd2 = d2[i] - d1[i]
        if dd2 == 0:
            l2 = 0
        elif dd2 < 0:
            l2 = dd2
        else:
            l2 = dd2 - N

        Da[l1] += 1
        Db[l2] += 1

    print(max(max(Da.values()), max(Db.values())))


# collect input:
N = int(input())
D1 = list(map(int, input().split()))
D2 = list(map(int, input().split()))
eval(N, D1, D2)
