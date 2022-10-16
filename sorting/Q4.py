# Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
# method. It does, however, have an elementAt ( i) method that returns the element at index i in
# 0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
# structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
# find the index at which an element x occurs. If x occurs multiple times, you may return any index.
def search(arr,t,left, right):
    while left < right:
        mid  =  left + (right  - left) // 2 
        if arr[mid] >= t:
            right = mid 
        else:
            left = mid + 1
    if arr[left % len(arr)] != t:
        return -1 
    return left 

def main():
    # arr is very large
    right = 1 
    while right < t :
        right *= 2
    left = 0 
    search(arr, t, left, right)

if __name__ == "__main__":
    main()