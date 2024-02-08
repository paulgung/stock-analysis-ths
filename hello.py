import requests
from bs4 import BeautifulSoup

# 目标网站的URL
url = 'http://basic.10jqka.com.cn/688311/'

# 模拟浏览器的User-Agent，这里使用的是Chrome浏览器的示例UA，你可以根据需要替换为其他浏览器的UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 发送带有自定义头部的HTTP GET请求
response = requests.get(url, headers=headers)

# 设置响应内容的编码为GBK，以正确解码来自GBK编码页面的内容
response.encoding = 'GBK'

# 确保请求成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML，此时传入的HTML文本已经是以GBK编码正确解码的字符串
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

    # 解析市盈率(静态)
    pe_ratio_static = soup.find(id="jtsyl").text

    # 解析总市值
    total_revenue_element = soup.find(string="总市值：")
    if total_revenue_element:
        total_revenue = total_revenue_element.find_next(class_="tip f12").text.strip()
    else:
        total_revenue = "未找到"

    # 解析每股未分配利润
    undistributed_profit_per_share_element = soup.find(string=lambda text: text and "每股未分配利润：" in text)
    if undistributed_profit_per_share_element:
        undistributed_profit_per_share = undistributed_profit_per_share_element.find_next(class_="tip f12").text
    else:
        undistributed_profit_per_share = "未找到"

    # 解析总股本
    total_share_capital_element = soup.find(string=lambda text: text and "总股本：" in text)
    if total_share_capital_element:
        total_share_capital = total_share_capital_element.find_next(class_="tip f12").text
    else:
        total_share_capital = "未找到"

    # 打印结果
    print(f"市盈率(静态): {pe_ratio_static}")
    print(f"总市值: {total_revenue}")
    print(f"每股未分配利润（假设为净利润）: {undistributed_profit_per_share}")
    print(f"总股本: {total_share_capital}")

else:
    print(f"Error fetching page: HTTP {response.status_code}")
