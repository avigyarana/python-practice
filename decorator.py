def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("my arguments are: {} {}".format(arg1,arg2))
        function(arg1,arg2)
    return wrapper_accepting_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("cities that i love are {} and {}".format(city_one, city_two))

cities("san fran","NYC")

#defining general purpose decorators

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("positional arguemnts are:", args)
        print ("keyword arguemnts are",kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_arguments():
    print("no arguments here")

function_with_no_arguments()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a,b,c):
    print(a,b,c)

function_with_arguments(1,2,3)

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("this has shown keyword arguments")


function_with_keyword_arguments(first_name = "avigya",last_name = "rana") #type: ignore