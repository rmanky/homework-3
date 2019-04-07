def findLargestSum(arr):

    max_sum = arr[0]
    current_max = arr[0]

    first = 0;
    last = 0;

    tempFirst = 0;
    tempLast = 0;
    
    for i in range(1, len(arr)):
        if(arr[i] > current_max + arr[i]): #current > rest
            current_max = arr[i] #max = current
            tempFirst = i #first = current index
        else:
            current_max += arr[i] #add current to the max
            
        tempLast = i #last = current index
        
        if(current_max > max_sum): #if we have a new maximum
            max_sum = current_max #set the max to our new one
            first = tempFirst #update first
            last = tempLast #and last indexes

    return max_sum, first, last #return all three

# put your array here!
array = [-81, -76, -57, -55, -35, -12, 22, 25, 75, 78]

largestSum = findLargestSum(array)[0]
first = findLargestSum(array)[1]
last = findLargestSum(array)[2]
print("Input array was", array)
print("Maximum sum is", largestSum)
print("Largest sum was the subarray", array[first:last + 1])


        
