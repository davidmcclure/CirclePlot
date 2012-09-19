import util
import random


class Circle:


    def __init__(self, words):

        '''Set words, generate positions.

        :param list words: A dictionary of words.

        :return void.'''

        self.texts = []
        self.plots = []

        # Randomize word order.
        self.words = words
        random.shuffle(self.words)

        # Generate circle.
        self.points = util.generate_circle(len(words))


    def register_text(self, text):

        '''Register a text.

        :param Text text: The text instance.

        :return void.'''

        self.texts.append(text)
        self.plots.append([])


    def plot_segment(self, words):

        '''Plot words and calculate centroid.

        :param list words: The words.

        :return tuple centroid: The centroid.'''

        points = []

        # Plot the words.
        for i,word in enumerate(words):
            points.append(self.points[i])

        # Compute centroid.
        return util.mean_center(points)


    def plot_texts(self, length=20):

        '''Generate aggregate plots for texts.

        :param in length: The segment length.

        :return void.'''

        # Walk texts.
        for i,text in enumerate(texts):

            # Zipper the segments.
            for segment in text.zipper(length):
                self.plots.append(self.plot_segment(segment))
