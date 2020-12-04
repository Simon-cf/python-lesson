import requests
import json

if __name__ == "__main__":
    # 流程分析
    # 1.首页关于公司的信息是通过Ajax来请求获得的,直接对网页对应的url发起请求得不到各个公司的数据
    # （也就是我们想要各个国内公司的各自的超链接来进入他们所对应的详情页获取信息，这步是没有办法实现的）
    # 2.通过ajax发起请求得到相应的各个公司的数据后，没有超链接，但是有对应的id,通过id可以拼接为url
    # 进入各个公司各自的详情页（各个公司的详情页url前面部分都是相同的），但是对这个url发起请求得不到对应公司的详情页详细信息
    # （详情页也是通过Ajax来请求获取数据的）

    ## 实现步骤
    # 1）获取各个公司的id,得到id列表
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    ids_list = []
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    numbers = int(input("请输入您想要爬取的页数（max=360）："))
    for page in range(1, numbers + 1):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url, data=data, headers=headers).json()
        for company in json_ids['list']:
            ids_list.append(company['ID'])


    # 2）对每个id对应的详情页请求，得到数据,并将各个公司详情页数据存储在ids_details_list中
    ids_details_list = []
    details_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in ids_list:
        details_data = {
            'id': id
        }
        json_ids_details = requests.post(url=details_url, data=details_data, headers=headers).json()
        ids_details_list.append(json_ids_details)


    # 3）持久性存储数据
    fp = open('药监局详情页数据.json', 'w', encoding='utf-8')
    json.dump(ids_details_list, fp, ensure_ascii=False)
    print("抓取成功！！！")
