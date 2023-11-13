class Users:
    def __init__(self, first_name, last_name):
        """Initializes the names attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Prints the information of the users"""
        print(f"Hello, {self.first_name} {self.last_name}, your information has been saved!")

    def greet_user(self):
        """Send a personalized greeting to the users"""
        print(f"Good day {self.first_name} {self.last_name}. Welcome!")

    def increment_login_attempts(self, number):
        """To increase the number of login attempts"""
        self.login_attempts += number

    def reset_login_attempts(self):
        """To reset the login attempts to 0"""
        self.login_attempts = 0

    def print_login_attempts(self):
        print(f'The number of login attempts is {self.login_attempts}')

class Admin(Users):
    def __init__(self, first_name, last_name):
        """Initializes the attribute of the parent class"""
        super().__init__(first_name, last_name)
        #self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()

    #def show_privileges(self):
        """Display the privileges"""
        #print(f"The admin user has the privileges; {self.privileges}")

class Privileges:
    """To make a class out of the show_privilege method, and use the class as an attribute"""
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def describe_privileges(self):
        """This method will print the privileges to the screen"""
        print(f'This user can do this: {self.privileges}')



UserInput = Users("Tochukwu", "Ikwelle")
UserInput.describe_user()
UserInput.greet_user()
UserInput.print_login_attempts()
UserInput.increment_login_attempts(1)
#UserInput.print_login_attempts()
#UserInput.reset_login_attempts()
#UserInput.print_login_attempts()

Admin = Admin('Tochukwu', 'Ikwelle')
Admin.privileges.describe_privileges()