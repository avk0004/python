class Man:
    def __init__(self):
        pass
    def sound(self):
        print('Hello')
class Ani(Man):
    def __init__(self):
        super().__init__()
    def sound(self):
        print("Animal Sound")

Cls= [Man(), Ani()]
for i in Cls:
    i.sound()