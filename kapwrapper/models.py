from enum import Enum


class Base:
    def __repr__(self):
        return str(self.__dict__)


class Kap(Base):
    def __init__(self, data):
        self.founder = data["founder"]
        self.start_date = data["start_date"]
        self.duration = data["duration"]
        self.fund_url = data["fund_url"]
        self.strategy = data["strategy"]
        self.risk_rate = data["risk_rate"]
        self.daily_cost = data["daily_cost"]
        self.annual_cost = data["annual_cost"]
