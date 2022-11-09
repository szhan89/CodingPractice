import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from collections import defaultdict

class Webscraping(object):
    DEFAULT_URL = 'https://www.nber.org/papers/' #url format
    NUM_PAPER = 400 #number of paper wish to scraping    
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        self.url = 'https://www.nber.org/papers/'
    
    #this function take download the HTML source with given url
    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        html = response.content.decode('utf-8')
        return html

    #this function parse the HTML with the information we want
    def get_info(self):
        #initialization
        html=self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        #get information
        issueDate = soup.time['datetime'] #paper publish time
        paperTitle = soup.title.string #paper title
        _abstract = soup.find_all('div', class_='page-header__intro-inner')[0]
        paperAbstract = str(_abstract).splitlines()[2]#paper abstract
        _authors = soup.find('meta', attrs={'name': 'dcterms.creator'})['content']
        paperAuthors = _authors.split(',')#paper authors in list
        return [paperTitle, issueDate, paperAbstract,paperAuthors]

    def buildDB(self):
        #initialization
        paperID = 20000
        c1=[]; c2=[]; c3=[]; c4=[]; c5=[]; authorships=[[],[]]
        wp_col = [c1, c2, c3, c4, c5]
        author_dict = defaultdict(int)
        counter = 0
        #linear scraping each webpage once, Time Complexity O(n), n is the same as constant NUM_PAPER
        for i in range(0, self.NUM_PAPER):
            self.url=self.url+'w'+str(paperID)#url update
            print(self.url)
            wp_=self.get_info()#parser function call
            c1.append(str(paperID)); c2.append(wp_[0]); c3.append(wp_[1]); c4.append(wp_[2]); c5+=wp_[3]
            #build an authorship relation
            for eachAuthor in wp_[3]:
                #build a dict for author and author id
                if(eachAuthor not in author_dict):
                    author_dict[eachAuthor.strip()]=10001+counter
                    counter+=1
                #authorship building
                authorships[0].append(author_dict[eachAuthor.strip()])
                authorships[1].append(str(paperID))
                
            self.url=self.DEFAULT_URL#reset the url to default
            paperID+=1
        
        #generate working_papers.csv
        dataframe = pd.DataFrame({'WID':c1, 'title':c2, 'publication_date':c3, 'paperAbstract':c4})
        dataframe.to_csv("working_papers.csv", index=False, sep=',')
        #generate authors.csv
        dataframe2 = pd.DataFrame(author_dict.items(), columns=['authorName', 'authorID'])
        dataframe2.to_csv("authors.csv", index=False, sep=',')
        #generate authorship.csv
        dataframe3 = pd.DataFrame({'authorID':authorships[0], 'WID':authorships[1]})
        dataframe3.to_csv("authorships.csv", index=False, sep=',')
        
if __name__ == '__main__':
    scrapper = Webscraping()
    scrapper.buildDB()