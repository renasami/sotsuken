# 業界
# 企業規模(売上)
# 企業規模(人数)
# 企業規模(上場or非上場)
# 平均年齢
# 勤続年数
# 特許数
# 設立からの年数
# 待遇(給与)
# 時間外労働
# 女性労働者の割合
import random
import math
import csv

num = int(input("ダミーデータの数を入れる:"))
print("it系の業界であるという前提で始める。")
lis = []
list_of_cols = ["名前","売上","従業員数","上場or非上場","平均年齢","平均勤続年数","特許数","設立からの経過","平均給与", "時間外労働","女の割合"]

for n in range(num):
    s = random.randint(0,1)
    salse = random.randint(200,100000)if s == 1 else random.randint(1,199)
    dummy_dic={
    "名前":f"{n}株式会社",
    "売上":salse,
    "従業員数":random.randint(10 if salse < 199 else 50, 1000 if salse < 199 else 10000),
    "上場or非上場":s,
    "平均年齢":random.randint(25,53),
    "平均勤続年数":random.randint(3,25),
    "特許数":random.randint(0,100),
    "設立からの経過":random.randint(3,100),
    "平均給与":random.randint(360,800), 
    "時間外労働":random.randint(1,60),
    "女の割合":random.randint(20,50)
    }
    lis.append(dummy_dic)
with open('random.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=list_of_cols)
    writer.writeheader()
    for n in lis:
        writer.writerow(n)