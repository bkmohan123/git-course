class Student:
    def __init__(self,p,t,r):
        self.p=p
        self.t=t
        self.r=r
    def SMP(self):
        si=(self.p*self.t*self.r)/100
        print(si)
S1=Student(10000,2,10.5)
S1.SMP()
