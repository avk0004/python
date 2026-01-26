class inher:
    def __init__(self,name):
        self.name = name
    def info(self):
        print("Name is",self.name)
class childz(inher):
    def __init__(self,name,classs):
        super().__init__(name)
        self.clz = classs
    def details(self):
        super().info()
        print("Class: ",self.clz)
Ch = childz('Anandha','1st Year')
Ch.details()
