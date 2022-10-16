# Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.
# EXAMPLE
# lnput:findSin{lS, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)

def search(arr,t,left,right):
    while left < right :
        mid  = left + (right - left) // 2 
        if arr[mid] >= t:
            right = mid 
        else:
            left = mid + 1
    if arr[left % len(arr)] != t:
        return -1
    return left 

def min_element(arr):
    left,right = 0, len(arr) - 1
    while left < right :
        mid  = left + (right - left) // 2 
        if arr[mid] < arr[right]:
            right  = mid 
        else:
            left = mid + 1
    return left 

def main():
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    t = 8 
    pos = min_element(arr)
    ind1 = search(arr,t,0,pos)
    ind2 =search(arr,t,pos, len(arr))
    if ind1 != -1:
        return ind1
    elif ind2 != -1:
        return ind2 
    else:
        return -1

if __name__ == "__main__":
    main()