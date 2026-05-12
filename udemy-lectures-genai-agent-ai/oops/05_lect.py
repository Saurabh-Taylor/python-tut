class ChaiOrder:
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.size = size

    def display_order(self):
        print(f"Chai Order: {self.size} {self.flavor}")

order1 = ChaiOrder("Masala", "Large")
order1.display_order()