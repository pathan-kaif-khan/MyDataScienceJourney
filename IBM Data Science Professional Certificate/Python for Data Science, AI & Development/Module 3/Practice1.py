### Q1 ###
'''
Challenge 1: The Movie Ticket (Beginner)
Write a program that takes a person's age as input.

If they are under 13, print "Child ticket: $5".

If they are between 13 and 64 (inclusive), print "Adult ticket: $12".

If they are 65 or older, print "Senior ticket: $8".
'''
age = int(input("Enter your Age: "))
if age < 13:
    print("Child ticket : $5")
elif 13 <= age <=64:
    print("Adult ticket : $12")
else:
    print("Senior ticket : $8")

### Q2 ###
'''
Challenge 2: The Leap Year (Intermediate)
Write a program that takes a year as input and determines if it is a leap year. Here are the rules:

A year is a leap year if it is divisible by 4.

Except if it is divisible by 100 (then it is not a leap year).

Unless it is also divisible by 400 (then it is a leap year).
'''
year = int(input("enter year"))

if (year %4 == 0 and year %100 != 0) or year %400 == 0:
    print("leap year")
else:
  print("Not a leap year")

### Q3 ###
'''
Challenge 3: The Secret Vault (Advanced)
Write a program for a security vault that checks three variables: hasKeycard (boolean),
knowsPin (boolean), and timeOfDay (number from 0 to 23).

The vault opens only if the user has the keycard AND knows the PIN.

However, if the timeOfDay is between 0 and 5 (midnight to 5 AM), 
the vault is in lockdown mode and requires an additional override. If they try to open it during lockdown, 
print "Lockdown active: Access denied."

Otherwise, if they have the right credentials, print "Vault opened." If they lack the credentials,
print "Alarm triggered!"
'''
haskey = True
knowspin = True
timeofday = 4

if haskey and knowspin:
  if 0 <=timeofday <=5:
    print("Lockdown active: Access denied")  
  else:
    print("Vault opened.")
else:
    print("Alarm triggered!")
