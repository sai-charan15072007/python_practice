#implementing stack using list
stack=[]
#pushing elements into stack
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
#pop
element=stack.pop()
print("element removed:",element)
print("stack is:",stack)
#peek/top
#to view top element without removing it
print("top elemnt:",stack[-1])
#checking whether the stack is empty
if(len(stack))==0:
    print("stack is empty")
else:
    print("stack is not empty")
#size of stack
print("size:",len(stack))     