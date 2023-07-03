def sayhi():
    print("Hello user")


sayhi()


def sayhi(name):
    print("Hello " + name)


sayhi("Jay")
sayhi("Talib")


def sayhi(name, age):
    print("Hello " + name + ", you are " + age + " years old")


sayhi("Jay", "30")


def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old")


sayhi("Talib", 25)
