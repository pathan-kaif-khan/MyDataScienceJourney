# Table program 

num = int(input("Enter the number: "))

for i in range(1,11):
  print(f" {i} X {num} = {i * num}")

# greet all the person names stored in a list ‘l’ and which starts with S
l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
  if i[0] == "S":
    print(f"Hey {i}")

#Attempt problem 1 using while loop
num = int(input("Enter the number: "))
i = 1
while i <= 10:
  print(f" {i} X {num} = {i * num}")
  i += 1

#Write a program to find whether a given number is prime or not
num = int(input("Enter number: "))

for i in range (2,num):
  if (num % i == 0 ):
    print('Number is not prime')
    break
else:
   print("number is prime")
   
#find the sum of first n natural numbers using while loop.
num = int(input("number: "))
sum = 0
current = 1
while current <= num:
  sum += current
  current+=1
print(f"The sum of the first {num} natural numbers is {sum}")

#Write a program to calculate the factorial of a given number using for loop
num = int(input("Enter number: "))
product = 1
for i in range(1,num+1):
  product = product * i
print(product)

#a program to print the following star pattern
num = int(input("Enter number: "))
for i in range(1,num+1):
  print(' '*(num-i),end="")
  print('*'*(2*i-1),end="")
  print("")

#Write a program to print the following star pattern
num = int(input("Enter number: "))
for i in range(num):
  print("*" * (i+1))
#Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *

num = int(input("Enter number: "))
for i in range(1,num+1):
  if(i ==1 or i ==num):
      print("*" *num,end="")
  else:
      print("*",end="")
      print(" "*(num-2),end="")
      print("*",end="")
  print("")

#Write a program to print multiplication table of n using for loops in reversed order

num = int(input("Enter the number: "))

for i in range(10,0,-1):
  print(f" {i} X {num} = {i * num}")
















    
