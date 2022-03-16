# https://codeforces.com/problemset/problem/706/B

def bin_srch(low, high, key, arr):
    while(low < high):
        mid = int((low + high) / 2)
        if(arr[mid] <= key):
            low = mid + 1
        else:
            high = mid
    return low

count_shop = int(input())
arr_price = [int(a) for a in input().split()]
arr_price.sort()

c = int(input())

while (c > 0):
    k = int(input())
    print(bin_srch(0,count_shop, k, arr_price))
    c -= 1