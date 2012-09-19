import math


def circle(count):

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


def mean_center(points):

    '''Compute the mean center of a set of points.

    :param list points: A list of x/y tuples.

    :return tuple center: The mean center points.'''

    xs = [x for x,y in points]
    ys = [y for x,y in points]
    return (avg(xs), avg(ys))


def avg(numbers):

    '''Average a list.

    :param list numbers: List of numbers.

    :return float: The average.'''

    return float(sum(numbers)) / len(numbers)