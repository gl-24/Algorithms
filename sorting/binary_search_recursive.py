def binary_search(arr,left, right, target):
    if left > right:
        return -1
    mid = left + (right) // 2 
    if arr[mid] == target:
        return mid 
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid+1, right, target)
    
def main():
    arr = [2,3,5,6]
    target = 5 
    index = binary_search(arr,0,len(arr), target)
    print(index)

if __name__ == "__main__":
    main()


