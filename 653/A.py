# https://codeforces.com/contest/1374/problem/A


def eval(x, y, n):
    R = n % x
    ans = n - R + y
    if ans < 0:
        return 0
    else:
        if ans > n:
            ans -= x
            return ans
        else:
            return ans


for _ in range(int(input())):
    x, y, n = list(map(int, input().split()))
    print(eval(x, y, n))
