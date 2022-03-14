import pandas as pd

# 创建一个DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4],
                     'B': [5, 6, 7, 8],
                        'C': [9, 10, 11, 12]})
print(df)
print('-' * 30)

# 创建一个含有空值的DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4],
                        'B': [5, 6, 7, 8],  
                        'C': [9, 10, 11, None]})
# 填充空值
df.fillna(value=0, inplace=True)
print(df)
# 使用均值填充空值
df.fillna(method='ffill', inplace=True)
print(df)
print('-' * 30)
