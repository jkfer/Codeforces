# https://codeforces.com/contest/1365/problem/A


def eval(matrix):
    visitedR = [False] * len(matrix)
    visitedC = [False] * len(matrix[0])
    K = 0

    # traverse the matrix first:
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                visitedR[r] = True
                visitedC[c] = True

    # Now you can traverse the non visited:
    for r in range(len(visitedR)):
        for c in range(len(visitedC)):
            if not visitedR[r] and not visitedC[c]:
                K += 1
                visitedR[r] = True
                visitedC[c] = True

    # eval K
    if K == 0:
        print('Vivek')
    else:
        if K % 2 == 0:
            print('Vivek')
        else:
            print('Ashish')


# intake input
for _ in range(int(input())):
    r, j = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(r)]
    eval(matrix)
