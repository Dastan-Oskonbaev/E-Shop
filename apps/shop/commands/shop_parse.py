from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

import requests
from bs4 import BeautifulSoup

from apps.shop.models import Product


class Command(BaseCommand):
    help = _('Parse data from external source')
    base_url = 'https://www.kivano.kg/mobilnye-telefony'

    # def add_arguments(self, parser):
    #     parser.add_argument('--date', type=str, help=_('Date in format: YYYY-mm-dd'))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(_('Parsing starting!')))
        self.parse(options['date'])
        self.stdout.write(self.style.SUCCESS(_('Parsing finished!')))

    def get_html(self, url):
        response = requests.get(url)
        return response.content

    def get_soup(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def parse(self, date):
        response = self.get_html(f"{self.base_url}")
        soup = self.get_soup(response)
        items_block = soup.find('div', {'class': 'list-view'})

        items_list = items_block.find_all('div', {'class': 'list-view'})

        for news in items_list:
            product = Product()
            product_url = product.find('a', {'class': 'ArticleItem--name'}).get('href')
            product_img = product.find('img', {'class': 'ArticleItem--image-img'}).get('src')
            product.logo = product_img
            product.name = news.find('a', {'class': 'ArticleItem--name'}).text
            # post.content = 'Test'
            product.save()


    # def parse_article(self, url):