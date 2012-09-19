import nltk


class Text:


    def __init__(self, text):

        '''Set the text, tokenize.

        :param string count: The source text.

        :return void.'''

        self.text = text
        self.tokens = []
        self.tokenize()


    def tokenize(self):

        '''Tokenize the text.

        :return void.'''

        self.tokens = nltk.word_tokenize(self.text)


    def zipper(self, length):

        '''Yield all segments of length <length> in order.

        :param int length: The segment length.

        :yield tuple: The segments.'''

        for i in range(len(self.tokens) - length+1):
            yield (self.tokens[i:i+length])
