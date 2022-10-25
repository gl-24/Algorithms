'''
IBH : Induction Base Hypothesis Method
'''
def print_one_to_n(n):
    if n == 1: 
        print(1) 
        return 
    print_one_to_n(n - 1)
    print(n) 

def print_n_to_one(n):
    print(n)
    
    if n == 1:
        return 
    
    print_n_to_one(n-1)

def main():
    print("One to N")
    print_one_to_n(10)
    print("N to One")
    print_n_to_one(5)

if __name__ == "__main__":
    main()
    