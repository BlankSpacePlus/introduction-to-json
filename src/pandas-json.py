import pandas as pd

# 创建一个URL
url = 'test.json'
# 加载数据
dataframe = pd.read_json(url, orient='columns')
# 查看前两行数据
print(dataframe.head(2))
