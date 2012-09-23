from text import *
import matplotlib.pyplot as plt
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


    def load_dir(self, path):

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
        self.v = list(set.union(*vocabs))

        # Randomize starting positions.
        random.shuffle(self.v)

        # Generate circle points.
        self.points = util.generate_circle(len(self.v))

        # Build word-point dict.
        self.wtp = {}
        for i,word in enumerate(self.v):
            self.wtp[word] = self.points[i]


    def build_corpus(self):

        '''Generate aggregate corpus from texts.

        :return void.'''

        self.corpus = []
        for text in self.texts: self.corpus += text.tokens


    def model_circle(self):

        '''Construct the semantic circle.

        :param int itr: The number of cycles.

        :return void.'''

        self.build_circle()
        self.build_corpus()
        self.links = {}
        wc = len(self.v)

        for word in self.v: self.links[word] = []

        # Set head and tail links.
        self.links[self.corpus[0]].append(self.corpus[1])
        self.links[self.corpus[-1]].append(self.corpus[-2])

        # Register links.
        for i in range(0, len(self.corpus)-2):
            triple = self.corpus[i:i+3]
            self.links[triple[1]].append(triple[0])
            self.links[triple[1]].append(triple[2])

        startlen = 0
        for k,v in self.links.iteritems():
            origin = self.wtp[k]
            targets = [self.wtp[w] for w in v]
            rays = [util.hypotenuse(origin, t) for t in targets]
            total = sum(rays)
            startlen += total
        print startlen

        # Run cycles.
        try:
            while True:

                # Get random indexes.
                i1 = random.randrange(wc)
                i2 = random.randrange(wc)

                # Sum 1.
                origin = self.wtp[self.v[i1]]
                targets = [self.wtp[w] for w in self.links[self.v[i1]]]
                rays = [util.hypotenuse(origin, t) for t in targets]
                s1 = sum(rays)

                # Sum 2.
                origin = self.wtp[self.v[i2]]
                targets = [self.wtp[w] for w in self.links[self.v[i2]]]
                rays = [util.hypotenuse(origin, t) for t in targets]
                s2 = sum(rays)

                # Starting total.
                total1 = s1 + s2

                # Swap the words.
                self.v[i1], self.v[i2] = self.v[i2], self.v[i1]
                self.wtp[self.v[i1]], self.wtp[self.v[i2]] = self.wtp[self.v[i2]], self.wtp[self.v[i1]]

                # Sum 1.
                origin = self.wtp[self.v[i1]]
                targets = [self.wtp[w] for w in self.links[self.v[i1]]]
                rays = [util.hypotenuse(origin, t) for t in targets]
                s1 = sum(rays)

                # Sum 2.
                origin = self.wtp[self.v[i2]]
                targets = [self.wtp[w] for w in self.links[self.v[i2]]]
                rays = [util.hypotenuse(origin, t) for t in targets]
                s2 = sum(rays)

                # Ending total.
                total2 = s1 + s2

                # Unswap if greater.
                if total2 > total1:
                    self.v[i1], self.v[i2] = self.v[i2], self.v[i1]
                    self.wtp[self.v[i1]], self.wtp[self.v[i2]] = self.wtp[self.v[i2]], self.wtp[self.v[i1]]


        except KeyboardInterrupt:

            for v in self.v:
                print v

            endlen = 0
            for k,v in self.links.iteritems():
                origin = self.wtp[k]
                targets = [self.wtp[w] for w in v]
                rays = [util.hypotenuse(origin, t) for t in targets]
                total = sum(rays)
                endlen += total
            print endlen / startlen
