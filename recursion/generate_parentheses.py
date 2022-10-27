def generate_parentheses(open,close,op,l):
    if open == 0 and close == 0:
        l.append(op)
        return  
    
    if open != 0:
        op1 = op 
        op1 += "("
        generate_parentheses(open-1,close,op1,l)

    if close > open:
        op2 = op 
        op2 += ")"
        generate_parentheses(open,close-1,op2,l)
    
    return l 

def main():
    n = 3 
    open = close = 3 
    op = ""
    l = []
    lst = generate_parentheses(open,close,op,l)
    print(lst)
if __name__ == "__main__":
    main()