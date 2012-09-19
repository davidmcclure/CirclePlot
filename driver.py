from text import *
from circle import *
import requests as req


c = None


def load(url, length):
    res = req.get(url)
    plot(res.text, length)


def plot(text, length):
    global c
    t = Text(text)
    c = Circle(t.vocab)
    c.register_text(t)
    c.plot_texts(length)
    print len(c.plots[0])
