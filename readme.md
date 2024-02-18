## 股票数据爬虫
该程序用于从特定网站上爬取股票数据，并将数据保存到 Excel 文件中。

#### 使用说明

安装 Python 3.x 环境。

安装所需的 Python 库：

```
pip install requests
pip install xlrd
pip install beautifulsoup4
pip install openpyxl
```

执行 main.py 文件来运行程序。

#### 文件结构

```
main.py：主程序文件，包含了爬虫逻辑和数据处理。
stock_data 文件夹：存储股票列表的 Excel 文件。
README.md：本文件，提供了关于程序的说明和使用方法。
```

#### 主要功能

从指定网站爬取股票数据。
解析 HTML 数据，并提取股票相关信息。
将股票数据保存到 Excel 文件中。

#### 注意事项

该程序依赖于第三方网站的数据格式，如果网站结构发生变化，程序可能会失效。
爬取过程中可能会出现网络错误或网站响应慢的情况，程序会捕获并输出错误信息。
请确保在合适的网络环境下运行程序，以确保数据的准确性和完整性。
