"""this script defines a clas square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    class defined
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Iniciatise

        Args"
        size-> size of the square
        x: The x-coordinate of the square.
        y: The y-coordinate of the square.
            
            id: The ID of the square.
        
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The formatted string containing the square information.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """
        Get the size of the square.

        """
        return self.width
    
    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        """
        self.width = self.height = value
