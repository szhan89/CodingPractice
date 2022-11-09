import requests
from bs4 import BeautifulSoup

class Webscraping(object):
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        self.url = 'https://www.nber.org/papers/w28748'
    
    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        html = response.content.decode('utf-8')
        return html
    
    '''return the following information:
    1. paper title
    2. paper id
    3. paper issue date
    4. paper abstract
    5. author name'''
    def get_info(self):
        html=self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        #file = open('raw_data.csv','w',encoding='utf-8')
        issueDate = soup.time['datetime'] #paper publish time
        paperTitle = soup.title.string #paper title
        _abstract = soup.find_all('div', class_='page-header__intro-inner')[0]
        paperAbstract = str(_abstract).splitlines()[2]#paper abstract
        _authors = soup.find('meta', attrs={'name': 'dcterms.creator'})['content']
        paperAuthors = _authors.split(',')
        
        print(paperTitle)
        print(issueDate)
        print(paperAbstract)
        print(paperAuthors)
        
if __name__ == '__main__':
    scrapper = Webscraping()
    scrapper.get_info()