from student import StudentID
student1 = StudentID("Hieu","Bui",12345678,8)
print(student1)

student1.greeting()
for i in range(3):
    student1.take_exam()
print("Energy level of student: " + str(student1.get_energy_level()))