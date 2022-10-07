class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self,data)->None:
        self.stack.append(data)
        self.size += 1 
    
    def pop(self)->int:
        x = self.stack[-1]
        self.stack.pop()
        self.size -= 1 
        return x
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def __str__(self):
        return str(self.stack)

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())

if __name__ == "__main__":
    main()
    