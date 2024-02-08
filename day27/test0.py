

def unlimited_sum(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

# JUST ARGS IS A TUPLE
# print(unlimited_sum(1, 2, 3, 4))


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")


my_car = Car(make="Nissan", model="GT", goaway="whatever")
print(my_car.make)