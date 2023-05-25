class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

def print_dog(axe):
    print(axe.name + "'s", 'age is', axe.age, 'and weight is', axe.weight)
 
codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)
codie.age = 8
print_dog(codie)
print_dog(jackson)    