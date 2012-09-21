from text import *
from circle import *
import matplotlib.pyplot as plt
import requests as req
import os


class Plot:


    def __init__(self):

        '''Create circle.

        :return void.'''

        self.circle = Circle()


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
        self.circle.register_text(res.text)


    def load_file(self, path):

        '''Register a text from a file.

        :param string path: The filepath.

        :return void.'''

        print path
        f = open(path, 'r')
        self.circle.register_text(f.read())


    def load_directory(self, path):

        '''Register texts from a directory.

        :param string path: The directory path.

        :return void.'''

        for filepath in os.listdir(path):
            self.load_file(path+'/'+filepath)


    def plot(self, width):

        '''Plot the circle.

        :param int width: The segment length.

        :return void.'''

        # Compute plot lines.
        self.circle.plot_texts(width)
        plt.clf()

        # Graph the texts.
        for plot in self.circle.plots:
            xs = [x for x,y in plot]
            ys = [y for x,y in plot]
            plt.plot(xs, ys)
