# https://codeforces.com/contest/1365/problem/B

import collections


def eval(k, j):
    # Evaluate the type of items in j:
    D = collections.defaultdict(int)
    i = 0
    while i < len(j):
        if j[i] == 1:
            D[1] += 1
        elif j[i] == 0:
            D[0] += 1

        # two types found
        if D[1] > 0 and D[0] > 0:
            return 'Yes'

        i += 1

    # If we have reached here - the numbers in k should be in order:
    i = 1
    while i < len(k):
        if k[i-1] <= k[i]:
            i += 1
        else:
            return 'No'

    return 'Yes'


# get input;
for _ in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    j = list(map(int, input().split()))
    print(eval(k, j))
