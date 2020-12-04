import requests
import json

if __name__ == "__main__":
    # 1)指定url,并处理参数
    url = "https://movie.douban.com/j/chart/top_list?"
    number = input("please tell me the numbers you wanna get:")
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': number
    }

    # 2.UA伪装，模拟浏览器发起请求（判断请求类型）并得到响应对象
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    response = requests.get(url=url, params=param, headers=headers)

    # 3.处理响应数据
    list_obj = response.json()

    # 4.持久化存储
    fp = open('豆瓣喜剧电影排行榜.json', 'w', encoding="utf-8")
    json.dump(list_obj, fp=fp, ensure_ascii=False)
    print("over")
