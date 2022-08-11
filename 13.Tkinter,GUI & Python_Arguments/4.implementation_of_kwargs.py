# # Example.
# class Car:
#     def __init__(self, **kwargs):
#         self.model = kwargs['model']
#         self.price = kwargs['price']
#         self.seats = kwargs['seats']
#
# # passing keyword arguments to a constructor in Car class.
# car = Car(model='SUV', price='2lakhs')
#
# # Accessing Car class attributes.
# print(car.model)
#
# # Produces an error since 'seats' keyword arguments is not passed as parameter to Car class.
# print(car.seats)

# To overcome the 'KeyError', we use 'dict.get()' method.
class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get('model')
        self.price = kwargs.get('price')
        self.seats = kwargs.get('seats')

car = Car(model='SUV', price='2lakhs')

# prints 'None', since we used get method.
print(car.seats)