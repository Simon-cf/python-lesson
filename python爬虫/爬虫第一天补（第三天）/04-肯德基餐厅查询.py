import requests
import json

if __name__ == "__main__":
    # 1)指定url,确定参数
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    kw = input("please enter the address:")
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10'
    }

    # 2）UA伪装，模拟浏览器发送请求并得到响应对象
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"

    }
    response = requests.post(url=url, data=data, headers=headers)

    # 3.处理响应数据
    page_text = response.text

    # 4.持久化存储
    FileName = kw + '肯德基餐厅地点.json'
    with open(FileName, 'w', encoding="utf-8") as fp:
        json.dump(page_text, fp=fp, ensure_ascii=False)

    print("抓取成功")
