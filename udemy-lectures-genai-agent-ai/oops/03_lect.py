class Chai:
    strength = "strong"
    temp = "hot"

cutting = Chai()

print(f"strength is {cutting.strength}")
print(f"temperature is {cutting.temp}")

cutting.temp = "cold"
print(f"temperature is {cutting.temp}")
print(f"Chai class temperature is {Chai.temp}")

del cutting.temp
print(f"temperature is {cutting.temp}")