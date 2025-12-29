#LEGB  - Local, Enclosing, Global, Built-in
# Local Variables - that are defined and accessed inside the function, can not be accessed outside the function
# def show():
#     x = "Ram"
#     print(x)
# show()
# GLobal Variables - that are defined outside the function, can be accessed inside or outside the function
# x = "Shyam"  
# def show():
#     x = "Ram"  # local variable
#     print(x)
# show()
# print(x)  # accessing global variable outside the function
# GLobal Keyword - to access and modify global variable inside the function
# x = "Shyam"  
# def show():
#     global x
#     x = "Ram"   
#     print(x)
# show()
# print(x)
# Enclosing Variables - variables in the enclosing function can be accessed by nested function
# def outer_function():
#     x = "Ram"
#     def inner_function():
#         print(x)
#     inner_function()
    
# outer_function()

# Built-in Variables - pre-defined variables in python that can be accessed anywhere
# print(len("Hello"))  # len is built-in function in python to find length of string



# lambda arguments : expressions
# num = lambda x : x + 20
# result = num(5)
# print("Result is :", result)

# num = lambda x : x ** 2
# result = num(5) 
# print("Result is :", result)

# num = lambda x,y : x + y
# result = num(5,3) 
# print("Result is :", result)

# num = lambda x,y,z : x + y * z
# result = num(5,3,2) 
# print("Result is :", result)

# def multiply(num1):
#     # product = lambda num2 : num1 * num2  # -> lambda num2 : 5 * num2
#     # return product
#     return lambda num2 : num1 * num2   # lambda num2 : 5 * 4
# result = multiply(5)
# final_result = result(4)
# print(final_result)


# def cube(x):
#     result = lambda y : x ** y   #-> lambda y : 5 ** y
#     return result  # lambda y : 5 ** 3 
# result = cube(5)
# cube_result = result(3)
# print(cube_result)