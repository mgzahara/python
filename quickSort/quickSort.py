import random
import sys
import timeit

def part(low, high, pivot):

    global arr

    while (low != high):#while low index is not at high index

        while (arr[high] > arr[pivot] and low != high):
            #while (value at high index > value at pivot index) AND (low index pos != high index pos)
            high = high - 1

        while (arr[low] <= arr[pivot] and low != high):
            #while (value at low index < value at pivot index) AND (low index pos != high index pos) 
            low = low + 1

        if (low != high):
            #if kicked out of both while loops above, one of the following is true
                #low index and high index are the same
                #low index reached a value greater than pivot value AND high index reached a value less than pivot value
            #if the later is true, swap the two values and move on
            hold = arr[low]
            arr[low] = arr[high]
            arr[high] = hold

    #switch pivot point into its position
    hold = arr[low]
    arr[low] = arr[pivot]
    arr[pivot] = hold

    return low

def findPivot(num1, num2, num3):
    global arr
#numX are indecies for the list arr
    mo3Values   = [arr[num1], arr[num2], arr[num3]]
    mo3Indecies = [num1, num2, num3]
    sortedValues    = []
    soertedIndecies = []

    low = 0 #low is the index of the lowest value of the 3 passed

    if(mo3Values[1] < mo3Values[low]):
        low = 1
    if(mo3Values[2] < mo3Values[low]):
        low = 2
    #low is now the index of the lowest value of the 3 given
    mo3Values.pop(low) #remove from consideration
    mo3Indecies.pop(low)
    low = 0
    if(mo3Values[1] < mo3Values[low]):
        low = 1

    return mo3Indecies[low] #returns the proper index to use

def quickSort(bottom, top):
    #bottom -> lowest  valid index for this step
    #top    -> highest valid index for this step

    global arr

    if((top - bottom) < 1):
        return#empty partition
    if((top - bottom) == 1):#only 2 items in this partition
        if(arr[bottom] < arr[top]):
            return#in proper order
        if(arr[bottom] > arr[top]):
            hold = arr[bottom]
            arr[bottom] = arr[top]
            arr[top] = hold
            return#switch to proper order

    mid = bottom + ((top - bottom) / 2)
    medianOfThree = findPivot(bottom, mid, top)

    #place MO3 pivot into the proper place to be utilized by part()
    temp = arr[bottom]
    arr[bottom] = arr[medianOfThree]
    arr[medianOfThree] = temp

    #pivot was just placed into the "bottom"-th place with the above instruction
    #therefore, the index of the pivot value is now found at the index "bottom"
    #therefore, the index at which to start the "low" soldier will be bottom + 1
    pivotPlacedIn = part(bottom + 1, top, bottom)

    quickSort(bottom, pivotPlacedIn - 1)#sort smaller

    quickSort(pivotPlacedIn + 1, top)#sort larger
    
    return


f = open("tenThousandDataPoints.dat", "r")
arr = f.readlines()
f.close()
#clean up data and convert to ints
for j in range(len(arr)):
    arr[j] = int(arr[j].rstrip())

start = timeit.default_timer()

quickSort(0, len(arr) - 1)

end = timeit.default_timer()

#print "\n DONE \n------"
#for a in range(len(arr)):
#    print str(a) + ". " + str(arr[a])

print "quickSort took " + str(end - start) + " seconds"
