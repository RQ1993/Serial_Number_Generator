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

class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""

    def __init__(self, start=0):
        """Initialize the SerialGenerator with a starting value."""
        self.start = start
        self.next_serial = start

    def generate(self):
        """Generate the next serial number and return it."""
        result = self.next_serial
        self.next_serial += 1
        return result

    def reset(self):
        """Reset the serial number back to the initial value."""
        self.next_serial = self.start
