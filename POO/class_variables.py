# Class variables

class A:
    vc = 1234
    
    def __init__(self):
        self.vc = 321
    
a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)
print(A.vc)
