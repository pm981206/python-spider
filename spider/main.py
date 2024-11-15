import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# 发送 HTTP 请求获取网页内容
url = 'https://blog.panmin.me/'  # 替换为目标网页 URL
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    print("成功获取网页内容!")
    html_content = response.text
else:
    print(f"请求失败，状态码：{response.status_code}")
    exit()

# 解析 HTML 内容
soup = BeautifulSoup(html_content, 'html.parser')

# 可选：提取网页的标题
page_title = soup.title.string if soup.title else 'Untitled'

# 将 HTML 转换为 Markdown
markdown_content = md(html_content)

# 创建或写入 .md 文件
md_filename = f"{page_title}.md".replace(" ", "_")  # 文件名不能包含空格
with open(md_filename, 'w', encoding='utf-8') as md_file:
    md_file.write(markdown_content)

print(f"网页内容已保存为 {md_filename}")
