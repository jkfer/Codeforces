# https://codeforces.com/contest/1364/problem/A


def eval(a, na, x):
    i = 0
    all_divisible = True
    sum = 0

    # Make the sum array:
    while i < len(a):
        sum += a[i]

        if a[i] % x != 0:
            all_divisible = False

        i += 1

    if sum % x != 0:
        return len(a)

    if all_divisible:
        return -1

    start = 0
    end = len(a) - 1

    while (a[start] % x == 0) or (a[end] % x == 0):
        if a[start] % x == 0:
            start += 1

        if a[end] % x == 0:
            end -= 1

    return max(len(a)-start-1, end)


# receive input:
for _ in range(int(input())):
    na, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(eval(a, na, x))
