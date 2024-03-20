import scrapy
class BukukitaSpider(scrapy.Spider):
    name = "bukukita"
    allowed_domains = ["www.bukukita.com"]
    start_urls = ["https://www.bukukita.com/katalogbuku.php?page="
                  +str(i)for i in range (1,403)]

    def parse(self, response):
        urls = response.css("div.ellipsis a::attr(href)").getall()
        for url in urls :
            if "bukukita.com" not in url:
                url = response.urljoin(url)
        yield scrapy.Request(url)

