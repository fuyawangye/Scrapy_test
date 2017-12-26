import scrapy

class MySpider(scrapy.Spider):
    name = 'hexun.new'
    old_url = ['http://news.hexun.com/2017-12-10/191928293.html']

    def start_requests(self):
        urls = [
            'http://news.hexun.com/2017-12-10/191928293.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            raw_article = response.css("div.art_context div.art_contextBox").css("p")
            article = []
            for i in raw_article:
                temp_p = []
                p = i.css("p::text").extract()
                a = i.css("a::text").extract()
                if len(p) == 1:
                    article.append(p[0])
                    continue
                elif len(p) == 0:
                    continue
                for index, pices in enumerate(p[0:-1]):
                    temp_p.append(pices)
                    temp_p.append(a[index])
                temp_p.append(p[-1])
                article.append(''.join(temp_p))
        except Exception:
            print(response.url)
            print("ERROR")
            return None
        print(response.url)
        print(' '.join(article))
        new_urls = response.css("div.like a::attr(href)").extract()
        for url in new_urls:
            if url not in self.old_url and url.split('/')[-2] > '2017-01-00':
                self.old_url.append(url)
                yield scrapy.Request(response.urljoin(url))
            # print(len())
        # print(raw_article.css("a::text"))
        # print(article)