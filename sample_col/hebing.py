import pandas as pd
import os

# 设置CSV文件所在的目录
csv_dir = 'data'

# 获取所有CSV文件的文件名
csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

# 读取第一个CSV文件并初始化DataFrame
merged_df = pd.read_csv(os.path.join(csv_dir, csv_files[0]))

# 合并剩余的CSV文件
for file in csv_files[1:]:
    df = pd.read_csv(os.path.join(csv_dir, file))
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# 将合并后的DataFrame保存到新的CSV文件
merged_df.to_csv('merged.csv', index=False)