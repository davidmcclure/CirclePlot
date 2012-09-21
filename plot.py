import matplotlib.pyplot as plt
import requests as req


class Plot:


    def __init__(self, text):

        '''Create circle.

        :return void.'''

        self.circle = Circle()


    def paste_stream(self, stream):

        '''Register text from direct stream.

        :param string stream: The text stream.

        :return void.'''

        self.circle.register_text(Text(stream))


    def load_url(self, url):

        '''Register a text from a URL.

        :param string url: The url.

        :return void.'''

        res = req.get(url)
        self.circle.register_text(res.text)


    def load_file(self, path):

        '''Register a text from a file.

        :param string path: The filepath.

        :return void.'''

        f = open(path, 'w')
        print f
        self.circle.register_text(res.text)
