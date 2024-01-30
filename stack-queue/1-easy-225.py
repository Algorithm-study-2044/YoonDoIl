class MyStack:

    def __init__(self):
        self.queues = [[],[]]

    def push(self, x: int) -> None:
        if self.queues[0]:
            self.queues[0].append(x)
        else:
            self.queues[1].append(x)

    def pop(self) -> int:
        if self.queues[0]:
            for i in range(len(self.queues[0])-1):
                self.queues[1].append(self.queues[0][i])
            ret = self.queues[0][-1]
            self.queues[0] = []
            return ret 
        else:
            for i in range(len(self.queues[1])-1):
                self.queues[0].append(self.queues[1][i])
            ret = self.queues[1][-1]
            self.queues[1] = []
            return ret 

    def top(self) -> int:
        if self.queues[0]:
            for i in range(len(self.queues[0])):
                self.queues[1].append(self.queues[0][i])
            ret = self.queues[0][-1]
            self.queues[0] = []
            return ret 
        else:
            for i in range(len(self.queues[1])):
                self.queues[0].append(self.queues[1][i])
            ret = self.queues[1][-1]
            self.queues[1] = []
            return ret 

    def empty(self) -> bool:
        return (len(self.queues[0])==0) and (len(self.queues[1])==0)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
