a = 9
b = 8
#c = sum((a,b)) #Built-in function

def function1(a,b) :
    print("Hello you are in function 1",a+b)

def function2(a,b) :
    """This is a function which will calculate average of two numbers."""    #This is a docstring
    average = (a+b)/2
    print(average)
    return average

# v = function2(5,7)
# print(v)
print(function2.__doc__) 