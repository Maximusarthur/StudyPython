import json
import csv


def jsonDeal(jfile):
    jf_path = jfile
    with open(jf_path, 'r') as jf:
        a = json.load(jf)
        b = json.loads(a['result'])
        print(b)
        print(b['listPrice'])
        for item in b['listPrice']:
            item.update({'日期': item.pop("sdt")})
            item.update({'价格': item.pop("pr")})
            del item['oldPrice']
            del item['yh']
            item['商品名称'] = b['spName']
            item['编码'] = '1101010501'
            if jf_path == '1101010501_1.json':
                item['序号'] = 1
            elif jf_path == '1101010501_2.json':
                item['序号'] = 2
            elif jf_path == '1101010501_3.json':
                item['序号'] = 3
        print(b['listPrice'])

        with open("../experiment_2/csvfile.csv", "a+", newline="") as cf:
            csvf = csv.DictWriter(cf, ["序号", "编码", "日期", "价格", "商品名称"])
            csvf.writeheader()
            csvf.writerows(b['listPrice'])


jsonDeal("1101010501_1.json")
jsonDeal("1101010501_2.json")
jsonDeal("1101010501_3.json")
