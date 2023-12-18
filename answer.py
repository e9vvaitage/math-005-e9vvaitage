def answer(n):
    num=0
    count=0
    while True:
     num=num+n
     for i in range(20,0,-1):
         num=num+n
         if num%i==0:
          count+=1
          if count==num+n:
              break         
     print(count)
    
N=int(input("enter the no."))

if __name__=='__main__':
 print(answer(N))



'''

def answer(n):
    num=0
    count=0
    while count!=18:
     
        num=num+n
        for i in range(20,2,-1):
            if num%i==0:
                count+=1
            if count==18:
                print(num)
                break
            
n=int(input("Enter the number: "))
l=[]
end=20
result=answer(n)
'''
