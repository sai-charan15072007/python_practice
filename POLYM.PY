class calculator:
   def add(self,a,b=0):
    return a+b
c=calculator()
print(c.add(10))
print(c.add(10,20))  


class calculator:
  def  add(self,*numbers):
    print(sum(numbers))
obj = calculator()
obj.add(10)
obj.add(10,20)
obj.add(10,20,30)
obj.add(10,20,30,40)