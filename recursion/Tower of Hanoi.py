def move(n,s,d,h):
    if n == 1:
        print("Move plate {} from {} to {}".format(n,s,d))
        return 
    move(n-1,s,h,d)
    print("Move plate {} from {} to {}".format(n,s,d))
    move(n-1,h,d,s)
    return 

def main():
    n = int(input())
    s = 1
    d = 3 
    h = 2 
    move(n,s,d,h)
if __name__ == "__main__":
    main()