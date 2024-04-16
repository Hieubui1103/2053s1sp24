from car import Car
cars_list = []
with open("cars.txt") as file:
    for line in file:
        line1 = line.strip()
        token = line.split()
        car_ins = Car(token[0],token[1],int(token[2]),int(token[3]))
        print(car_ins)
        cars_list.append(car_ins)

for i in range(0,2):
    print(cars_list[i])
    cars_list[i].drive()
    gallons = cars_list[i].get_gas_tank()
    mileage = cars_list[i].get_odometer()
    print(" The number of gallons of gas left: " + str(gallons))
    print(" The mileage of the car: " + str(mileage))
    print()

