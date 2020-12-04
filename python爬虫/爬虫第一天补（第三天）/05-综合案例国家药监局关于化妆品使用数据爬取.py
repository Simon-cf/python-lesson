import requests
import json

if __name__ == "__main__":
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=e02b9ae90a0e419f93e7baf64a022dfb"
    # UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    page_text = requests.get(url=url,headers=headers).text
    with open('化妆品.html', 'w', encoding="utf-8") as fp:
        fp.write(page_text)
    print("over!!!")

    # 没有爬取到页面关于企业的内容--> 用抓包工具测试出来关于企业的内容是通过ajax请求的