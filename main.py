def merge():
    k = int(input())

    ls = []
    for i in range(k):
        ls += list(map(int, input().split(',')))
    ls = sorted(ls)
    return ls

print(merge())
