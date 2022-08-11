# Default Values for optional arguments.
def my_function(a=1, b=2, c=3):
    new_num = a + b + c
    return new_num

# no arguments needed.
default_value = my_function()
print(default_value)

# keyword arguments can be used to change the values.
optional_value = my_function(b=3)
print(optional_value)