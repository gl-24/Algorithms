def subsets(ip,op):
    if len(ip) == 0:
        print(op,end = " ")
        return 
    op1 = op2 = op 
    op2 += ip[0]
    ip = ip[1:]
    subsets(ip,op1)
    subsets(ip,op2)
    return 

def main():
    ip = input()
    op = ""
    subsets(ip,op)

if __name__ == "__main__":
    main()