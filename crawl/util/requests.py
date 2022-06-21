import requests
from requests import Response 
import asyncio

class Requests:
    def __init__(self,url:str,key:str):
        self.url = url
        self.key = ""

    async def __get(self) -> Response:  
        return await requests.get(self.url + self.key)

    async def __get_with_param(self,param) -> Response:
        keys = list(param.keys())
        data = self.key
        for key in keys:
            data = "{}&{}={}".format(data,key, param[key])
        return await requests.get(self.url+data)

    def get(self):
        data = self.__get(self)

class YahooRequest(Requests):
    def __init__(self,url,key):
        self.url = url
        self.key = "/?appid={}".format(key)

    
    def __get(self) -> Response:  
        res = requests.get(self.url + self.key)
        return res

    def __get_with_param(self,param) -> Response:
        keys = list(param.keys())
        data = self.key
        for key in keys:
            data = "{}&{}={}".format(data,key, str(param[key]))
 
        return  requests.get(self.url+data)

    def get_with_params(self)->list:
        total = self.__get().json()["total"]
        params = {
            "results":100,
            "start": 1
        }
        result = []
        while total > 0:
            try:
                resp = self.__get_with_param(params)

                for n in resp.json()["results"]:
                    result.append(n)
                total -= 100
                params["start"] += 100
                print(total)
            except:
                total -= 100
                params["start"] += 100
                continue
        return result
