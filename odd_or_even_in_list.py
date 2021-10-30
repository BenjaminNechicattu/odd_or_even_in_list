print("enter the lim")
lim=int(input())
print("enter the num")  
num=[]
for i in range (10):
    num2=int(input())
    num.append (num2)

eve=[]
odd=[]
for i in range (10):
    if i%2 ==0:
        eve.append(i)
    else:
        odd.append(i)

print ("even num is an")
print (eve)
print ("odd num is an")
print (odd)
