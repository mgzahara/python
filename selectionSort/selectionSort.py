import timeit
import time
import random

base = []

#f = open("hundredDataPoints.dat", "r")
#base = f.readlines()

f = open("tenThousandDataPoints.dat","r")
base = f.readlines()
f.close()
#clean up data and convert to ints
for j in range(len(base)):
    base[j] = int(base[j].rstrip())

#print "original\n---------"
#for y in range(len(base)):
#    print str(y) + ". " + str(base[y])

start = timeit.default_timer()

for i in range(len(base) - 1):
    low = i

    for j in range(i, len(base)):
        if(base[j] < base[low]):
            low = j
    base[i], base[low] = base[low], base[i]

end = timeit.default_timer()

print "selection sort took " + str(end - start) + " seconds"

#print "sorted\n-------"
#for z in range(len(base)):
#    print str(z) + ". " + str(base[z])
