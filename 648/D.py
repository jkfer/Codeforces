# https://codeforces.com/contest/1365/problem/D

import collections


def dfs(M, visited, r, c):
    visited[r][c] = True
    D = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    for dr, dc in D:
        R = r + dr
        C = c + dc

        if (R >= 0 and R < len(M)) and (C >= 0 and C < len(M[0])) \
                and not visited[R][C]:
            if M[R][C] == '.' or M[R][C] == 'G':
                dfs(M, visited, R, C)


def inspect(M, r, c):
    D = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    for dr, dc in D:
        R = r + dr
        C = c + dc

        if (R >= 0 and R < len(M)) and (C >= 0 and C < len(M[0])):
            if M[R][C] == "G":
                return "No"
            elif M[R][C] == ".":
                M[R][C] = '#'


def eval(M, R, C):
    GOOD = collections.defaultdict(bool)
    impossible = False

    for r in range(R):
        for c in range(C):
            if M[r][c] == 'G':
                GOOD[(r, c)] = True
            elif M[r][c] == 'B':
                ans = inspect(M, r, c)
                if ans and ans == "No":
                    impossible = True
                    break

    if impossible:
        return 'No'
    elif M[R-1][C-1] == '#':
        if len(GOOD.keys()) == 0:
            return 'Yes'
        else:
            return 'No'
    else:
        new_visited = [[False for _ in range(C)] for _ in range(R)]
        dfs(M, new_visited, R-1, C-1)

        for n in GOOD:
            r, c = n
            if not new_visited[r][c]:
                return 'No'

        return 'Yes'


# receive the input:
for i in range(int(input())):
    R, C = list(map(int, input().split()))
    M = []
    for _ in range(R):
        M.append(list(input()))
    print(eval(M, R, C))
