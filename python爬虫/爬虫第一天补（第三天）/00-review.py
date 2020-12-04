import requests

# 爬取搜狗
if __name__ == "__main__":
    # 1）指定url,并且对它进行处理，
    url = "https://www.sogou.com/web?"
    kw = input("please enter a word:")
    param = {
        "query": kw
    }

    # 2）UA伪装反反爬策略，模拟浏览器发起请求，得到响应对象
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }

    response = requests.get(url=url, params=param, headers=headers)
    # 3）对响应对象进行处理
    page_text = response.text

    # 4）持久化存储
    FileName = kw + ".html"
    with open(FileName, "w", encoding="utf-8") as fb:
        fb.write(page_text)

    print("爬取成功...")
