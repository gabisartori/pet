# This one envolves object orientation
# So it'll be a bit more flexible as to where and how you should change it


# The Person class is used to hold the information about a person
# The information being name and age

# It has a method dedicated to showing the person's information on screen
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name
        self.__age: int = age
    
    # This one
    def show_information(self):
        print(f"{self.__name} is {self.__age} {'years' if self.__age != 1 else 'year'} old.")

# With a few examples, you can see that the method is working just fine
people = [
    Person("John", 20),
    Person("Mary", 19),
    Person("Bob", 21),
    Person("Alice", 1),
]
for person in people:
    person.show_information()  # Ok

print("\nEverything is working until here\n")

# But when I try to replicate its behaviour right here, the code crashes
for person in people:
    print(f"{person.__name} is {person.__age} {'years' if person.__age != 1 else 'year'} old.")
