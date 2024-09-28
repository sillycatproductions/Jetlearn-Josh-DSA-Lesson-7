class Stack(): #---------------------------------------------------------------class start
    def __init__(self,n): #calls self and number of items in stack
        self.stack = []
        self.n = n #max stack amount

    def push(self, a): #allows a to go into self.stack
        if len(self.stack) < self.n:
            self.stack.append(a)
        else:
            print('stack is full.') #only happens when self.stack >= self.n
    
    def pop(self): #allows a to get removed from self.stack
        if len(self.stack) == 0:
            print('stack is empty.') #only happens when self.stack == 0
        else:
            self.stack.pop(-1) #delete last element and bring it back later
        
    def top(self):
        if len(self.stack) == 0:
            print('stack is empty.') #go to line 14
        else:
            return self.stack[-1] #brings back the popped element
    
    def size(self):
        print('The size of the stack is',len(self.stack), '!') #fairly straightforward it prints the length of the stack

    
    def display(self):
        print(self.stack) #also fairy straitforward it prints the stack itself

#-----------------------------------------------------------------------------------class done

thing = Stack(10) #class object                 Stack(10) the ten equals the max stack amount 

for i in range(10):
 thing.push(i)  #pushes i 10 times and completely fills the stack

thing.display()  #go to line 27
thing.push(i)  #overloads the stack


thing.pop() #go to line 12
thing.display()  #go to line 27

thing.push(i) #go to line 42
b = thing.top() #go to line 16
print(b) #prints thing.top() (line 45)

thing.size() #go to line 25
