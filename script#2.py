#Ordenar tres stacks paso a paso
import string
    stack1 = [1,2,3]
    stack2 = [5,4]
    stack3 = []

stack3.append(stack1.pop())
stack3.append(stack1.pop())
stack3.append(stack1.pop())
stack1.append(stack2.pop())
stack2.append(stack3.pop())
stack1.append(stack3.pop())
stack1.append(stack2.pop())
stack2.append(stack3.pop())
stack3.append(stack1.pop())


print (stack1)
print (stack2)
print (stack3)
