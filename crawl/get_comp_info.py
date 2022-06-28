import requests
from config import GBIZ_CLIENT_KEY 
import csv

def get_info(hojin_num:str):
    query = f"?corporate_number={hojin_num}"
    url = f"https://info.gbiz.go.jp/hojin/v1/hojin/{hojin_num}/patent"

    header = {
    "Accept": "application/json",
    "X-hojinInfo-api-token": GBIZ_CLIENT_KEY
    }

    result = requests.get(url, headers=header)
    return result.json()["hojin-infos"][0]

def get_hojin_infos():
    num = 0
    data_list = []
    keys = ["corporate_number","location","name","employee_number","company_size_male","company_size_female","company_url","average_age","average_continuous_service_years_Male","average_continuous_service_years_Female","patent"]
    headers = ["corporate_number","location","name","employee_number","company_size_male","company_size_female","company_url","average_age","month_average_predetermined_overtime_hours","average_continuous_service_years_Male","average_continuous_service_years_Female","shohyo","tokkyo","others"]
    with open("./comp_inf_tmp.csv", "r", encoding="utf-8") as csv_file:
        files = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        for file in files:
            result_to_dic = {}
            result = get_info(file["hojin_num"])
            test = [0,0,0]
            for h in keys:
                if h in result:
                    if h == "patent":
                        for n in result[h]:
                            if n["patent_type"] == "商標":
                                test[0] += 1
                            elif n["patent_type"] == "特許":
                                test[1] += 1
                            else:
                                test[2] += 1
                        result_to_dic["shohyo"] = test[0]
                        result_to_dic["tokkyo"] = test[1]
                        result_to_dic["others"] = test[2]
                        continue
                    result_to_dic[h] = result[h]
                    if h == "workplace_info":
                        result_to_dic["average_age"] = result[h]["base_infos"]["average_age"]
                        result_to_dic["month_average_predetermined_overtime_hours"]  = result[h]["base_infos"]["month_average_predetermined_overtime_hours"]
                        result_to_dic["average_continuous_service_years_Male"]  = result[h]["base_infos"]["average_continuous_service_years_Male"]
                        result_to_dic["average_continuous_service_years_Female"]  = result[h]["base_infos"]["average_continuous_service_years_Female"]
                        continue

                else:
                    result_to_dic[h] = ""

            data_list.append(result_to_dic)
            num += 1
            print(num)
    print(data_list[:3])
    with open("./test_result.csv","w",encoding="utf8") as f:
        writer = csv.DictWriter(f,fieldnames=headers)
        writer.writeheader()
        for d in data_list:
            writer.writerow(d)

# print(get_info("5011001042496"))
get_hojin_infos()
