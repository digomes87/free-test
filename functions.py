def function_one():
    print("Here one function")
    
def function_two():
    print("Another function !!!")
    
def run_function(first, second):
    print("About to run the function !")
    
    first()
    second()
    print("\nRan the functions")
    
run_function(function_one, function_two)


def get_run_function(first, second):
    
    def run_the_functions():
        print("About to run the fucntions !\n")
        first()
        second()
        print("\nran the functions")
    
    return run_the_functions

f = get_run_function(function_one, function_two)

type(f)
f()
print(f)


def outer_functions(outer_param: str):
    print(f"return a string param: {outer_param}")
    
    def inner_functions(inner_param):
        return(f"Your outer param was {outer_param} and your inner param is {inner_param}")

    return inner_functions


def generate_power(expoent):
    def power(base):
        return base ** expoent
    return power


raise_two = generate_power(2)

print(raise_two(2))
print(raise_two(5))
