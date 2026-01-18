class A:
    def __init__(self, other):
        self.op = other
    @staticmethod
    def fea1():
        print("Hi")
    @classmethod
    def fea(cls,o1, p):
        return cls(o1.op + p)
M = A(20)
N = A.fea(M,50)
print(N.op)
M.fea1()