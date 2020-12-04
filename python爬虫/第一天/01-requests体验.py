import requests
if __name__ == "__main__":
    # 指定url,
    url = "https://www.bilibili.com/"
    # 向指定的url发起请求,并返回一个响应对象
    response = requests.get(url=url)
    # 需要想要的数据里面的文本内容
    page_text = response.text
    print(page_text)
    # 持久化存储数据
    with open('bilibili.html', 'w', encoding="utf-8") as fb:
        fb.write(page_text)
