# Create a parent class with 1 method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printing(self):
        print(f"{self.name} is now {self.age} years old")

# Create a child class inheriting from Person class and add 1 method called printing_2
class Student(Person):
    def __init__(self,name,age):
        # super() method help child class automatically inherit method from parent class
        super().__init__(name,age)
    def printing_2(self):
        print(f"{self.name} is now at the age of {self.age}")

john = Student('John',23)
print(john.printing())
# Output: John is now 23 years old
print(john.printing_2())
# Output: John is now at the age of 23