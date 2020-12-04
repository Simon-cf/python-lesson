import requests
import json

if __name__ == '__main__':
    # UA伪装，模拟浏览器向服务器发起请求
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52"
    }
    # 1.处理url
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    numbers = int(input("亲输入您想要爬取的页码数："))
    ids_list = []

    for page in range(1, numbers + 1):

        # 处理参数
        data = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': ''
        }
        json_ids = requests.post(url=url, data=data, headers=headers).json()

        for company_dict in json_ids["list"]:
            ids_list.append(company_dict["ID"])

    details_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    details_list = []
    for id in ids_list:
        data = {
            'id': id
        }
        json_details = requests.post(url=details_url, data=data, headers=headers).json()
        details_list.append(json_details)

    fp = open('details.json', 'w', encoding="utf-8")
    json.dump(details_list, fp=fp, ensure_ascii=False)
    print("抓取成功...")
