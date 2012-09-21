from text import *
from circle import *
import matplotlib.pyplot as plt


def load(url, width, html=False):
    res = req.get(url)
    plot(res.text, width)


def plot(text, width):
    t = Text(text)
    c = Circle()
    c.register_text(t)
    c.plot_texts(width)
    xs = [x for x,y in c.plots[0]]
    ys = [y for x,y in c.plots[0]]
    plt.clf()
    plt.plot(xs, ys)


def comp(url1, url2, width):
    res1 = req.get(url1)
    res2 = req.get(url2)
    t1 = Text(res1.text)
    t2 = Text(res2.text)
    c = Circle()
    c.register_text(t1)
    c.register_text(t2)
    c.plot_texts(width)
    plt.clf()
    xs = [x for x,y in c.plots[0]]
    ys = [y for x,y in c.plots[0]]
    plt.plot(xs, ys)
    xs = [x for x,y in c.plots[1]]
    ys = [y for x,y in c.plots[1]]
    plt.plot(xs, ys)
