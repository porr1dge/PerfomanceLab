import sys
n, m = sys.argv[1:]
n = int(n)
m = int(m)
i = 1
c = 1
f = 0
while i <= n:
    if i == 1 and c == m:
        break
    if i == 1 and f == 0:
        print(i, end='')
        f = 1
    if c == m:
        print(i, end='')
        c = 1
        continue
    if i == n:
        i = 0
    i += 1
    c += 1