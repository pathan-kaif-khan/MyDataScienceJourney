#Quick Revision of Python basics 

#Tuple
x=(1,'a',2,'b',3)
print(type(x))

#List
x=[1,'a',2,'b',3]
print(type(x))

x.append(43)
print(x)
  #For loop
for item in x:
    print(item)
  #While loop
i=0
while( i!= len(x)):
   print(x[i])
   i = i + 1
#
a=[1,2] + [3,4]
print(a)

b=[1] * 3
print(b)

c=1 in [1,2,3]
print(c)

#String 
z='This is string'
print(z[0])
print(z[0:1])
print(z[0:2])

print(z[-1])
print(z[-4:-2])
print(z[:3])
print(z[3:])

Firstname='Alex'
Lastname='Bill'
print(Firstname +' '+Lastname)
print(Firstname * 3)
print('Alex' in Firstname)

Firstname='Alex Volk Islam Khabib'.split(' ')[0]
Lastname='Bill Aspinal Jones Pin'.split(' ')[-1]
print(Firstname)
print(Lastname)

#Dict
x={'Ayan' :'Ayank.edu' ,'Zaid' : 'Zaidk.edu'}
print(x)
print(type(x))
print(x['Ayan'])
print("*************************")

for name in x:
    print(x[name])

print("*************************")
for name, email in x.items():
    print(name)
    print(email)
