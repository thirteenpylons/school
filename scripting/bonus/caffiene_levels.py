"""
A half-life is the amount of time it takes for a substance or entity to fall 
to half its original value. Caffeine has a half-life of about 6 hours in humans. 
Given caffeine amount (in mg) as input, output the caffeine level after 6, 12, 
and 24 hours. Use a string formatting expression with conversion specifiers to 
output the caffeine amount as floating-point numbers.

Output each floating-point value with two digits after the decimal point, 
which can be achieved as follows:
print('{:.2f}'.format(your_value))

Ex: If the input is:

100
the output is:

After 6 hours: 50.00 mg
After 12 hours: 25.00 mg
After 24 hours: 6.25 mg
Note: A cup of coffee has about 100 mg. A soda has about 40 mg. An "energy" 
drink (a misnomer) has between 100 mg and 200 mg.
"""


class CaffeineHalflife:
    def __init__(self, caffeine_mg: float):
        self.caffeine_mg = caffeine_mg
    
    def print_halflife(self):
        halflife_at_six_hours = self.caffeine_mg / 2
        halflife_at_twelve_hours = halflife_at_six_hours / 2
        halflife_at_twenty_four_hours = halflife_at_twelve_hours / 4

        print("After 6 hours: {:.2f} mg".format(halflife_at_six_hours))
        print("After 12 hours: {:.2f} mg".format(halflife_at_twelve_hours))
        print("After 24 hours: {:.2f} mg".format(halflife_at_twenty_four_hours))



if __name__ == "__main__":
    caffeine_mg = float(input())
    halflife = CaffeineHalflife(caffeine_mg)
    halflife.print_halflife()
