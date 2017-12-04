import timeit
import sys
import time
import random

radixSortCount = 0

def radixSort(arr1 = [], arr2 = []):

    global radixSortCount

    for i in range(10):
        #compare to 0 - 9
        for a in range(len(arr1)):
            #look at all data
            if(len(str(arr1[a]) ) == 4):
                #999 < a < 10000
                thou = int(arr1[a] / 1000)
                hund = int(arr1[a] / 100) % 10
                tens = int(arr1[a] / 10) % 10
                ones = arr1[a] % 10
            elif(len(str(arr1[a]) ) == 3):
                #99 < a < 1000
                thou = 0
                hund = int(arr1[a] / 100)
                tens = int(arr1[a] / 10) % 10
                ones = arr1[a] % 10
            elif(len(str(arr1[a]) ) == 2):
                #9 < a < 100
                thou = 0
                hund = 0
                tens = int(arr1[a] / 10)
                ones = arr1[a] % 10
            else:
                #a < 10
                thou = 0
                hund = 0
                tens = 0
                ones = arr1[a]
                #-- put into second array --#

            if(radixSortCount == 0 and ones == i):
                arr2.append(arr1[a])
            if(radixSortCount == 1 and tens == i):
                arr2.append(arr1[a])
            if(radixSortCount == 2 and hund == i):
                arr2.append(arr1[a])
            if(radixSortCount == 3 and thou == i):
                arr2.append(arr1[a])
            
    
    radixSortCount += 1

    arr1 = []    

    if(radixSortCount < 4):
        return radixSort(arr2, arr1)
    return arr2


arr1 = []
arr2 = []

#read data into arr1 from file
#f = open("hundredDataPoints.dat", "r")
#arr1 = f.readlines()

f = open("tenThousandDataPoints.dat", "r")
arr1 = f.readlines()

#clean up data and convert to ints
for j in range(len(arr1)):
    arr1[j] = int(arr1[j].rstrip())

f.close()

start = timeit.default_timer()

done = radixSort(arr1, arr2)

end = timeit.default_timer()

print "radix sort took " + str(end - start) + " seconds"

#for d in range(len(done)):
#    print str(d) + ". " + str(done[d])

