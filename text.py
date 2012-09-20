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


    def zipper(self, length):

        '''Yield heads and tails of segments.

        :param int length: The segment length.

        :yield tuple: The head and tail.'''

        for i in range(1, len(self.tokens) - length):
            yield (self.tokens[i], self.tokens[i+length])
