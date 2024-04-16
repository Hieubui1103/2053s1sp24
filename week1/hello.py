#
# Function to print a quote from The Simpsons episode titled
# Bart vs. Thanksgiving.
#
def print_simpsons_quote():
 print("Operator, what's the number for 9-1-1?") # s2, ep7
 print(' - Homer Simpson')
# Main program
print_simpsons_quote()

print('He said "Hi" to his friend.')
print("She's a great dancer.")
name = "Hieu"
title = "Projects"
sentence = 'Without' + name + 'there would be no' + title + '.'
print(sentence)
m = 2**4
print(m)
m = pow(2,4)

# if statements
y = 1
x = -1
if (x<1) : 
    x = 1
    x += 10
    print(x)
    print(" x was negative")

print("outside of if statement")

if x < 0 and y == 1 :
   print("x negative and y is 1")

if x < 0 or y == 1 :
   print("x negative and y is 1")

#loops

nums = [10,20,30,40,50]
for i in range(2,len(nums)):
   print(nums[i])

for num in nums:
   num += 5
   print(num)

print(nums)
print()

for i, val in enumerate(nums):
   print("i is ", i, "and val is", val)

dogs = ["boomer","rocky","daisy"]

for i in range(len(dogs)):
   print(i, end=" ")
print()
for dog in dogs: 
  dog+=" is happy"
  print(dog)

for a,b in enumerate(dogs):
   print(a," is the index of ",b)

num1 = [1,2,3,4,5]

sum = 0
for num in num1:
   sum += num
print("the sum of the list:",sum)
print(f"the sum of the list: {sum}")

#functions

def hello(name):
   print("Hello", name)
hello("Bob")

##default functions

def Hello1(name = "friend"):
   print("Hello",name)
Hello1()
Hello1("Bob")

subtotal = 10
statement = "The subtotal is" + str(subtotal)
title = "AnythingWeNeedSoFar"

print(title[4])

##negative index for counting backward

print(title[-1])
print(title[-4])


print()
#repition

print('python ' * 7)
print(15 * '#') #the order doesn't matter, as long as they are a string and an integer 

#compare strings

magician = 'một thằng ất ơ nào đó'
if magician == 'Harry Houdini':
   print("World's greatest magician")
else: 
   print(magician)

#string methods:

name  = "John"
print(name.upper())

course = "Platform computing"
print(course[0:7])
print(course[9:18])

print(course[:])

# Exercise
swap = [0,3,4,5,8]
t = swap[2]
swap[2] = swap[4]
swap[4] = t
print(swap)

number = [10,20,30,40,50]

for i in range(2,-1,-1):
   print(number[i], end=" ")