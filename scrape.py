import bs4 as bs
import urllib.request

def get_paragraphs(url):
        """ Using beautiful soup, scrape the paragraphs from a specified page """

        source = urllib.request.urlopen(url).read()

        soup = bs.BeautifulSoup(source,'lxml')

        paragraphs = []

        for paragraph in soup.find_all('p'):
            paragraphs.append(paragraph.text)

        return paragraphs

if __name__ == "__main__":
    source = urllib.request.urlopen('http://www.thelatinlibrary.com/cicero/arch.shtml').read()
    paragraphs = get_paragraphs(source)
    for paragraph in paragraphs:
        print(paragraph)
