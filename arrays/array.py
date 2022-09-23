def array_test():
    arr = [2,3,4,5,6,7]
    n = len(arr) # 6
    
    arr.append(8)
    arr.insert(0,9) #insert(index, val)
    arr.insert(0,1) 
    arr.pop()
    # del arr[0]
    arr.remove(4)
    # print(arr)
    # print(arr.index(9))
    arr = [0] * 10
    print(arr)


def main():
    array_test()

if __name__ == "__main__":
    main()
