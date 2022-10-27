def delete_middle_element_of_stack(stack,k):
    if k == 1:
        stack.pop()
        return 
    temp = stack[-1]
    stack.pop()
    delete_middle_element_of_stack(stack,k-1)
    stack.append(temp)
    return stack
    
def main():
    st = [1,2,3,4,5]
    k = (len(st) // 2 )+ 1 
    if not st:
        return 
    stack = delete_middle_element_of_stack(st,k)
    print(stack)
if  __name__ == "__main__":
    main()