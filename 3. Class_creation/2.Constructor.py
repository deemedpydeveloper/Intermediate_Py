# Constructor.

## It is used to define what should an object do when it is created from the class.
## It does 'Initialization' of the attribute in an object.
## Easy way of creation of attributes , if there are many.

# Syntax for constructing an object.

class User:
    def __init__(self, user_id, username):   # pass object attribute value as many as required.
        self.id = user_id   # object.attribute_name = attribute_value
        self.username = username
        self.followers = 0

user_1 = User("001", "tejendra")  # attribute value as positional arguments.

# Accessing object attributes.
print(user_1.id)
print(user_1.followers)