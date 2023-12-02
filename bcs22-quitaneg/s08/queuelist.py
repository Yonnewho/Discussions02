class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.QList = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            print("The list is full or overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.QList[self.rear] = item
        self.size = self.size + 1
        print("%s added to the list" % str(item))

    '''def dequeue(self):
        if self.isEmpty():
            print('The list is empty or underflow')
            return
        item = self.QList[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1
        print("%s dequeued" % str(item))'''

    def queueFront(self):
        if self.isEmpty():
            print("Queue is empty.")
        print("Front item is ", self.QList[self.front])

    def queueRear(self):
        if self.isEmpty():
            print("Queue is empty.")
        print("Rear item is ", self.QList[self.rear])

if __name__ == '__main__':
    queue = Queue(5)

    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(25)
    queue.enqueue(1)
    queue.enqueue(250)
    queue.queueFront()
    queue.queueRear()

    
    queue.queueFront()
    queue.queueRear()


'''
	Mini-Activity
	Create dequeue function on this code
  
'''