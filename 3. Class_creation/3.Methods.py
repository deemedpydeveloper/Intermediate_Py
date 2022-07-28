# Method Creation.

## Instagram followers.

# Class Creation.
class User:

    # Constructor for object attributes.
    def __init__(self, user_id, username):  # self ---> refers to as "object calling the constructor".
        self.id = user_id
        self.user_name = username
        self.followers = 0  # for attributes whose value is initialized, no need to be passed to constructor.
        self.following = 0

    # Constructor for object methods.
    def follow(self, user):
        user.followers += 1
        self.following += 1

# Object Creation and passing attribute values as positional arguments.
user_1 = User('001', 'tejendra')
user_2 = User('002', 'angela')

# Accessing Object Method.
user_1.follow(user_2)

# Accessing Objects Attributes.
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
