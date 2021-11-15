import math


class Tire:
    """
    tire represents a tire that would be used in an automobile
    """

    def __init__(self, tire_type, width, ration, diameter, brand= '', construction='R'):
        self.tire = tire_type
        self.width = width
        self.ration = ration
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def circumfrence(self):
        """
        the circumfrence of the tire in inches
        this is another way of creating tests in python, run the code on repl 

        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumfrence()
        80.1
        """
        side_wall_inches = (self.width * ( self.ratio / 100 )) /  25.4
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * math.pi, 1)


    def __repr__(self):
        """
        Represent the tire information in the standard notation present on the side of 
        the tire. 
    
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}") + (f"{self.construction}{self.diameter}")   