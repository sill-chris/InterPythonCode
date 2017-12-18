"""
Python Review of classes
"""

import math

class MyFirstClass:
    pass


class Point:
    """
    Represents a point in 2-D geometric coordinates
    """
    def __init__(self, x = 0, y =0):
        """
        Initializes the position of a new point.
         If they are not specified, the point defaults
         to the origin
        :param x: x coordinate.Default = 0
        :param y: y coordinate.Default = 0
        """
        self._x = x
        self._y = y

    # Add some instance methods: Do something
    def reset(self):
        """
        Reset the point to the original location in 2D space
        :return: Nothing
        """
        self._x = 0
        self._y = 0

    # Get the points
    def getPoint(self):
        """
        Get current x and y coordinate values of 2D point
        :return:
        """
        return self._x, self._y

    # Move Point
    def movePoint(self, x, y):
        """
        Move point ot a new location in a 2D space
        :param x: x coordinate
        :param y: y coordinate
        :return: Nothing
        """
        self._x = x
        self._y = y


    # Calculate distance
    def calcDistance(self, other_point):
        """
        Calculate the distance from this point to a second
        point passed as a parameter
        This method uses Pythagorean Theorem to calculate
        the distance between two points
        :param other_point: second point to calculate
        :return: Distance between two points (float)
        """
        return math.sqrt((self._x - other_point._x)**2 +
        (self._y + other_point._y))


def main():
    p1 = Point() # Take default values
    p2 = Point(2, 5) # Set values

    # Add information
    # p1.x = 5
    # p1.y = 4
    # p2.x = 3
    # p2.y = 6

    print(p1._x, p1._y)
    # p1.reset()
    print(p2.calcDistance(p1))
    p1.movePoint(3, 2)
    print(p1.getPoint())
    print(p2.getPoint())
    print(p2.calcDistance(p1))

if __name__ == '__main__':  # Ever single module you write should have this
    main()
