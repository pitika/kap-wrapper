import requests
import re
import json
from datetime import datetime, timedelta
from lxml import html

from .models import Kap, FundGroup, Subject

class Wrapper:
    def __init__(self):
        self.data = {}
        self.session = requests.Session()
        res = self.session.get("https://www.kap.org.tr/tr/bildirim-sorgu")
        self.cookies = self.session.cookies.get_dict()
        

    def get(self, url):
        response = requests.get(url=url)
        return self.__parse_kap(response.content)

    def get_funds(self,fund_group: FundGroup, liquidated = False):
        response = requests.get(url="https://www.kap.org.tr/tr/api/fund/" + fund_group.value + "/T" if liquidated else "/Y")
        return json.loads(response.text)

    def get_portfoy_companies(self,fund_group: FundGroup):
        response = requests.get(url="https://www.kap.org.tr/tr/api/fundMembers/" + fund_group.value)
        return json.loads(response.text)

    def __kap_query(self, fund_oid, subject: Subject, from_date, to_date):
        data = {
            "fromDate": from_date,
            "toDate": to_date,
            "subjectList": [subject.value],
            "fundOidList": [fund_oid]
        }

        response = requests.post(url="https://www.kap.org.tr/tr/api/fundDisclosureQuery", json=data)
        
        return json.loads(response.text)

    def get_last_portfoy_url(self, fund_oid):
        from_date = (datetime.today() - timedelta(days=40)).strftime("%Y-%m-%d")
        to_date = datetime.today().strftime("%Y-%m-%d")
        data = self.__kap_query(fund_oid, Subject.PORTFOY_DAGILIM_RAPORU, from_date, to_date)
        
        response = requests.get(url="https://www.kap.org.tr/tr/Bildirim/" + str(data[0]["disclosureIndex"]))

        tree = html.fromstring(response.content)
        attachments = tree.xpath('//*[@id="disclosureContent"]/div/div[4]/a')
        
        return ["https://www.kap.org.tr" + a.get("href") for a in attachments if a.get("href") != "#"]


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