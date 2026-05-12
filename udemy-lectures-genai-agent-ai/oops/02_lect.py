class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = False
print(Chai.is_hot) 

# creating objects from class chai

masala_tea = Chai()
print(masala_tea.origin)
print(masala_tea.is_hot)

masala_tea.is_hot = True
print(masala_tea.is_hot)
print(Chai.is_hot) 