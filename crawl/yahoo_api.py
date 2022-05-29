from requests import Request
import requests
import csv 
import asyncio

from config import YAHOO_CLIENT_KEY 
from util.requests import YahooRequest

def get_company():
    yahoo_request = YahooRequest(url="https://job.yahooapis.jp/v1/furusato/company",key=YAHOO_CLIENT_KEY)

    with open('test.csv', 'w') as csv_file:
        fieldnames = ['name', 'prefecture','city','town','block','building','presidentPosition','presidentName','capital','employees','establishmentDate','listed','stockCode','averageAge','femaleRate','averageAnnualIncome','paidHolidayDigestibility','turnoverRate','handicappedEmployeeRate','femaleManagerRate','averageDuration','sales','salesDate','currentEarnings','currentEarningsDate','webUrl','prText','remarks']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        response =  yahoo_request.get_with_params()
        for n in response:
            dic = {}
            for s in fieldnames:
                dic[s] = n[s]
            writer.writerow(dic)
get_company()
# loop = asynci?o.get_event_loop()
# loop.run_until?_complete(get_company())
