import requests
import csv 

from config import YAHOO_CLIENT_KEY 

def get_company():
    response = requests.get('https://job.yahooapis.jp/v1/furusato/company/?appid={}'.format(YAHOO_CLIENT_KEY))    
    with open('test.csv', 'w') as csv_file:
        fieldnames = ['name', 'prefecture','city','town','block','building','presidentPosition','presidentName','capital','employees','establishmentDate','listed','stockCode','averageAge','femaleRate','averageAnnualIncome','paidHolidayDigestibility','turnoverRate','handicappedEmployeeRate','femaleManagerRate','averageDuration','sales','salesDate','currentEarnings','currentEarningsDate','webUrl','prText','remarks']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for n in response.json()["results"] :
            dic = {}
            for s in fieldnames:
                dic[s] = n[s]
            writer.writerow(dic)

get_company()