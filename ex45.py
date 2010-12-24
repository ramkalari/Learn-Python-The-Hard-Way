## Animal is-a object.
class Animal(object):
	
	def is_mammal(self):
		pass

## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name

	def is_mammal(self):
		return True

	def print_name(self):
		print self.name


## Cat is-a animal
class Cat(Animal):
	
	def __init__(self, name):
		## Cat has-a name
		self.name = name

	def is_mammal():
		return True



## Person is-a Object
class Person(object):
	
	def __init__(self, name):
		## Person has-a name
		self.name = name
		## Person has-a pet of some kind	
		self.pet = None
		## Person has-many children
		self.children = []
	

	def is_male():
		pass

	def add_child(self, child):
		self.children.append(child)


## Employee is-a person
class Employee(Person):
	
	def __init__(self, name, salary):
		
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

	def is_male():
		pass	


class Child(Person):
	pass
	
## Fish is-a object 
class Fish(object):

	def is_amphibian():
		return False


## Salmon is-a fish
class Salmon(Fish):
	
	def is_tasty():
		return True

## Halibut is-a fish
class Halibut(Fish):
	
	def is_tasty():
		return False

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet which is-a satan
mary.pet = satan

## frank is-a Employee who has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has a pet which is-a rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()


Dog.name = "We are all dogs"

print Dog.name
alsatian = Dog("Alsatian")
print alsatian.name

print rover.is_mammal()
rover.print_name()

frank.add_child(mary)

for child in frank.children:
	print child.name
