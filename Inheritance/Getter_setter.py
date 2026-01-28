class Employee:
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if value=="":
            raise ValueError("Not NULL VALUE") 
        self._name = value
    @property
    def salary(self):
        
        return self._salary

    @salary.setter
    def salary(self,value):
        if value=="":
            raise ValueError("Not NULL VALUE") 
        self.salary = value