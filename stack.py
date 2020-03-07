class Stack:
    def __init__(self,size):
        self.head = -1
        self.stack = []
        self.size = size

    def isEmpty(self):
        if self.head<=-1:
            return True
        else:
            return False

    def isFull(self):
        if self.head >= self.size:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            pass
        else:
            self.head  +=1
            # print(self.head)
            self.stack.insert(self.head, value)

    
    def pop(self):
        if self.isEmpty():
            self.head -=1
            try:
                self.stack.pop()
            except:
                pass

        else:
            popped =  self.stack[self.head]
            self.head -=1
            self.stack.pop()
            return popped

    def showStack(self):
        if self.isEmpty():
            print("Err..Stack is Empty")
        else:
            print(' '.join(self.stack))
