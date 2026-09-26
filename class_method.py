class Myclass:
    @classmethod
    def Stcl(cls,arg1,arg2):
        cls.arg1=arg1
        cls.arg2=arg2
        print(arg1*arg2)

cl1 = (Myclass.Stcl(10,5))
print(cl1)

