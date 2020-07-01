# https://codeforces.com/contest/1367/problem/B


def eval(n, L):
    out_of_place_even = 0
    out_of_place_odd = 0

    for i, n in enumerate(L):
        if not i % 2 == n % 2:
            if i % 2 == 0:
                out_of_place_odd += 1
            else:
                out_of_place_even += 1

    if out_of_place_even == out_of_place_odd:
        return out_of_place_even
    else:
        return -1


# receive input:
for _ in range(int(input())):
    n = int(input())
    ll = input()
    L = list(map(int, ll.split()))
    print(eval(n, L))
