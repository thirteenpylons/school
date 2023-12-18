"""
Given class Triangle, complete the program to read and set the base and height 
of triangle1 and triangle2, determine which triangle's area is larger, 
and output the larger triangle's info, making use of Triangle's relevant methods.

Ex: If the input is:

3.0
4.0
4.0
5.0
where 3.0 is triangle1's base, 4.0 is triangle1's height, 4.0 is 
triangle2's base, and 5.0 is triangle2's height, the output is:

Triangle with larger area:
Base: 4.00
Height: 5.00
Area: 10.00

"""

class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base: float) -> None:
        self.base = user_base

    def set_height(self, user_height: float) -> None:
        self.height = user_height
   
    def get_area(self) -> float:
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print('Base: {:.2f}'.format(self.base))
        print('Height: {:.2f}'.format(self.height))
        print('Area: {:.2f}'.format(self.get_area()))

if __name__ == "__main__":
    triangle_one = Triangle()
    triangle_two = Triangle()

    triangle_one_base = float(input())
    triangle_one.set_base(triangle_one_base)
    triangle_one_height = float(input())
    triangle_one.set_height(triangle_one_height)

    triangle_two_base = float(input())
    triangle_two.set_base(triangle_two_base)
    triangle_two_height = float(input())
    triangle_two.set_height(triangle_two_height)

    print("Triangle with larger area:")
    
    if triangle_one.get_area() > triangle_two.get_area():
        triangle_one.print_info()
    else:
        triangle_two.print_info()
