import pandas as pd


# 读取CSV文件
#csv_file = 'data/data_2024_06_18.csv'
csv_file = 'merged.csv'
df = pd.read_csv(csv_file)

df = df[df['behavior'] != '获取用户信息']
df = df[df['behavior'] != '页面查询']
# 将日期列转换为datetime类型
df['createTime'] = pd.to_datetime(df['createTime'])
#df['createTime'] = df['createTime'].strftime('%Y-%m-%d %H:%M:%S.%f') + "\t"

# 按日期排序
df_sorted = df.sort_values(by='createTime')

# 指定列的顺序
columns_order = ['userId', 'behavior', 'url', 'ip', 'userAgent', 'createTime', 'requestTime']

# 选择需要的列，并且按照指定的顺序排列
df = df_sorted[columns_order]

# 假设我们要添加的列名为'case'，并且我们想将其添加到第一列
# 我们可以使用列的赋值操作来添加新列
# 这里我们给'case'列赋值为1，你可以根据需要修改这个值
df['case'] = ''

# 将'case'列移动到DataFrame的第一列
df = df[['case'] + [col for col in df.columns if col != 'case']]

#定义函数，修改login为登录
def modify_value(row):
    row['behavior'] = '登录邮箱'
    return row

#定义函数，修改logout为退出登录
def modify_value1(row):
    row['behavior'] = '退出登录'
    return row

#选择url中值为：http://192.168.3.111:6080/login.php的行
selected_rows = df.loc[df['url'] == 'http://192.168.3.111:6080/login.php']

#应用修改函数到选择的行
df.loc[df['url'] == 'http://192.168.3.111:6080/login.php', 'behavior'] = selected_rows.apply(modify_value, axis=1)


#定义要匹配的特定前缀
specific_prefix = 'http://192.168.3.111:6080/logout.php'
#选择url中特定前缀的值为：http://192.168.3.111:6080/logout.php的行
selected_rows1 = df.loc[df['url'].str.startswith(specific_prefix)]

#应用修改函数到选择的行
df.loc[df['url'].str.startswith(specific_prefix), 'behavior'] = selected_rows1.apply(modify_value1, axis=1)

#删除行为为'未定义行为-缓存中未匹配到行为'的行
df = df[df['behavior'] != '未定义行为-缓存中未匹配到行为']



# 假设我们要根据'column_name'列中的字符串匹配来选择行
column_name = 'behavior'
start_string = '登录邮箱'
end_string = '退出登录'

# 初始化一个计数器，用于分组和编号
group_counter = 1

#定义一个bool变量
bool_v = False

# 遍历DataFrame中的每一行
for index, row in df.iterrows():
    # 检查第三列的值是否在指定的范围内

    if row['behavior'] == start_string:
        bool_v = True

    if bool_v:
        # 根据规则更改第一列的值
        df.at[index, 'case'] = f'case{group_counter:05d}'
        if row['behavior'] == end_string:
            bool_v = False
            # 更新计数器，准备下一组编号
            group_counter += 1

# 保存排序后的CSV文件
df.to_csv('sorted_2024_06_25.csv', index=False)