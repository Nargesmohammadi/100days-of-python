def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 4, 5, 6))


# it has dictionary type because of kwargs:
def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n += kwargs["multiply"]

    print(n)


calculate(2, add=3, multiply=5)


class Car:

    # in this class if we want to print my_car without one of arguments that gives mount it gets error.
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="bmw", model="401")
print(my_car.make)


class Car1:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")


my_car2 = Car1(make="bmw", model="230")
# now if call the colour, but it doesn't give mount we don't give an error like former code, it just prints none.
print(my_car2.colour)
