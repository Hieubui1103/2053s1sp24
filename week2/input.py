num = int(input("Enter a number: "))
print(num)
num += 10
print(num)

try:
    num = int(input("Enter a number: "))
    print(num)
    sum = num +2
    sum += 10 #you need to have a number stored in variable "sum"
    print(sum)
except:
    print("You did not enter a number.")

with open("movies.txt") as file:
    for line in file:
        line=line.strip()
        print(line)

with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        tokens= line.split()
        print(tokens)    