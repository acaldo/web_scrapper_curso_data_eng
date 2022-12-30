import requests
import bs4

from common import config

class NewsPage:

    def __init__(self,news_site_uid,url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self._url = url

        self._visit(url)

    def _select(self,query_string):
        return self._html.select(query_string)

    def _visit(self,url):
        headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        
        self._html = bs4.BeautifulSoup(response.text,'html.parser')


class HomePage(NewsPage):

    def __init__(self,news_site_uid,url):
        super().__init__(news_site_uid,url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_articles_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)
        

class ArticlePage(NewsPage):
    
        def __init__(self,news_site_uid,url):
            super().__init__(news_site_uid,url)
    
        @property
        def body(self):
            result = self._select(self._queries['article_body'])
            
            text = ''
            if len(result)>0:
                for i in result:
                    text += " " + i.text
            return text
    
        @property
        def title(self):
            result = self._select(self._queries['article_title'])
            text = ''
            if len(result)>0:
                for i in result:
                    text += " " + i.text
            return text

        @property
        def url(self):
            return self._url