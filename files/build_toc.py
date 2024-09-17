import os

def create_html_toc():
    # 获取当前目录下所有的文件名
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # 创建HTML头部
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title> Table of Files</title>
    <style>
        body {font-family: Arial, sans-serif;}
        table {border-collapse: collapse; width: 100%;}
        th, td {border: 1px solid #ddd; padding: 8px; text-align: left;}
        tr:nth-child(even){background-color: #f2f2f2;}
        th {background-color: #4CAF50; color: white;}
    </style>
</head>
<body>
    <h1>Table of Files</h1>
    <table>
        <tr>
            <th>File Name</th>
            <th>Link</th>
        </tr>
    """

    # 遍历文件并构建HTML表格行
    for file_name in files:
        if file_name=='toc.html' or file_name=='build_toc.py':
            continue
        link = f"https://shawkui.github.io/files/{file_name}"
        html_content += f'<tr><td>{file_name}</td><td><a href="{link}">{link}</a></td></tr>\n'

    # 关闭HTML表格和文档
    html_content += """
    </table>
</body>
</html>
"""

    # 写入HTML文件
    with open('toc.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    create_html_toc()