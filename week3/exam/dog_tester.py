#Hieu Bui 
#task 2
from dog import Dog
print()
dog_list = []
with open("dogs.txt") as file:
    for line in file:
        line=line.strip()
        tokens = line.split()
        dog_ins = Dog(tokens[0],tokens[1],tokens[2],bool(tokens[3]))
        print(dog_ins)
        dog_list.append(dog_ins)

print()
# task 3
print(dog_list[0].get_name())
print(dog_list[0].get_breed())
print(dog_list[0].get_trick())
print(dog_list[0].isHungry())

print()

# task 4
dog_list[0].speak()
dog_list[0].feed()
dog_list[0].change_trick("fetch")

print()

# task 5
print(dog_list[0].get_name())
print(dog_list[0].get_breed())
print(dog_list[0].get_trick())
print(dog_list[0].isHungry())