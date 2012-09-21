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


def paste(stream, width):
    p = Plot()
    p.paste_stream(stream)
    render(p.plot(width))


def load(url, width):
    p = Plot()
    p.load_url(url)
    render(p.plot(width), p.legend)


# Experiments:


def shakespeare(width=20000):
    p = Plot()
    p.load_directory('texts/shakespeare')
    render(p.plot(width), p.legend)


def tempest(width=9000):
    p = Plot()
    p.load_file('texts/shakespeare/tempest.txt')
    render(p.plot(width), p.legend)


def hamlet(width=9000):
    p = Plot()
    p.load_file('texts/shakespeare/hamlet.txt')
    render(p.plot(width), p.legend)


def macbeth(width=5000):
    p = Plot()
    p.load_file('texts/shakespeare/macbeth.txt')
    render(p.plot(width), p.legend)


def winters_tale(width=8000):
    p = Plot()
    p.load_file('texts/shakespeare/winters_tale.txt')
    render(p.plot(width), p.legend)


def othello(width=8000):
    p = Plot()
    p.load_file('texts/shakespeare/othello.txt')
    render(p.plot(width), p.legend)


def shakespeare_vs_yeats(width=20000):
    p = Plot()
    p.load_directory('texts/shakespeare')
    p.load_file('texts/poets/yeats.txt')
    render(p.plot(width), p.legend)


def antony_and_cleopatra(width=5000):
    p = Plot()
    p.load_file('texts/shakespeare/antony_and_cleopatra.txt')
    render(p.plot(width), p.legend)


def aesop(width=30000):
    p = Plot()
    p.load_url('http://www.gutenberg.lib.md.us/1/1/3/3/11339/11339.txt')
    render(p.plot(width), p.legend, True)
