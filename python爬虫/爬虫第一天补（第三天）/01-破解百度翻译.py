import requests
import json

if __name__ == "__main__":
    # 1.指定url,并且设置参数
    url = "https://fanyi.baidu.com/sug"
    word = input("please enter a word:")
    data = {
        "kw": word
    }
    # 2.UA伪装，并发起请求（确定请求类型）得到请求对象
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"

    }
    response = requests.post(url=url, data=data, headers=headers)
    # 3.对得到的响应对象进行数据处理 如果响应（response）的数据类型是json类型，可以使用json()方法，得到一个json字典对象
    dic_obj = response.json()
    print(dic_obj)
    # 4.持久化存储数据
    FileName = word + ".json"
    with open(FileName, 'w', encoding="utf-8") as fp:
        json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print("翻译成功")

# 函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象。
a = open('1.txt', 'w')
json.dump([1, 2, 3], fp=a)
# python中对文件进行操作的时候，必须先打开文件,再进行后续的操作。
# 函数json.load()可以将json类型的数据加载到内存
