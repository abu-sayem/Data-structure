class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item) - 1]

    def size(self):
        return len(self.item)

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())