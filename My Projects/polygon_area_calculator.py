class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # set new width
    def set_width(self, new_width):
        self.width = new_width

    # set new height
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perm = 2 * self.width + 2 * self.height
        return perm

    def get_diagonal(self):
        diag = (self.width**2 + self.height**2)**0.5
        return diag

    # make the picture out of "*" and get the picture of the shape
    def get_picture(self):
        pic = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            stars = "*" * self.width
            for i in range(self.height):
                pic = stars + "\n" + pic
            return pic

    # the amount of other shapes that could be stored inside of this rectangle
    # if this rect is smaller than the other shape just return 0
    def get_amount_inside(self, shape):
        ans = 0
        if self.get_area() > shape.get_area():
            ans += self.get_area() / shape.get_area()
            return int(ans)
        else:
            return 0

    def __str__(self):
        string = f"Rectangle(width={self.width}, height={self.height})"
        return string


# a subclass of Rect
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    # set new square side length
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    # set new width but change the height as well bcs it's a square(same as above)
    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side

    # set new height and width(same as above)
    def set_height(self, new_side):
        self.width = new_side
        self.height = new_side

    def __str__(self):
        string = f"Square(side={self.width})"
        return string
