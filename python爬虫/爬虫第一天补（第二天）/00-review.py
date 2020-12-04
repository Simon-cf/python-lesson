import requests

# 网页采集器回顾（bing为例）
if __name__ == "__main__":
    # 使用request简单步骤
    # 1)指定url并且对它进行处理
    url = "https://cn.bing.com/search?"
    kw = input("Please enter the keyword you wanna serching...")
    # 处理url
    param = {
        "q": kw
    }
    # UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }

    # 2)发起请求（UA伪装，反反爬策略），得到响应对象
    response = requests.get(url=url, params=param, headers= headers)

    # 3)对爬取得到的响应对象进行处理
    page_text = response.text

    # 4）永久性存储
    FileName = kw + ".html"
    with open(FileName, "w", encoding="utf-8") as fb:
        fb.write(page_text)

    print("抓取成功")
