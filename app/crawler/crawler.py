'''
Crawls an XML/HTML document. It can extract urls for further crawling and
optionally store the documents it has visited.
'''
from selenium import webdriver
from lxml import etree
from crawler.storage import Archiver
import urllib.parse as urlparse


class Fetcher(object):

    def __init__(self, driver):
        self.driver = driver

    def fetch(self, url, wait_query):
        self.driver.get(url)
        if wait_query is not None:
            self.driver.find_element_by_xpath(wait_query)
        return self.driver.page_source


class PhantomFetcher(Fetcher):

    def __init__(self):
        driver = webdriver.PhantomJS()
        driver.implicitly_wait(10)
        super(PhantomFetcher, self).__init__(driver)


class Crawler(object):
    '''
    Crawls a page and stores its results in a datastore to await
    further processing.
    :param queries: an array of Query objects, configuring the Crawler.
    :param fetcher: an implementation of Fetcher.
    :param archiver: an implementation of Archiver.
    :param queuer: an implementation of Queuer.
    :param version: version of the Crawler implementation in case we want to
                    reprocess some urls with an updated crawler.
    :param archive: flag dictating if the crawler should store the file after
                    fetching it.
    :param wait_query: an xpath query that must first produce at least one
                       match, before the page is used for url extraction. This
                       allows pages that use javascript to be crawled.

    :returns: a list of Orders
    '''

    def __init__(self, queries,
                 fetcher=PhantomFetcher(),
                 archiver=Archiver(),
                 queuer=None,
                 version=1,
                 archive=False,
                 wait_query=None):
        self.queries = queries
        self.version = version
        self.archive = archive
        self.wait_query = wait_query
        self.fetcher = fetcher
        self.archiver = archiver
        self.queuer = queuer

    def crawl(self, url):
        print("fetching %s" % url)
        html = self.fetcher.fetch(url, self.wait_query)
        if self.archive:
            print("archiving %s" % url)
            self.archiver.archive(url, html)

        if self.queries is not None and self.queuer is not None:
            print("extracting queries")
            orders = self.extract(url, html, self.queries)
            for order in orders:
                self.queuer.que(*order)

    def extract(self, original_url, html, queries):
        tree = etree.HTML(html)
        orders = []
        for query in queries:
            urls = tree.xpath(query.query)
            for url in urls:
                orders.append(
                    (query.crawler, urlparse.urljoin(original_url, url))
                )
        return orders
