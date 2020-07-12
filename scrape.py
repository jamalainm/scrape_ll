import bs4 as bs
import urllib.request

class Text:
    """
    This is an object made up of paragraphs scraped from a specified page from the Latin Library.
    Maybe this shouldn't be a class but just a single function.

    ...

    Attributes
    ----------

    source : string
        The url for a specific work by a particular author on the Latin Library

    Methods
    -------

    make_text():
        return a list of paragraphs from the specified source

    """

    def __init__(self,source):
        self.source = source

    def make_text(self):
        """ Using beautiful soup, scrape the paragraphs from a page """

        soup = bs.BeautifulSoup(self.source,'lxml')

        paragraphs = []

        for paragraph in soup.find_all('p'):
            paragraphs.append(paragraph.text)

        return paragraphs

if __name__ == "__main__":
    source = urllib.request.urlopen('http://www.thelatinlibrary.com/cicero/arch.shtml').read()
    proArchia = Text(source)
    paragraphs = proArchia.make_text()
    for paragraph in paragraphs:
        print(paragraph)
