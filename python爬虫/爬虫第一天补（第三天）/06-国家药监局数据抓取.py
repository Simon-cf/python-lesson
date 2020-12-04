import requests
import json

if __name__ == "__main__":
    id_list = []
    # UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    # 1)指定url并处理参数
    page = input("please enter pages:")
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    for page in range(1, int(page) + 1):
        data = {
            'on': 'true',
            'page': '1',
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        # 2)发起请求得到数据
        json_ids = requests.post(url=url, data=data, headers=headers).json()

        # 得到id列表

        for id in json_ids['list']:
            id_list.append(id['ID'])

    detail_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    details_list = []
    for id in id_list:
        detail_data = {
            'id': id
        }
        json_details = requests.post(url=detail_url, data=detail_data, headers=headers).json()
        details_list.append(json_details)

    # 3）持久化存储
    fb = open('details.json', 'w', encoding='utf-8')
    json.dump(details_list, fb, ensure_ascii=False)
    print("over!!!")
# http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=e02b9ae90a0e419f93e7baf64a022dfb
# http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=c03863ccafe84187a05427fc6bf9603e
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
