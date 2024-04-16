class StudentID:
    def __init__(self, fname, Iname,id, energy_level = 10):
        self.fname = fname
        self.Iname = Iname
        self.id = id
        self.energy_level = energy_level
    
    def __str__(self):
        return f"{self.Iname}: {self.id}"
    
    def greeting(self):
            print(f"Hi, my name is {self.fname} {self.Iname}!")

    def take_exam(self):
        self.energy_level -= 1

    def get_energy_level(self):
        return self.energy_level
    
