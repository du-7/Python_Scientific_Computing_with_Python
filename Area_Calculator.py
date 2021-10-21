
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return self.width*2 + self.height*2
    
    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**0.5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return ("Too big for picture.")
        else:
            return ("*" * self.width + "\n") * self.height
    
    def get_amount_inside(self, shape):
        fit_in_width = self.width // shape.width
        fit_in_height = self.height // shape.height
        return fit_in_height*fit_in_width
    
class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
        pass

    def __repr__(self):
        return "Square(side={})".format(self.side)

    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)
    
    def set_height(self, height):
        self.set_side(height)
    
    def set_width(self, width):
        self.set_side(width)

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
