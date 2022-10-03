#TC:O(logn) 
#SC:O(1)

def FindMissingElement(arr):
    low,high = 0, len(arr)-1 #initialize low and high pointer
    
    if arr[0] != 1: #If the first element is not equal to 1, then return 1
        return 1
    
    if arr[-1] == len(arr): #If the last element is equal to the length of arr then the last element is missing, return len(arr)+1
        return len(arr)+1
    
    while low+1 != high:   
        mid = low + (high-low) //2  #find the mid
        
        if (arr[mid]-mid) == 1: #answer is when the difference between index and element is 1
            low = mid #change low to mid
        else:   
            high = mid  #else, move high to mid
    return arr[low]+1   #low+1 points to the missing number