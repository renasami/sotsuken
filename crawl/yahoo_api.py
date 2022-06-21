from requests import Request
import requests
import csv 
import asyncio

from config import YAHOO_CLIENT_KEY 
from util.requests import YahooRequest

def get_company():
    yahoo_request = YahooRequest(url="https://job.yahooapis.jp/v1/furusato/company",key=YAHOO_CLIENT_KEY)
    comp_name_list = []
    comp_list = []
    with open('fin_to_analyze.csv', 'w') as csv_file:
        # fieldnames = ['name', 'prefecture','city','town','block','building','presidentPosition','presidentName','capital','employees','establishmentDate','listed','stockCode','averageAge','femaleRate','averageAnnualIncome','paidHolidayDigestibility','turnoverRate','handicappedEmployeeRate','femaleManagerRate','averageDuration','sales','salesDate','currentEarnings','currentEarningsDate','webUrl','prText','remarks']
        fieldnames = ["name","capital","employees","establishmentDate","listed","averageAge","femaleRate","averageAnnualIncome","paidHolidayDigestibility","turnoverRate","femaleManagerRate","handicappedEmployeeRate","averageDuration","sales","salesDate","currentEarnings","currentEarningsDate"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        response =  yahoo_request.get_with_params()

        for n in response:
            dic = {}
            for s in fieldnames:
                dic[s] = n[s]
            # writer.writerow(dic)
            if n['name'] not in comp_name_list:
                comp_list.append(dic)
                comp_name_list.append(n['name'])
        for comp in comp_list:
            writer.writerow(comp)

get_company()
# loop = asynci?o.get_event_loop()
# loop.run_until?_complete(get_company())
