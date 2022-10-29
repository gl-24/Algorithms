def solve(arr,k,index):
    if len(arr) == 1:
        print(arr[0])
        return  
    index = (index + k )  % len(arr)
    arr.pop(index)
    solve(arr,k,index)  

def main():
    n = int(input())
    arr = list(range(1,n+1))
    k = int(input())
    k = k - 1
    index = 0
    solve(arr,k,index)

if __name__ == "__main__":
    main()