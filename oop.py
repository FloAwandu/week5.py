class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print("Hello, my name is {}, I am {} years old, and I am {}.".format(self.name, self.age, self.gender))

# An instance of the Person class
person1 = Person("Anastacia", 30, "Female")

# Call introduce method to display person's information
person1.introduce()