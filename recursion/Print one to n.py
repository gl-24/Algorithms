'''
IBH : Induction Base Hypothesis Method
'''
def print_one_to_n(n):
    if n == 1: 
        print(1) 
        return 
    print_one_to_n(n - 1)
    print(n) 

def main():
    print_one_to_n(10)

if __name__ == "__main__":
    main()
    