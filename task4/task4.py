import sys
import statistics


f = open(sys.argv[1])
l = [int(line.strip()) for line in f]
m = statistics.median_low(l)
c = 0
for index, i in enumerate(l):
    while i != m:
        if i < m:
            i += 1
            c += 1
        elif i > m:
             i -= 1
             c += 1
        else:
            l[index] = i
print(c)
f.close()


