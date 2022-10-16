"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""
def search(A,m,B,n):
    i,j = m - 1,n - 1
    ith = m + n - 1
    while j >= 0:
        if i >= 0 and A[i] > B[j]:
            A[ith] = A[i]
            i -= 1 
        else:
            A[ith] = B[j]
            j -= 1
        ith -= 1
    print(A)
    
def main():
    A =  [1,2,3,0,0,0]
    B =  [2,5,6]
    arr = search(A,3,B,3)
    # print(arr)

if __name__ == "__main__":
    main()