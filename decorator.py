def decorator(func):
    def inner(a,b):
        print("inside inner")
        func(a,b)
        print("inside decorator")
    return inner

@decorator
def sum(a,b):
    #print(a,b)
    print(a+b)
    #return result
sum(4,5)
#print(c)

