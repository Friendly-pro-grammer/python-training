from math import floor
def binary_search(nums,target):
    low = 0
    high = len(nums)-1
    while(low<=high):
        mid=floor(low+(high-low)/2)
        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            low = mid+1
        else:
            high = mid-1
    return -1
        