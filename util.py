import math
import itertools


def generate_circle(count):

    '''Generate the coordinate positions for a circle
    comprised of <count> points on a cartesian grid.

    :param int count: The number of points in the circle.

    :return list points: An ordered list of tuples of x/y
    float coordinates that form the circle.'''

    # Get angle unit and radius.
    interval = 360 / float(count)
    radius = count / (2 * math.pi)
    points = []

    # Walk the word count.
    for i in range(count):
        angle = (interval * i) * (math.pi / 180)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))

    return points


def hypotenuse(origin, target):

    '''Compute linear distance between points.

    :param tuple origin: The origin.
    :param tuple target: The target.

    :return float: The hypotenuse.'''

    dx = origin[0]-target[0]
    dy = origin[1]-target[1]
    return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
