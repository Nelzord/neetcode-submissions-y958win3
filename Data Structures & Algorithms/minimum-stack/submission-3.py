class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.curMin = None

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.curMin is None:
            self.minstack.append(val)
            self.curMin = val
        else:
            self.curMin = min(val, self.curMin)
            self.minstack.append(self.curMin)

    def pop(self) -> None:
        self.stack.pop(len(self.stack) - 1)
        self.minstack.pop(len(self.minstack) - 1)
        if len(self.minstack) > 0:
            self.curMin = self.minstack[-1]
        else:
            self.curMin = None

    def top(self) -> int:
        return(self.stack[-1])
        

    def getMin(self) -> int:
        return(self.minstack[-1])

        
