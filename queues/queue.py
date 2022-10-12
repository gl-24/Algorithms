from collections import deque
class Queue:
    
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data) -> None:
        self.queue.append(data)
    
    def dequeue(self) -> int:
        x = self.queue.popleft()
        return x
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def __str__(self):
        return str(self.queue)
    
def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())

if __name__ == "__main__":
    main()