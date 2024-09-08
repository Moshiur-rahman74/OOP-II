'''
a=(1,2,5,7,4)
print(len(a),type(a))
print(a)
print(a[-2],a[2])
b=list(a)
b[-3]=50
print(b)
print(b[-4:-1])
b.append(100)
print(b)
b.insert(2,400)
print(b)
b.pop()
print(b)
b.pop(1)
print(b)
c=(2,4,6)
b.extend(c)
print(b)
b.sort()
print(b)
b.sort(reverse=True)
print(b)
print(b[::-1])
x=sorted(b)
print(x)
for x in b:
    print(x , end=" , ")


#Dictionalry
z={
    "name":"A",
    "age":40,
    "type": {"developer":["ios","android"]},
    "parmanent":"true",
    "salary": 30000,
    100: (1,2,3),
    4.5:{5,6,"True",7,1}
}

print(len(z),type(z))
print(z["type"]["developer"])
print(z[4.5])
z["parmanent"]="False"
z["Gender"]="Male"
z.pop("age")

print(z)
print(z.keys())
print(z.values())
for x in z.keys():
    print(x)
for x in z.values():
        print(x)
for x in z.items():
    print(x)
for x in z:
    print(x,z[x])

a={1,3,5,8,5,2}
b={0,"False",1,5}
print(a,b)
print(len(a),type(a),len(b),type(b))
a.add(10)
b.add(10)
a.remove(8)
print(a,b)
q=a.union(b)
w=a.intersection(b)
e=a.difference(b)
print(q,w,e)
for x in a:
    print(x)
for x in a:
    if x == 5:
        break
    print(x)
j=[2,3,4]
h=a.union(j)
print(h)
'''