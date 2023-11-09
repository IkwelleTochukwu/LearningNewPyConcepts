class Resturant:

    def __init__(self, resturant_name, cusine_type):
        """Initializes class attributes"""
        self.resturant_name = resturant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def descirbe_resturant(self):
        print(f"The name of the restaurant is {self.resturant_name} and they known for making the {self.cusine_type},")

    def open_resturant(self):
        print("The restaurant is now open from 9:00am to 10:00pm today")

    def set_number_served(self, set_number):
        """set the number of served to a given value"""
        self.number_served = set_number

    def statistics(self):
        print(f"Total number served is {self.number_served} for today!")

    def increment_number_served(self, number):
        """Increase the number served by a given amount"""
        self.number_served += number



Res = Resturant("TeyceeFoods", "Beans&Dodo")
Res.descirbe_resturant()
Res.open_resturant()
Res.set_number_served(450)
Res.statistics()
Res.increment_number_served(100)
Res.statistics()
