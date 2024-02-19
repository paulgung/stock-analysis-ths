import requests
from bs4 import BeautifulSoup
import re

# 目标网站的URL
url = 'http://basic.10jqka.com.cn/688311/'

# 模拟浏览器的User-Agent
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

    # 解析股票名
    stock_name = soup.find('h1', string=lambda text: text and text.strip()).get_text(strip=True)
    # 解析股票代码
    stock_code = soup.find('h1', string=lambda text: text and text.strip().isdigit()).get_text(strip=True)
    # 解析市值
    total_market_value_tag = soup.find(string="总市值：")
    if total_market_value_tag:
        total_market_value = total_market_value_tag.find_next(class_="tip f12").text.strip()
    else:
        total_market_value = "没找到总市值"
    # 解析市盈率(静态)
    pe_ratio_static = soup.find(id="jtsyl").text
    # 解析分红率
    dividend_rate = None
    # 解析员工人数
    number_of_employees = None
    # 解析股价
    stock_price = None
    # 解析每股收益
    earnings_per_share_tag = soup.find(string="每股收益：")
    if earnings_per_share_tag:
        earnings_per_share = earnings_per_share_tag.find_next(class_="tip f12").text.strip()
    else:
        earnings_per_share = "没找到每股收益"
    # 解析每股净资产
    net_asset_per_share = soup.find(id="jtsyl").text
    net_asset_per_share_element = soup.find(string="每股净资产：")
    if net_asset_per_share_element:
        net_asset_per_share = net_asset_per_share_element.find_next(class_="tip f12").text.strip()
    else:
        net_asset_per_share = "未找到每股净资产"
    # 解析营业总收入
    total_revenue_element = soup.find('span', class_='hltip f12', string=re.compile(r'营业总收入'))
    if total_revenue_element:
        total_revenue = total_revenue_element.find_next(class_="tip f12").text.strip()
    else:
        total_revenue = "未找到营业总收入"
    # 解析净利润
    net_profit_element = soup.find(string="净利润：")
    if net_profit_element:
        net_profit = net_profit_element.find_next(class_="tip f12").text.strip()
    else:
        net_profit = "没找到净利润"
    # 解析公司亮点
    company_highlight_element = soup.find(string="公司亮点：")
    if company_highlight_element:
        company_highlight = company_highlight_element.find_next(class_="tip f14 fl core-view-text").text.strip()
    else:
        company_highlight = "未找到公司亮点"
    # 解析主营业务
    main_business_element = soup.find('span', class_='hltip f12 fl', string='主营业务：')
    main_business_text = main_business_element.find_next_sibling('span', class_='tip f14 fl main-bussiness-text')
    if main_business_text:
        main_business = main_business_text.get_text(strip=True)
    else:
        main_business = "未找到主营业务"

    # 打印结果
    print(f"{stock_name}")
    print(f"{stock_code}")
    print(f"{total_market_value}")
    print(f"{pe_ratio_static}")
    print(f"{earnings_per_share}")
    print(f"{net_profit}")

else:
    print(f"Error fetching page: HTTP {response.status_code}")