# Passing as many keyword arguments as required by the user.

# **name ---> used to pass multiple keyword arguments.
# ** ---> this operator stores keyword arguments as 'dictionary'.

def my_function(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)

# no arguments either (positional or keyword) are passed as parameters.
print(my_function())

# keyword arguments are passed as parameters.
print(my_function(name='tejendra', age=22, degree='b.tech'))