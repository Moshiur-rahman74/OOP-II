'''
def avg(x,y):
    res=(a+b)/2
    return res
#Calculator

a=float(input("Enter 1st number:"))
b=float(input("Enter 2st number:"))

result=avg(a,b)
print("The avarage is ",result)


if result>10:
   print("good")
elif resule==10:
    print("Avarage")
else:
    print("Bad")

list1 =[1,2,3,4,5,6]
sum=0
for x in list1:
    sum+=x
    if x==4:
        break
    print(x, sum, end="      ")
'''
#This is for multiplication Calculation!!!!!!!!!!!!
a=int(input("Enter the number:"))
def multiplication(a):
    for i in range(1,11):
        if i==8:
            break
        if i==6:
            continue
        print(f"{a} * {i} = {a * i}")

m=multiplication(a)
print(m)

'''
#This is for Odd and Even Calculation!!!!!!!!!!!!
a=[10,15,20,30]
def ll(a):
    even = 0
    odd = 0
    for x in a:
        if x%2==0:
            even+=1
        else:
            odd+=1
    print(even,odd)
ll(a)

'''
list0=['a','s','d','f','g','h']
print(list0)
print(list0[2])
print(list0[-4])
print(list0[1:4])
print(list0[2:])
if "apple" in list0:
  print("Yes, 'apple' is in the fruits list")

'''
list1=[5,9,3,7,9,1]
print(list1[-1],list1[3])
print('Length: ',len(list1))
list1[2] = 30
print(list1)
list1.insert(3, 70)
print(list1)
list1.pop(4)
print(list1)
list2 = list1.copy()
print(list2)
list1.extend(list2)
print(list1)
list1.sort()
print(list1)
'''
