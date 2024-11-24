class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def move(self):
        return "Running"


class Cat(Animal):
    def move(self):
        return "Jumping"


class Fish(Animal):
    def move(self):
        return "Swimming"


class Bird(Animal):
    def move(self):
        return "Flying"


# Example usage
if __name__ == "__main__":
    animals = [Dog(), Cat(), Fish(), Bird()]

    for animal in animals:
        print(animal.move())