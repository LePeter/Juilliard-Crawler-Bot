# Juilliard-Crawler-Bot
Web Crawler Spider for extraction of course data from [Juilliard](http://catalog.juilliard.edu/content.php?catoid=25&navoid=2696).

## Running the Spider 
In order to run the crawler, you must have Python 2.7 or higher and have installed BeautifulSoup 4 and Scrapy Framework.
Execute the following command in the Julliard/ root directory.  The outputs should be in the results.csv file.
- scrapy crawl juilliardSpider -o results.csv -t csv


