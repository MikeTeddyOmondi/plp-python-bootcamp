class Person:
    def __init__(self, name, age, gender):
        """
        Initializes a new instance of the Person class.

        Parameters:
            name (str): The person's name.
            age (int): The person's age.
            gender (str): The person's gender.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """
        Prints an introduction message with the person's details.
        """
        print(
            f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}."
        )


# Creating an instance of the Person class and calling the introduce method
person = Person("Alice", 30, "Female")
person.introduce()
