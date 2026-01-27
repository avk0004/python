class Employee:
    def __init__(self,name,emp,status):
        self.Name = name
        self.id = emp
        self.Status = status
    def show_details(self):
        if self.Status== 'Active':
            return "Name is ",self.Name,"Employee id",self.id
        else:
            return False
class Developer(Employee):
    def __init__(self, name, emp, status,exp):
        super().__init__(name, emp, status)
        self.exp= exp
    def Display(self):
        x = super().show_details()
        if x:
            level = "Senior" if self.exp >=4 else "Juniot"
            print(f"{x}:level {level}")
        else:
            print("Not Active")
Emp = Developer('Anandha',2021,'Active',5)
Emp.Display()
# print(x1)