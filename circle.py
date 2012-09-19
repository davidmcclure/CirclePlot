import util
import random


class Circle:


    def __init__(self, words):

        '''Set words, generate positions.

        :param list words: A dictionary of words.

        :return void.'''

        self.texts = []
        self.plots = []

        # Copy words, randomize.
        self.words = list(words)
        random.shuffle(self.words)

        # Generate circle.
        self.points = util.generate_circle(len(words))

        # Build word-point dict.
        self.word_to_point = {}
        for i,word in enumerate(self.words):
            self.word_to_point[word] = self.points[i]


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
        for word in words:
            points.append(self.word_to_point[word])

        # Compute centroid.
        return util.mean_center(points)


    def plot_texts(self, length=20):

        '''Generate aggregate plots for texts.

        :param in length: The segment length.

        :return void.'''

        # Walk texts.
        for i,text in enumerate(self.texts):

            # Zipper the segments.
            for segment in text.zipper(length):
                point = self.plot_segment(segment)
                self.plots[i].append(point)
