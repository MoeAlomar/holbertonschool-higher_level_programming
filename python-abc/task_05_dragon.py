#!/usr/bin/python3


class SwimMixin:
    """This class defines a swim method that prints a statement."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """This class defines a fly method that prints a statement."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """This class defines a roar method that prints a statement."""

    def roar(self):
        print("The dragon Roars!")


draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
