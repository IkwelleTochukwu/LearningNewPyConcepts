class Users:
    def __init__(self, first_name, last_name):
        """Initializes the names attributes"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Prints the information of the users"""
        print(f"Hello, {self.first_name} {self.last_name}, your information has been saved!")

    def greet_user(self):
        """Send a personalized greeting to the users"""
        print(f"Good day {self.first_name} {self.last_name}. Welcome!")


UserInput = Users("Tochukwu", "Ikwelle")
UserInput.describe_user()
UserInput.greet_user()
