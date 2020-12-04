import requests

if __name__ == "__main__":
    url = "https://www.baidu.com/s?"
    kw = input("Enter a word")

    param = {
        'wd': kw
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    FileName = kw + ".html"
    with open(FileName, 'w', encoding="UTF-8") as fb:
        fb.write(page_text)
    print(page_text, "保存成功")

### 第一次没有爬取成功，原因是没有用UA伪装