class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.age > 7:
            print(f"{self.name} starts barking WOOF-WOOF")
        else:
            print(f"{self.name} is barking woof-woof")

miranda = Dog('Miranda', 7, 21)
mill = Dog('Mill', 9, 18)
miranda.bark()
mill.bark()
