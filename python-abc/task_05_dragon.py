#!/usr/bin/python3


class SwimMixin:
    """A mixin class that provides swimming behavior.

    Methods:
        swim(): Prints a message indicating the creature swims.
    """
    def swim(self):
        """Prints a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """This class defines a fly method that prints a statement."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """This class defines a roar method that prints a statement."""

    def roar(self):
        print("The dragon Roars!")
