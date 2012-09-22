from text import *
import util
import random
import os


class Circle:


    def __init__(self):

        '''Shells for texts and plots.

        :param list words: A dictionary of words.

        :return void.'''

        self.texts = []


    def paste_stream(self, stream):

        '''Register text from direct stream.

        :param string stream: The text stream.

        :return void.'''

        self.texts.append(Text(stream))


    def load_url(self, url):

        '''Register a text from a URL.

        :param string url: The url.

        :return void.'''

        res = req.get(url)
        self.texts.append(Text(res.text))


    def load_file(self, path):

        '''Register a text from a file.

        :param string path: The filepath.

        :return void.'''

        f = open(path, 'r')
        self.texts.append(Text(f.read()))


    def load_directory(self, path):

        '''Register texts from a directory.

        :param string path: The directory path.

        :return void.'''

        # Register texts.
        for filepath in os.listdir(path):
            self.load_file(path+'/'+filepath)


    def build_circle(self):

        '''Generate the unique vocabulary, build circle.

        :param list words: A dictionary of words.

        :return void.'''

        # Generate vocabulary from texts.
        vocabs = [text.vocab for text in self.texts]
        self.vocab = list(set.union(*vocabs))

        # Randomize starting positions.
        random.shuffle(self.vocab)

        # Generate circle points.
        self.points = util.generate_circle(len(self.vocab))

        # Build word-point dict.
        self.word_to_point = {}
        for i,word in enumerate(self.vocab):
            self.word_to_point[word] = self.points[i]


    def build_corpus(self):

        '''Generate aggregate corpus from texts.

        :return void.'''

        self.corpus = []
        for text in self.texts: self.corpus += text.tokens


    def model(self, iterations=10):

        '''Construct the semantic circle.

        :return void.'''

        self.build_circle()
        self.build_corpus()
        self.links = {}

        for word in self.vocab: self.links[word] = []

        # Set head and tail links.
        self.links[self.corpus[0]].append(self.corpus[1])
        self.links[self.corpus[-1]].append(self.corpus[-2])

        # Register links.
        for i in range(1, len(self.corpus)-3):
            triad = self.corpus[i:i+3]
            self.links[triad[1]].append(triad[0])
            self.links[triad[1]].append(triad[2])
