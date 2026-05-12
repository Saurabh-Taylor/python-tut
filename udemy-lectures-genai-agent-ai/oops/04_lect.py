class Chaicup:
    size = 150 # ml

    def describe(self):
        print(f"This is a chaicup with a capacity of {self.size} ml.")


my_cup = Chaicup()
my_cup.describe()  
my_cup.size = 200
my_cup.describe()  
print(f"Chaicup class {Chaicup.describe()} ")