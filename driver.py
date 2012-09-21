from plot import *


def shakespeare(width):
    p = Plot()
    p.load_directory('texts/shakespeare')
    p.plot(width)
