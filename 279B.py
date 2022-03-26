# https://codeforces.com/contest/279/problem/B

# books, minutes = input().split()
# books = int(books)
# minutes = int(minutes)

# arrMinutes = []

# arrMinutes = [int(a) for a in input().split()]

# print(arrMinutes)
# buf = 0
# cntr = 0
# j = 0
# while ((minutes > 0) and (j < len(arrMinutes) - 1)):
#     minutes -= arrMinutes[j]
#     cntr += 1
#     j += 1
#     if minutes > arrMinutes[j]:
#         buf = arrMinutes[j]

#     print("arrMinutes[", j, "] =", arrMinutes[j], "minutes = ", minutes)
#     print("counter = ", cntr)
#     print(buf)

# cntr = 0
# for i in range(len(arrMinutes)):
#     if minutes < arrMinutes[i]:
#         continue 
#     if minutes > 0 and (i < len(arrMinutes)):
#         minutes -= arrMinutes[i]
#         cntr += 1
       
# print(cntr)



books, minutes = input().split()
books = int(books)
minutes = int(minutes)
arrMinutes = []
sum = 0
s = 0
ans = 0
# 3 1 2 1 
arrMinutes = [int(a) for a in input().split()]
for k in range(books):
    sum += arrMinutes[k]
    while sum > minutes and s <= k:
        sum -= arrMinutes[s]
        s += 1
    ans = max(ans, k - s + 1)

print(ans)

