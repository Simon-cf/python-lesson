# 回顾一下昨天爬取药监局的步骤

import requests
import json

if __name__ == "__main__":
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
    }
    numbers = int(input("please enter pages:"))
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    for page in range(1, numbers + 1):
        data = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
        }

        json_ids = requests.post(url=url, data=data, headers=headers).json()
        fp = open('details' + str(page) + ".json", 'w', encoding='utf-8')
        json.dump(json_ids, fp=fp, ensure_ascii=False)
        ids_list = []
        for company_id in json_ids['list']:
            ids_list.append(company_id['ID'])

    details_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    details_list = []
    for id in ids_list:
        details_data = {
            'id': id
        }
        json_details = requests.post(url=details_url, data=details_data, headers=headers).json()
        details_list.append(json_details)

    fp = open('details.json', 'w', encoding='utf-8')
    json.dump(details_list, fp=fp, ensure_ascii=False)
    print("抓取成功")


