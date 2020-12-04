import requests
import json

if __name__ == "__main__":

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"}
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    number = input("请输入您想要爬取的页面：")
    id_list = []

    for page in range(1, int(number) + 1):

        data = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url, data=data, headers=headers).json()
        for company_dict in json_ids['list']:
            id_list.append(company_dict['ID'])

    details = []
    details_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        data = {
            'id': id
        }
        json_detail = requests.post(url=details_url, data=data, headers=headers).json()
        details.append(json_detail)

    fp = open('details.json', 'w', encoding='utf-8')
    json.dump(details, fp=fp, ensure_ascii=False)

    print("爬取成功")
