import requests
import json

if __name__ == "__main__":
    url = "https://translate.sogou.com/reventondc/suggV3"
    word = input("please enter a world:")
    data = {
        'from': 'auto',
        'to': 'zh - CHS',
        'client': 'wap',
        'text': word,
        'uuid': '3ca7c756-96a8-4c29-8e92-512fd7fd7e1b',
        'pid': 'sogou - dict - vr',
        'addSugg': 'on'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
    }

    page_json = requests.post(url=url, data=data, headers=headers).json()

    fileName = word + ".json"
    fp = open(fileName, 'w', encoding='utf-8')
    
