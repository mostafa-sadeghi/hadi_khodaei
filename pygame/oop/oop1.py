class Dog:
    def __init__(self, dog_name, dog_gender, dog_age):
        self.name = dog_name
        self.gender = dog_gender
        self.age = dog_age

    def eat(self):
        if self.gender == "boy":
            print(f"{self.name} good boy eatup!!")

        else:
            print(f"{self.name} good girl eatup!!")

    def bark(self, is_loud):
        if is_loud:
            print("WOOF WOOF WOOF")
        else:
            print("WOOF")


dog_1 = Dog("Dog 1", "boy", 3)
# print(dog_1.name)
# print(dog_1.gender)
# print(dog_1.age)
dog_1.eat()
dog_1.bark(True)

dog_2 = Dog("Dog 2", "girl", 6)
# print(dog_2.name)
# print(dog_2.gender)
# print(dog_2.age)
dog_2.eat()
dog_2.bark(False)
