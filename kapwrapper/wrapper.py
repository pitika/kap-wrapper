import requests
import re
from datetime import datetime, timedelta
from lxml import html

from .models import *

class Wrapper:
    def get(self, url):
        response = requests.get(url=url)
        return self.__parse_kap(response.content)

    def __get_value(self, tree, xpath):
        return tree.xpath(xpath)[0].strip() if len(tree.xpath(xpath)) else ""

    def __parse_kap(self, content):
        tree = html.fromstring(content)
        return Kap({
            "founder": self.__get_value(tree, '//*[@id="printAreaDiv"]/div[2]/div[6]/p/text()'),
            "start_date": self.__get_value(tree, '//*[@id="printAreaDiv"]/div[2]/div[14]/div/a[2]/div[2]/text()'),
            "duration": self.__get_value(tree, '//*[@id="printAreaDiv"]/div[2]/div[16]/text()'),
            "fund_url": self.__get_value(tree, '//*[@id="printAreaDiv"]/div[2]/div[22]/div/a[2]/div[1]/text()'),
            "strategy": self.__get_value(tree, '//*[@id="printAreaDiv"]/div[2]/div[24]/div/a[2]/div[1]/text()'),
            "risk_rate": self.__get_value(tree, '//*[@id="printAreaDiv"]/div[2]/div[24]/div/a[2]/div[2]/text()'),
            "daily_cost": self.__get_value(tree, '//*[@id="printAreaDiv"]/div[4]/div[2]/div/a[2]/div[4]/text()'),
            "annual_cost": self.__get_value(tree, '//*[@id="printAreaDiv"]/div[4]/div[2]/div/a[2]/div[5]/text()')
        })
