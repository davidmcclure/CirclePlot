import nltk
from nltk.corpus import stopwords


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
