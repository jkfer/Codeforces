# https://codeforces.com/contest/1367/problem/A


def eval(S):
    if len(S) <= 2:
        return S

    s = S[0]
    for i in range(1, len(S), 2):
        if i % 2 != 0:
            s += S[i]

    return s


# get input:
for _ in range(int(input())):
    S = input()
    print(eval(S))
