class car:
    """
    car models a car with tyres and an engine
    """
    def __init__(self, engine, tires):
        """
        docstring describing a method
        dunder method , to get specific functionality on them. 
        """
        self.engine = engine 
        self.tires = tires

    def description(self):
        print(f"A car with an {self.engine} is engine and {self.tires} is tires")

    def wheel_circumfrence(self):
        if len(self.tires) > 0:
            return self.tires[0].circumfrence()
        else:
            return 0
    

 