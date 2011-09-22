class Animal(object):
    pass

# Dog is an animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a name
        self.name = name

# Cat is an animal
class Cat(Animal):

    def __init__(self, name):
       ## Cat has a name
       self.name = name

# Person is a object
class Person(object):

    def __init__(self, name):
        # Person has a name
        self.name = name
        # Person has a pet
        self.pet = None

# Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        # Employee has a salary
        self.salary = salary

# Fish is an object
class Fish(object):
    pass


# Salmon is a Fish
class Salmon(Fish):
    pass

# Halibut is a fish
class Halibut(Fish):
    pass


# rover is a Dog
rover = Dog("Rover")

# Satan is a Cat
satan = Cat("Satan")

# mary is a person
mary = Person("Mary")

# mary has a pet called satan which is a cat
mary.pet = satan

# Frank is an employee
frank = Employee("Frank", 120000)

# frank has a pet called rover which is a dog
frank.pet = rover

# flipper is a fish
flipper = Fish()

# crouse is a salmon
crouse = Salmon()

# harry is a Halibut
harry = Halibut()



