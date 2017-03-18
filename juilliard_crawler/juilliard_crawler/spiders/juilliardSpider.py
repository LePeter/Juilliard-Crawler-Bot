from scrapy.spiders import CrawlSpider, Rule, BaseSpider, Spider
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from juilliard_crawler.items import JuilliardCrawlerItem

class MyFirstSpider(CrawlSpider):
    name = 'juilliardSpider'
    allowed_domains = ['catalog.juilliard.edu']
    start_urls = ['http://catalog.juilliard.edu/content.php?catoid=25&navoid=2696']




def parse_item(self, response):
    SET_SELECTOR = '.ajaxcourseindentfix'

    #loops through each ajaxcourseindentfix class
    for juilliardset in response.css(SET_SELECTOR):
        TITLE_SELECTOR = 'h3 ::text'

        yield{
            'title': juilliardset.css(NAME_SELECTOR).extract_first(),

        }





    #loops through and crawl through each indexes of a next link.  stop once no
    #more links are found
    NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
    next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
    if next_page:
        yield scrapy.Request(
            response.urljoin(next_page),
            callback = self.parse
        )
