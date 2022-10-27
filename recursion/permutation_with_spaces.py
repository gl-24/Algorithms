'''Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.
The output should be printed in sorted increasing order of strings
Input:
S = "ABC"
Output: (A B C)(A BC)(AB C)(ABC)
Explanation:
ABC
AB C
A BC
A B C
These are the possible combination of "ABC".
'''

def permutation_with_spaces(ip:str,op:str):
    if len(ip) == 0:
        print(op)
        return 
    op1 = op2 = op
    op2 += "_"
    op2 += ip[0]
    op1 += ip[0]
    ip = ip[1:]
    permutation_with_spaces(ip,op1)
    permutation_with_spaces(ip,op2)
    return 

def main():
    ip = "ABC"
    op = ""
    op+=ip[0]
    ip = ip[1:]
    permutation_with_spaces(ip,op)

if __name__ == "__main__":
    main()