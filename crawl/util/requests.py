import requests
from requests import Response 

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
        print(self)

    async def __get_with_param(self,param) -> Response:
        keys = list(param.keys())
        data = self.key
        for key in keys:
            data = "{}&{}={}".format(data,key, str(param[key]))
        res =  await requests.get(self.url+data)
        return res 

    async def get_with_params(self)->list:
        total = await self.__get(self).total
        params = {
            "results":100,
            "starts": 1
        }
        result = []
        while total > 0:
            resp = await self.__get_with_param(self,params)
            for n in resp.json()["results"]:
                result.append(n)
            total -= 100
            params.starts += 100
        return result