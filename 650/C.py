# https://codeforces.com/contest/1367/problem/C
# Referred solution


def find_count(s, i, j, k, v):
    n = 0
    if v == "left":
        for _ in range(i, j - k + 1, k):
            n += 1
    elif v == "right":
        for _ in range(i + k - 1, j, k):
            n += 1
    elif v == "mid":
        for _ in range(i + k - 1, j - k + 1, k):
            n += 1
    else:
        # v is "all"
        for _ in range(i, j, k):
            n += 1

    return n


def eval(n, k, s):
    i = 0
    m = 0

    while i < len(s):
        if s[i] == '0':
            j = i
            while j < len(s) and s[j] == '0':
                j += 1

            if i == 0 and j == len(s):
                # All numbers are "0"
                # print("all")
                m += find_count(s, i, j, k+1, "all")
            elif i == 0:
                # print("left")
                m += find_count(s, i, j, k+1, "left")
            elif j == len(s):
                # print("right")
                m += find_count(s, i, j, k+1, "right")
            else:
                # print("mid")
                # print(i, j, k+1)
                m += find_count(s, i, j, k+1, "mid")
            i = j
        else:
            i += 1

    return m


# Receive input:
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    print(eval(n, k, s))
