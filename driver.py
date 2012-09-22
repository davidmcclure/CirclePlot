from circle import *


def test():
    c = Circle()
    c.load_file('texts/shakespeare/sonnets.txt')
    c.model()
