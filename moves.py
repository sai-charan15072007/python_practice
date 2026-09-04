 movezeroes(self,list):
        p=0
        for i in range(len(list)):
            if list[i]!=0:
               list[p]=list[i]
               p+=1
        while p<len(list):
           list[p]=0
           p+=1
