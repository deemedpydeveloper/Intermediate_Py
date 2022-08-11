# Passing many parameter as arguments to a defined function.

# *name ---> used to accept as many arguments as required for user.
# * operator collects all the arguments in a 'tuple'. Therefore, this method is referred as "Unlimited Positional Arguments."
def add(*args):
    #  first_argument = args[0]
    sum = 0
    for n in args:
        sum += n
    return sum

# displays *args when inputting parameters.
result = add()
print(result)