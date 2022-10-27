def permute_string_case(ip:str,op:str) -> None:
    if len(ip) == 0:
        print(op)
        return  
    op1 = op2 = op 
    op2 += ip[0].upper()
    op1 += ip[0]
    ip = ip[1:]
    permute_string_case(ip,op1)
    permute_string_case(ip,op2)
    return 

def main():
    ip = "ab"
    op = ""
    permute_string_case(ip,op)
if __name__ == "__main__":
    main()