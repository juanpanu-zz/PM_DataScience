# %%
import scrapy
# %%
class Spider12 (scrapy.Spider):
    name = 'spider12'
    allowed_domains = ['pagina12.com.ar']
    custom_settings = {'FEED_FORMAT':'json',
                        'FEED_URI':'resultados.json',
                        'FEED_EXPORT_ENCODING': 'utf-8',
                        'DEPTH_LIMIT':2}

    start_urls = ['https://www.pagina12.com.ar/secciones/el-pais',
                'https://www.pagina12.com.ar/secciones/universidad-diario',
                'https://www.pagina12.com.ar/secciones/economia',
                'https://www.pagina12.com.ar/secciones/sociedad',
                'https://www.pagina12.com.ar/suplementos/cultura-y-espectaculos',
                'https://www.pagina12.com.ar/secciones/el-mundo',
                'https://www.pagina12.com.ar/secciones/deportes',
                'https://www.pagina12.com.ar/secciones/contratapa']
    def parse(self, response):
        # Articulo promocionado
        nota_promocionada = response.xpath('//div[@class="featured-article_container"]/h2/a/@href').get()
        if nota_promocionada is not None:
            yield response.follow(nota_promocionada, callback = self.parse_nota)
        # Listado Notas
        notas = response.xpath('//ul[@class="article-list"]//li//a/@href').getall()
        for nota in notas:
            yield response.follow(nota, callback = self.parse_nota)
        # LinL siguiente pagina
        next_page = response.xpath('//a[@class="pagination-bin-next"]/href')
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)


    def parse_nota(self,response):
        #parseo nota
        titulo = response.xpath('//h1[@class="article-title"]/text()').get()
        cuerpo = ''.join(response.xpath('//div[@class=article-text]/p/text()').getall())
        yield{'url':response.url,
            'titulo':titulo,
            'cuerpo':cuerpo}
# %%
from scrapy.crawler import CrawlerProcess
# %%
process = CrawlerProcess()
process.crawl(Spider12)
process.start()
# %%
import requests
import re
# %%
def get_my_ip(url='http://www.cualesmiip.com/',proxies=None):
    try:
        r = requests.get(url=url,proxies=proxies)
    except Exception as e:
        print('Error haciendo la request', e)
        return None
    if r.status_code != 200:
        print('status Code', r.status_code)
        return None

    regex = re. compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3})')
    my_ip = regex.findall(r.text)
    return my_ip[0] if my_ip else None
#%%
get_my_ip()
# %%
proxy_dict = {'http':'http://181.3.27.96:7071',
                'https':'https://181.3.27.96:7071'}
#%%
get_my_ip(proxies=proxy_dict)
# %%
