import re
import requests


if __name__ == '__main__':
    url = "https://www.qiushibaike.com/imgrank/"
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    page_text = requests.get(url=url, headers=headers).text
    print(page_text)
