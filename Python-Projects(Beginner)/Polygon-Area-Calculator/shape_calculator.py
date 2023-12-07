class Rectangle:
    def __init__(self,width=None,height=None) -> None:
        self.width = width
        self.height=height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self,width:int):
        self.width=width
    def set_height(self,height:int):
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self)->float:
        perimter=(2 * self.width + 2 * self.height)
        return perimter
    def get_diagonal(self):
        dia=((self.width ** 2 + self.height ** 2) ** .5)
        return dia
    
    def get_picture(self):
        h = self.height
        w = self.width
        if h > 50 or w > 50:
            return "Too big for picture.\n"

        picture = ""
        for i in range(h):
            picture += "*" * w + "\n"

        return picture
    def get_amount_inside(self, shape):
        if not isinstance(shape, (Rectangle, Square)):
            raise ValueError("The 'shape' argument must be an instance of Rectangle or Square.")

        # Calculate how many times 'shape' can fit horizontally and vertically
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height

        return horizontal_fit * vertical_fit

class Square(Rectangle):
    def __init__(self, side=None) -> None:
        super().__init__(width=side, height=side)

    def set_side(self,side):
        super().__init__(width=side,height=side)
        
    def __str__(self):
        return f"Square(side={self.width})"

        

