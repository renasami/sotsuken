
from typing import List
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time 
import os
import re
import csv
url = "https://xn--vckya7nx51ik9ay55a3l3a.com/industries/5250"
url2 = "https://xn--vckya7nx51ik9ay55a3l3a.com"

page_num = 0

#main > div.page-wrapper > div.page-body > section:nth-child(2) > h3 > a
#TODO:void(0)の対策を入れる
links = []

def get_comp_link(url,page_num):
    query =  f"?page={page_num}"
    page_url = ""
    if page_num == 0:
        page_url = url
    else:
        page_url = url + query
    print(page_url)
    headers = {
    'User-Agent':'Mozilla/5.0'
    }

    html = requests.get(page_url,headers=headers)
    print(html)
    soup = BeautifulSoup(html.content,"html.parser")
    for elem in soup.find_all("h3"):
        for e in elem.find_all("a"):
            link = str(e.get("href"))
            if link not in links:
                links.append(str(e.get("href")))
    page_num += 1
    time.sleep(1)
    if page_num == 28:
        get_comp_info(url2,links)
        return
    return get_comp_link(url,page_num)

def is_hojin_num(arg:str):
    if len(arg) >13:
        num = arg[:13]
        if num.isdecimal():
            return (True,num)
    return (False,"")

# with open("comp_links.txt","w") as f:
#     get_comp_link(url,0)
#     f.write(str(links))
hojin = ['/companies/1973', '/companies/2138', '/companies/2303', '/companies/2307', '/companies/2315', '/companies/2317', '/companies/2321', '/companies/2323', '/companies/2326', '/companies/2327', '/companies/2329', '/companies/2330', '/companies/2332', '/companies/2335', '/companies/2338', '/companies/2345', '/companies/2349', '/companies/2351', '/companies/2352', '/companies/2354', '/companies/2359', '/companies/2411', '/companies/2484', '/companies/3040', '/companies/3042', '/companies/3371', '/companies/3622', '/companies/3623', '/companies/3624', '/companies/3625', '/companies/3626', '/companies/3627', '/companies/3628', '/companies/3630', '/companies/3632', '/companies/3633', '/companies/3634', '/companies/3635', '/companies/3636', '/companies/3639', '/companies/3640', '/companies/3641', '/companies/3645', '/companies/3646', '/companies/3647', '/companies/3648', '/companies/3649', '/companies/3652', '/companies/3653', '/companies/3655', '/companies/3656', '/companies/3657', '/companies/3658', '/companies/3659', '/companies/3660', '/companies/3662', '/companies/3663', '/companies/3664', '/companies/3665', '/companies/3666', '/companies/3667', '/companies/3668', '/companies/3671', '/companies/3672', '/companies/3673', '/companies/3674', '/companies/3675', '/companies/3677', '/companies/3678', '/companies/3679', '/companies/3681', '/companies/3682', '/companies/3683', '/companies/3686', '/companies/3687', '/companies/3688', '/companies/3689', '/companies/3691', '/companies/3692', '/companies/3694', '/companies/3695', '/companies/3696', '/companies/3697', '/companies/3698', '/companies/3710', '/companies/3711', '/companies/3712', '/companies/3719', '/companies/3723', '/companies/3727', '/companies/3733', '/companies/3738', '/companies/3741', '/companies/3744', '/companies/3747', '/companies/3750', '/companies/3751', '/companies/3753', '/companies/3756', '/companies/3758', '/companies/3760', '/companies/3762', '/companies/3763', '/companies/3765', '/companies/3766', '/companies/3768', '/companies/3769', '/companies/3770', '/companies/3771', '/companies/3773', '/companies/3774', '/companies/3776', '/companies/3777', '/companies/3778', '/companies/3779', '/companies/3782', '/companies/3784', '/companies/3787', '/companies/3788', '/companies/3791', '/companies/3793', '/companies/3796', '/companies/3798', '/companies/3799', '/companies/3800', '/companies/3803', '/companies/3804', '/companies/3807', '/companies/3810', '/companies/3814', '/companies/3815', '/companies/3816', '/companies/3817', '/companies/3822', '/companies/3823', '/companies/3825', '/companies/3826', '/companies/3834', '/companies/3835', '/companies/3836', '/companies/3837', '/companies/3839', '/companies/3840', '/companies/3841', '/companies/3842', '/companies/3843', '/companies/3844', '/companies/3845', '/companies/3847', '/companies/3848', '/companies/3850', '/companies/3851', '/companies/3852', '/companies/3853', '/companies/3854', '/companies/3856', '/companies/3857', '/companies/3858', '/companies/3900', '/companies/3901', '/companies/3902', '/companies/3903', '/companies/3904', '/companies/3905', '/companies/3906', '/companies/3907', '/companies/3908', '/companies/3910', '/companies/3911', '/companies/3912', '/companies/3913', '/companies/3914', '/companies/3915', '/companies/3916', '/companies/3917', '/companies/3918', '/companies/3919', '/companies/3920', '/companies/3921', '/companies/3922', '/companies/3923', '/companies/3924', '/companies/3925', '/companies/3926', '/companies/3927', '/companies/3928', '/companies/3929', '/companies/3930', '/companies/3931', '/companies/3932', '/companies/3933', '/companies/3934', '/companies/3935', '/companies/3936', '/companies/3937', '/companies/3938', '/companies/3939', '/companies/3940', '/companies/3960', '/companies/3961']
# hojin = ['/companies/1973', '/companies/2138']
test_lis = []
fieldnames = ["name","hojin_num","edinet","site_url"]
def get_comp_info(url,links:list):
    # test_lis.append(fieldnames)
    for link in links:
        print(link)
        comp_labeled =  {
            "name":"",
            "hojin_num":"",
            "edinet":"",
            "site_url":"",
        }
        page_url = url + link

        headers = {
        'User-Agent':'Mozilla/5.0'
        }

        html = requests.get(page_url, headers=headers)
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.content,"html.parser")
        hojin_num = soup.select(".companies_data")
        current = soup.select(".current")[0]

        comp_labeled["name"] = current.text
        for hoj in hojin_num:
            (is_true,hojin_num) = is_hojin_num(hoj.text.strip())
            if is_true:
                comp_labeled["hojin_num"] = hojin_num
            if "E" in hoj.text:
                comp_labeled["edinet"] = hoj.text.strip()
            elif "http" in hoj.text:
                comp_labeled["site_url"] = hoj.text.strip()
        test_lis.append(comp_labeled)
get_comp_link(url,page_num)

with open("it_comp_inf_tmp.csv","w") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for n in test_lis:
        writer.writerow(n)

# print(test_lis)