# write down a decorator program
# 1. define a decorator function
def decorator(func):
    # 2. define a function to be decorated
    def inner_function():
        print("This is before function execution")
        # 3. decorate the function
        func()
        print("This is after function execution")
    return inner_function

# define a function to be decorated
@decorator
def function_to_be_decorated():
    print("This is inside the function")
