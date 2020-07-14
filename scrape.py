import bs4 as bs
import urllib.request
import json
from unidecode import unidecode

def get_paragraphs(url):
        """ Using beautiful soup, scrape the paragraphs from a specified page """

        source = urllib.request.urlopen(url).read()

        soup = bs.BeautifulSoup(source,'lxml')

        paragraphs = []

        for paragraph in soup.find_all('p'):
            paragraphs.append(paragraph.text)

        new_paragraphs = []

        for p in paragraphs:
            p = p.lower()
            p = unidecode(p)
            new_paragraphs.append(p)

        return new_paragraphs

if __name__ == "__main__":
    url = 'http://www.thelatinlibrary.com/ter.andria.html'
    paragraphs = get_paragraphs(url)
    filename = 'andria.json'
    with open(filename,'w') as f:
        json.dump(paragraphs,f)
