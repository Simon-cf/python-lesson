import requests
import json

if __name__ == "__main__":
    # 1)指定url，并对参数进行处理
    url = "https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&otf=2&ssel=0&tsel=0&kc=1&tk=455652.15611&"
    kw = input("enter a word :")
    param = {
        'q': kw
    }
    # 2）UA伪装来设置反反爬策略，发起请求（确定请求的类型）得到响应对象
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    response = requests.get(url=url, params=param, headers=headers)
    print(response)
    # 3）对得到的响应对象的数据进行处理
    list_data = response.json()
    # 4）持久化存储
    FileName = kw + ".json"
    fp = open(FileName, 'w', encoding="gzip")
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print("翻译成功")
