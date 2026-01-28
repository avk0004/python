class Employee:
    def __init__(self,name,emp,status,role):
        self.Name = name
        self.id = emp
        self.Status = status
        self.role = role
    def Display(self):
        if self.Status== 'Active':
            return "Name is ",self.Name,"Employee id",self.id
        else:
            return False
class Developer(Employee):
    def __init__(self, name, emp, status,role,exp):
        super().__init__(name, emp, status,role)
        self.exp= exp
    def Display(self):
        x = super().Display()
        if x:
            if self.role == 'D':
                level = "Senior" if self.exp >=4 else "Junior"
                print(f"{x}:level {level}")
            else:
                print("Not Belong to developer")
        else:
            print("Not Active")
class Manager(Employee):
    def __init__(self,name,emp,status,role,team_size):
        super().__init__(name,emp,status,role)
        self.size = team_size
    def Display(self):
        x = super().Display()
        if x:
            if self.role == 'M':
                return (f"{self.Name} Size{self.size}")
            else:
                return ('Not Manger')
        else:
            return ("Not Active")
manager = Manager('Anandha',101,'Active','M',10)
employees = [
    Developer("Anandha", 101, "Active", "D", 5),
    Manager("Rahul", 102, "Active", "M", 8),
    Developer("Priya", 103, "Inactive", "D", 2)
]

for emp in employees:
    print()
    emp.Display()

