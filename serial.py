"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

>> original answer 
class SerialGenerator:  
    
    def __init__(self,start=100):
       self.start = 100
       self.next=100
    
    def generate(self):
        self.next += 1
    
    def reset(self):
        self.next = self.start


>>correct answer 
class SerialGenerator:
    def __init__(self, start=0):
        """Make a new generator, starting at start."""

        self.start = self.next = start

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next serial."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to original start."""

        self.next = self.start

