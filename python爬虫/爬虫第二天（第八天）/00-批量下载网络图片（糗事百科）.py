import requests


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"}

    url = 'https://pic.qiushibaike.com/system/pictures/12383/123838762/medium/729T73UZ7WAUMFCO.jpg'
    img_data = requests.get(url=url, headers=headers).content
    with open('1.jpg', 'wb') as fp:
        fp.write(img_data)


if __name__ == '__main__':
    main()
