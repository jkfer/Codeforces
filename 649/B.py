# https://codeforces.com/contest/1364/problem/B


def eval(n, L):
    if len(L) == 2:
        print("2")
        print(" ".join(map(str, L)))
    else:
        st = L[0]
        en = L[-1]

        # find the peak and min:
        MID = []
        for i in range(1, n-1):
            # smallest
            if (L[i] < L[i-1]) and (L[i] < L[i+1]):
                MID.append(L[i])
            elif (L[i] > L[i-1]) and (L[i] > L[i+1]):
                MID.append(L[i])

        seq = [st] + MID + [en]
        print(len(seq))
        print(" ".join(list(map(str, seq))))


# receive input:
for _ in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    eval(n, L)
