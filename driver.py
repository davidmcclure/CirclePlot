from circle import *


def paste_stream(stream):
    c = Circle()
    c.paste_stream(stream)
    c.model_circle()
    c.plot_circle()


def load_url(url):
    c = Circle()
    c.load_url(url)
    c.model_circle()
    c.plot_circle()


def load_file(path):
    c = Circle()
    c.load_file(path)
    c.model_circle()
    c.plot_circle()


def load_dir(path):
    c = Circle()
    c.load_dir(path)
    c.model_circle()
    c.plot_circle()
