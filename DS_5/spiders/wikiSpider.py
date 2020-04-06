# REMOVE THIS AFTER USE

# Task 5

# In this task you should create your very own news data set by scraping it from the web. We will be looking at the "Politics and Conflict" section of the Wikinews site (https://en.wikinews.org/wiki/Category:Politics_and_conflicts), which contains about 7500 articles sorted by the first letter in their title. Since we want the different groups to have slightly different experiences with this data, each group should try to extract the articles for a specific range of letters - given by the python expression:

# "ABCDEFGHIJKLMNOPRSTUVWZABCDEFGHIJKLMNOPRSTUVWZ"[group_nr%23:group_nr%23+10]

# where group_nr is your group number (according to Task 1). The data set you produce should contain fields corresponding to the content of the article, in addition to some metadata fields like the date when the article was written. Describe the tools you used, and any challenges that you faced, and report some basic statistics on the data (e.g. number of rows, fields, etc). Note that there are no fake/no-fake labels in this dataset - we will consider it as a trusted source of only true articles (which is perhaps a bit naive).

#     REMOVE THIS AFTER USE

import scrapy
import string
from urllib.parse import urljoin


# urls passed to class(might not be optimal)
### ROBOTSTXT_OBEY = False write out this change used to scrape some parts of the website ###

# get all links
# response.xpath('//div[@id="mw-pages"]/div/div/div/ul/li/a/@href').extract()
# response.xpath('//div[@id="mw-pages"]/div/div/div/ul/li')  selector 
# '//div[@id="mw-pages"]/a[2]' get link for next page

class wikiSpider(scrapy.Spider):
    name = "wiki"
    # start urls for scraping
    def start_requests(self):
        urls = [
            'https://en.wikinews.org/w/index.php?title=Category:Politics_and_conflicts&from=A',

            #'https://en.wikinews.org/w/index.php?title=Category:Politics_and_conflicts&from=F',

            # 'https://en.wikinews.org/w/index.php?title=Category:Politics_and_conflicts&subcatfrom=F&filefrom=F&pageuntil=Gaddafi+loyalists+go+on+offensive%2C+rebels+pushed+back#mw-pages',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Set the maximum depth### change later to larger number ###
    maxdepth = 1;

    # my own debug dump
    debug_list = [
        "### DEBUG DUMP ALL STEPS ###:",
        "### DEBUG DUMP ALL STEPS ###:",
        "### DEBUG DUMP ALL STEPS ###:",
    ]

    def parse(self, response):
        """ Main method that parse downloaded pages. """
        # Set defaults for the first page that won't have any meta information
        start_url = ''
        from_url = ''
        from_text = ''
        depth = 0;
        # Extract the meta information from the response, if any
        if 'start' in response.meta: start_url = response.meta['start']
        if 'from' in response.meta: from_url = response.meta['from']
        if 'text' in response.meta: from_text = response.meta['text']
        if 'depth' in response.meta: depth = response.meta['depth']
        
        # set start url for crawler
        if depth == 0:
            start_url = response.url

        # if depth == 0:
        #     orginal_url = response.url
        # print("### DEBUG DUMP_B:", orginal_url, "orginal_url END ###")   

        # get all article links ### change to only specifik letters ie E articles ###
        articles = response.xpath('//div[@id="mw-pages"]/div/div/div[1]/ul/li/a/@href').getall() #### change back when all links are needed ('//div[@id="mw-pages"]/div/div/div[1]/ul/li[1]/a/@href')
        for a in articles:
            # yield response.follow(a, callback=self.parse_article)
            url = urljoin(response.url, a)
            yield scrapy.Request(url, callback=self.parse_article)
        print("### DEBUG DUMP_A:", len(articles), "num_of_links END ###")
        print("### DEBUG DUMP_K:", start_url, "END ###")
        print("### DEBUG DUMP_W:", start_url[-1], response.xpath('//div[@id="mw-pages"]/div/div/div[1]/h3/text()').get(), "END ###")


        # Update the print logic to show what page contain a link to the
        # current page, and what was the text of the link
        print("### DEBUG DUMP STEP:", depth, response.url, '<-', from_url, from_text, "END ###")
        # tmp_str = "### DEBUG DUMP STEP:" + depth

        # Browse a tags only if maximum depth has not be reached
        if depth < self.maxdepth and start_url[-1] != 2:
            next_page = response.xpath('//div[@id="mw-pages"]/a[2]') # location of next link ### CHANGE LATER
            next_page_text = next_page.xpath("text()").get()
            next_page_link = next_page.xpath("@href").get()
            print("### DEBUG DUMP_C:", next_page, "next_page END ###")

            if next_page_link is not None:
                request = response.follow(next_page_link, callback=self.parse)
                # Meta information: URL of the current page
                request.meta['from'] = response.url
                # Meta information: text of the link
                request.meta['text'] = next_page_text
                # Meta information: depth of the link
                request.meta['depth'] = depth + 1
                # Meta information: start page for current crawler
                request.meta['start'] = start_url
                yield request
        else:
            # print all debug messages for each step
            for debug_step in (self.debug_list):
                print(*debug_step)

    # get article content
    def parse_article(self, response):
        for info in response.xpath('//div[@id="content"]'):
            yield {
                'title': info.xpath('//*[@id="firstHeading"]/text()').get(),
            }





class testSpider(scrapy.Spider):
    name = "test"
    def start_requests(self):
        urls = [
            'https://en.wikinews.org/wiki/A_policeman_is_killed_and_another_one_is_tortured_in_MST_camp,_in_Brazil',
            
            'https://en.wikinews.org/wiki/African_Union_refuses_to_arrest_Sudan%27s_President_for_war_crimes',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # get article content
    def parse(self, response):
        for info in response.xpath('//div[@id="content"]'):
            yield {
                'title': info.xpath('//*[@id="firstHeading"]/text()').get(),
            }

class test2Spider(scrapy.Spider):
    name = "test2"
    def start_requests(self):
        urls = [
            'https://en.wikinews.org/w/index.php?title=Category:Politics_and_conflicts&from=F',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # get article content
    def parse(self, response):
        for quote in response.xpath('//div[@id="mw-pages"]/div/div/div/ul/li'):
            yield {
                'text': quote.xpath('./a/@href').get(),
            }

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

class articlesSpider(scrapy.Spider):
    name = "articles"
    start_urls = [
        'https://www.phidgets.com/?tier=1&catid=64&pcid=57',
    ]

    def parse(self, response):
        articles = response.xpath("//*[contains(@class, 'ph-summary-entry-ctn')]/a/@href").extract()
        for p in articles:
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_product)

    def parse_product(self, response):
        for info in response.css('div.ph-product-container'):
            yield {
                'product_name': info.css('h2.ph-product-name::text').extract_first(),
                'product_image': info.css('div.ph-product-img-ctn a').xpath('@href').extract(),
                'sku': info.css('span.ph-pid').xpath('@prod-sku').extract_first(),
                'short_description': info.css('div.ph-product-summary::text').extract_first(),
                'price': info.css('h2.ph-product-price > span.price::text').extract_first(),
                'long_description': info.css('div#product_tab_1').extract_first(),
                'specs': info.css('div#product_tab_2').extract_first(),
            }