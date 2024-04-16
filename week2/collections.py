lst = [6,7,10,20,50]

print(lst)
lst = lst[1:]
index3 = lst.index(7)
print(index3)

lst.append(20)
lst.append(20)
lst.append(20)
print(lst)

num20 = lst.count(20)
print(num20)

lst_copy=lst
print(lst_copy)
lst_copy[1] = 99
print(lst_copy)

print("originial list", lst)

new_copy = lst.copy()
print(new_copy)
new_copy[0] = 1000
print(lst)
print(new_copy)

new_copy = lst[:]

empty_list = []
for val in lst:
    empty_list.append(val)

print(empty_list)

empty_list = [0] * 10
print(empty_list)
empty_list[1] = 100
print(empty_list)

squares = []
for i in range(1,10):
    squares.append(i**2)
print(squares)

plus_5 = [x+5 for x in lst]
print(plus_5)

small_vals = [val for val in lst if val < 20]
print(small_vals)

#dictionaries

fav_foods = {"Kathleen" : "pizza","Maya" : "ice cream", "Tom":"ice cream","Eric":"steak"}

print(fav_foods)

mff = fav_foods["Maya"]
print(mff)

for key in fav_foods:
    print(f"{key}'s favourite food is {fav_foods[key]}")

for person, food in fav_foods.items():
    print(f"{person}'s favourite food is {food}")

#print(fav_foods['Bob'])

if "Bob" in fav_foods:
    print(fav_foods['Bob'])
else:
    fav_foods['Bob'] = 'wings'
print(fav_foods)