import util
import datetime as dt
import random


class Circle:


    def __init__(self, words):

        '''Set words, generate positions.

        :param list words: A dictionary of words.

        :return void.'''

        self.texts = []
        self.plots = []

        # Copy words.
        self.words = list(words)

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


    def plot_texts(self, length):

        '''Generate aggregate plots for texts.

        :param in length: The segment length.

        :return void.'''

        avgx = None
        avgy = None

        # Walk texts.
        for i,text in enumerate(self.texts):

            # Plot the first segment.
            seed = self.plot_segment(text.tokens[:length])
            self.plots[i].append(seed)

            # Set averages.
            avgx = seed[0]
            avgy = seed[1]

            # Zipper the text.
            for h,t in text.zipper(length):

                # Get head and tail points.
                head = self.word_to_point[h]
                tail = self.word_to_point[t]

                # Update averages, push point.
                avgx = ((avgx*length)-head[0]+tail[0])/length
                avgy = ((avgy*length)-head[1]+tail[1])/length
                self.plots[i].append((avgx, avgy))
