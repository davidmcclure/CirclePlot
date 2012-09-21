from text import *
from circle import *
import matplotlib.pyplot as plt
import requests as req
import util
import os


class Plot:


    def __init__(self):

        '''Create circle.

        :return void.'''

        self.circle = Circle()
        self.labels = []


    def paste_stream(self, stream):

        '''Register text from direct stream.

        :param string stream: The text stream.

        :return void.'''

        self.circle.register_text(Text(stream))


    def load_url(self, url):

        '''Register a text from a URL.

        :param string url: The url.

        :return void.'''

        res = req.get(url)
        self.circle.register_text(Text(res.text))
        self.labels.append(url)


    def load_file(self, path):

        '''Register a text from a file.

        :param string path: The filepath.

        :return void.'''

        f = open(path, 'r')
        self.circle.register_text(Text(f.read()))
        self.labels.append(path)


    def load_directory(self, path):

        '''Register texts from a directory.

        :param string path: The directory path.

        :return void.'''

        # Register texts.
        for filepath in os.listdir(path):
            self.load_file(path+'/'+filepath)


    def plot(self, width):

        '''Generate plot lines.

        :param int width: The segment length.

        :return list plots: The list of [xs, ys].'''

        self.plots = []

        # Compute plot lines.
        self.circle.plot_texts(width)

        # Graph the texts.
        for plot in self.circle.plots:
            xs = [x for x,y in plot]
            ys = [y for x,y in plot]
            self.plots.append((xs, ys))


    def render(self, labels=True, ticks=True, parts=10):

        '''Render plot lines.

        :param bool labels: Render plot labels if true.
        :param bool ticks: Render percentage ticks if true.
        :param int parts: The number of tick partitions.

        :return void.'''

        # Clear.
        plt.clf()

        for i,p in enumerate(self.plots):

            # Render.
            plt.plot(*p)

            # Label.
            if labels:
                x = p[0][0]
                y = p[1][0]
                plt.annotate(self.labels[i], (x,y))

            # Ticks
            if ticks:
                for l,i in util.plot_labels(len(p[0]), parts):
                    plt.annotate(l, (p[0][i], p[1][i]))
