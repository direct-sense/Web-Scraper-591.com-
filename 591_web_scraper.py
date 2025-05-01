import requests
from bs4 import BeautifulSoup

# 發送請求
url = "https://rent.591.com.tw/list"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

# 解析 HTML
soup = BeautifulSoup(response.text, "html.parser")

# 抓出 title 和 price 的元素清單
links = soup.select('a.link.v-middle')
prices = soup.select('span.price')

# 列出 title 和 price 的資料
for link, price in zip(links, prices):
    title = link.get('title')
    price_text = price.text.strip()
    print(f"🏠 {title} ｜ 💰 {price_text}")
