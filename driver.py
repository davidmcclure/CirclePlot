from text import *
from circle import *
from plot import *
import matplotlib.pyplot as plt
import util


def render(plots, labels=None, partitions=10):
    plt.clf()
    for i,p in enumerate(plots):
        plt.plot(*p)
        if labels: plt.annotate(labels[i], (p[0][0], p[1][0]))
        for l,i in util.plot_labels(len(p[0]), partitions):
            plt.annotate(l, (p[0][index], p[1][index]))


def paste_stream(stream, width):
    p = Plot()
    p.paste_stream(stream)
    p.plot(width)
    p.render()


def load_url(url, width):
    p = Plot()
    p.load_url(url)
    p.plot(width)
    p.render()


def load_file(path, width):
    p = Plot()
    p.load_file(path)
    p.plot(width)
    p.render()


def load_dir(path, width):
    p = Plot()
    p.load_directory(path)
    p.plot(width)
    p.render()


# Experiments:


def shakespeare(width=20000):
    load_dir('texts/shakespeare', width)


def tempest(width=6000):
    load_file('texts/shakespeare/tempest.txt', width)


def hamlet(width=9000):
    load_file('texts/shakespeare/hamlet.txt', width)


def macbeth(width=5000):
    load_file('texts/shakespeare/macbeth.txt', width)


def winters_tale(width=8000):
    load_file('texts/shakespeare/winters_tale.txt', width)


def othello(width=8000):
    load_file('texts/shakespeare/othello.txt', width)


def shakespeare_vs_yeats(width=20000):
    p = Plot()
    p.load_directory('texts/shakespeare')
    p.load_file('texts/poets/yeats.txt')
    p.plot(width)
    p.render()
