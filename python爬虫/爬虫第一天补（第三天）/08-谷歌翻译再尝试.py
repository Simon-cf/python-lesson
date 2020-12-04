import requests
import json

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    url = "https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&source=bh&ssel=0&tsel=0&kc=1&tk=60340.402576&"
    word = input("please enter a word:")
    param = {
        'q': word
    }
    page_json = requests.get(url=url, params=param, headers=headers).text
    FileName = word + '.html'
    fp = open(FileName, 'w', encoding='utf-8')
    json.dump(page_json, fp=fp, ensure_ascii=False)
    print("翻译成功...")
