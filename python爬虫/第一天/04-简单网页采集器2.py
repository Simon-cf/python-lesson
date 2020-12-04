import requests

if __name__ == "__main__":
    url = "https://www.baidu.com/s"
    kw = input("Please enter the keyword you wanna searching...")
    param = {
        'wd' : kw
    }
    # UA伪装（伪装成是通过浏览器来请求的）
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    # 发送请求，得到响应对象
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    FileName = kw + ".html"
    with open(FileName, 'w', encoding="utf-8") as fb:
        fb.write(page_text)
    print("抓取成功")
