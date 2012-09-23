import util
import datetime as dt
import random


class Circle:


    def __init__(self):

        '''Shells for texts and plots.

        :param list words: A dictionary of words.

        :return void.'''

        self.texts = []
        self.plots = []


    def build_circle(self):

        '''Generate the unique vocabulary, build circle.

        :param list words: A dictionary of words.

        :return void.'''

        # Generate vocabulary from texts.
        vocabs = [text.vocab for text in self.texts]
        self.vocab = list(set.union(*vocabs))
        random.shuffle(self.vocab)

        # Generate circle.
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


    def plot_texts(self, width):

        '''Generate aggregate plots for texts.

        :param int width: The segment length.

        :return void.'''

        self.build_circle()

        avgx = None
        avgy = None

        # Walk texts.
        for i,text in enumerate(self.texts):

            # Plot the first segment.
            seed = self.plot_segment(text.tokens[:width])
            self.plots[i].append(seed)

            # Set averages.
            avgx = seed[0]
            avgy = seed[1]

            # Zipper the text.
            for h,t in text.zipper(width):

                # Get head and tail points.
                head = self.word_to_point[h]
                tail = self.word_to_point[t]

                # Update averages, push point.
                avgx = ((avgx*width)-head[0]+tail[0])/width
                avgy = ((avgy*width)-head[1]+tail[1])/width
                self.plots[i].append((avgx, avgy))


    def model_circle(self):

        '''Construct the semantic circle.

        :param int itr: The number of cycles.

        :return void.'''

        self.build_circle()
        self.build_corpus()
        self.links = {}
        wc = len(self.vocab)

        for word in self.vocab: self.links[word] = []

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
            origin = self.word_to_point[k]
            targets = [self.word_to_point[w] for w in v]
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
                origin = self.word_to_point[self.vocab[i1]]
                targets = [self.word_to_point[w] for w in self.links[self.vocab[i1]]]
                rays = [util.hypotenuse(origin, t) for t in targets]
                s1 = sum(rays)

                # Sum 2.
                origin = self.word_to_point[self.vocab[i2]]
                targets = [self.word_to_point[w] for w in self.links[self.vocab[i2]]]
                rays = [util.hypotenuse(origin, t) for t in targets]
                s2 = sum(rays)

                # Starting total.
                total1 = s1 + s2

                # Swap the words.
                self.vocab[i1], self.vocab[i2] = self.vocab[i2], self.vocab[i1]
                self.word_to_point[self.vocab[i1]], self.word_to_point[self.vocab[i2]] = self.word_to_point[self.vocab[i2]], self.word_to_point[self.vocab[i1]]

                # Sum 1.
                origin = self.word_to_point[self.vocab[i1]]
                targets = [self.word_to_point[w] for w in self.links[self.vocab[i1]]]
                rays = [util.hypotenuse(origin, t) for t in targets]
                s1 = sum(rays)

                # Sum 2.
                origin = self.word_to_point[self.vocab[i2]]
                targets = [self.word_to_point[w] for w in self.links[self.vocab[i2]]]
                rays = [util.hypotenuse(origin, t) for t in targets]
                s2 = sum(rays)

                # Ending total.
                total2 = s1 + s2

                # Unswap if greater.
                if total2 > total1:
                    self.vocab[i1], self.vocab[i2] = self.vocab[i2], self.vocab[i1]
                    self.word_to_point[self.vocab[i1]], self.word_to_point[self.vocab[i2]] = self.word_to_point[self.vocab[i2]], self.word_to_point[self.vocab[i1]]


        except KeyboardInterrupt:

            for v in self.vocab:
                print v

            endlen = 0
            for k,v in self.links.iteritems():
                origin = self.word_to_point[k]
                targets = [self.word_to_point[w] for w in v]
                rays = [util.hypotenuse(origin, t) for t in targets]
                total = sum(rays)
                endlen += total
            print endlen / startlen
