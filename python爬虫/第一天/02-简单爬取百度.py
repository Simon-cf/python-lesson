import requests
if __name__ == "__main__":
    url = "http://www.baidu.com"
    response = requests.get(url=url)
    page_text = response.text
    with open('baidu.html', 'w', encoding="utf-8") as fp:
        fp.write(page_text)
    print(page_text)