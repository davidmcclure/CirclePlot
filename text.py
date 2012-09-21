import nltk


class Text:


    def __init__(self, text):

        '''Set the text, tokenize.

        :param string count: The source text.

        :return void.'''

        self.text = text
        self.tokenize()


    def tokenize(self):

        '''Tokenize the text.

        :return void.'''

        self.tokens = nltk.word_tokenize(self.text)
        self.vocab = set(self.tokens)

        # self.tokens = []
        # length = len(self.text)

        # offset = None
        # token = ''

        # for i,c in enumerate(self.text):

        #     if c != ' ':
        #         token += c
        #         if offset is None: offset = i

        #     elif token and (c == ' ' or i+1 == length):
        #         self.tokens.append((token, offset))
        #         offset = None
        #         token = ''


    def zipper(self, length):

        '''Yield heads and tails of segments.

        :param int length: The segment length.

        :yield tuple: The head and tail.'''

        for i in range(1, len(self.tokens) - length):
            yield (self.tokens[i], self.tokens[i+length])


    def snippet(self, marker, total_markers, length):

        '''Get a text snippet at an offset marker.

        :param int marker: The marker.
        :param int total_markers: The total number of markers.
        :param int length: The radial word count of the snippet.

        :return string: The snippet.'''

        pass
