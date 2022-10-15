def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2 
        if arr[mid] >= target:
            right = mid 
        else:
            left = mid+1 
    if arr[left % len(arr)] != target: 
        return -1 
    return left 

def main():
    arr = [2,5,7,9]
    target = 9 
    index = binary_search(arr, target)
    print(index)

if __name__ == "__main__":
    main()