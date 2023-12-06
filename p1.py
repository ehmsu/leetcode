# # Problem
# Imagine you want to build an application that can visually show data on a graph. Data is sporadic in practice, so we want to be able to smooth it out when we’re visualizing it using configurable overlapping intervals. (For this question you will implement a very basic "smoothing" function)

# Write a function that given an array of integers and an interval length, can calculate the sum of the each of the overlapping intervals contained in the input array.

# ([1,3,2,4,6,5], 3) => [6,9,12,15]

# Visually:
# [1,3,2] => 6
#   [3,2,4] => 9
#     [2,4,6] => 12
#       [4,6,5] => 15


# So imagine that we might want multiple views of this data. One for sum, but we are also interested in localized spikes in the data. Can you create another function with the same input, but instead of sum returns a max for each window?


#old 
def smooth_old(arry, interval): 
    if interval > len(arry) or interval < 0: 
        return 0 
    i = 0 
    returnList = []
    while (i + interval) <= len(arry): 
        returnList.append(sum(arry[i:(i+(interval))]))
        i += 1
    
    return returnList

#new, uses running sum (investigate afterwards)
def smooth_new(arry, interval): 
    if interval > len(arry) or interval < 0: 
        return 0
    runningSum = 0 
    
    for i in range(0,interval):
        runningSum += arry[i]
    returnList = [runningSum]
    i = 1
    while (i + interval) < len(arry): # i = 2 , 2
        runningSum = runningSum - arry[i-1] + arry[i+interval]
        returnList.append(runningSum)
    
    return returnList

# loop 

# use list or set to find max of first 0 - interval entries 
# remove the smallest element from the list add the new largest element in the list 

# output array adds the max of the above list 
# can also use heap (slightly more inefficient)

if __name__ == "__main__": 
    print(smooth_old([1, 3, 2, 4, 6, 5], 3))
    print(smooth_new([1, 3, 2, 4, 6, 5], 3))