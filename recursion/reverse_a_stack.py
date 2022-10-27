def reverse_stack(stack):
    if len(stack) == 1:
        return stack 
    temp = stack[-1]
    stack.pop()
    reverse_stack(stack)
    insert(stack,temp)
    return stack

def insert(stack, ele):
    if not stack:
        stack.append(ele)
        return stack
    temp = stack[-1]
    stack.pop()
    insert(stack,ele)
    stack.append(temp)
    return  stack

def main():
    arr = [5,4,3,2,1]
    if not arr:
        return 
    st = reverse_stack(arr)
    print(st)

if __name__ == "__main__":
    main()
