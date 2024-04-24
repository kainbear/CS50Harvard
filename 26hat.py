import random


class Hat:
    houses = ["dom", "street", "world", "car"]

def sort(cls, name):
    print(name, "is in", random.choice(cls.houses))


sort("Stas")