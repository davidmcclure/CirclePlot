from text import *
from circle import *
from plot import *
import matplotlib.pyplot as plt
import util


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


def sonnets(width=2000):
    load_file('texts/shakespeare/sonnets.txt', width)


def ulysses(width=100000):
    load_url('http://www.gutenberg.lib.md.us/4/3/0/4300/4300.txt', width)


def bible(width=200000):
    load_url('http://www.gutenberg.lib.md.us/1/10/10.txt', width)


def notes_from_underground(width=1000):
    load_url('http://www.gutenberg.lib.md.us/6/0/600/600.txt', width)


def aesops_fables(width=1000):
    load_url('http://www.gutenberg.lib.md.us/1/1/3/3/11339/11339.txt', width)


def dubliners(width=20000):
    load_url('http://www.gutenberg.lib.md.us/2/8/1/2814/2814.txt', width)


def shakespeare_vs_yeats(width=20000):
    p = Plot()
    p.load_directory('texts/shakespeare')
    p.load_file('texts/poets/yeats.txt')
    p.plot(width)
    p.render()


def iliad_vs_leaves_of_grass(width=3000):
    p = Plot()
    p.load_url('http://www.gutenberg.lib.md.us/2/1/9/2199/2199.txt')
    p.load_url('http://www.gutenberg.lib.md.us/1/3/2/1322/1322.txt')
    p.plot(width)
    p.render()


def yeats_vs_leaves_of_grass(width=3000):
    p = Plot()
    p.load_file('texts/poets/yeats.txt')
    p.load_url('http://www.gutenberg.lib.md.us/1/3/2/1322/1322.txt')
    p.plot(width)
    p.render()
