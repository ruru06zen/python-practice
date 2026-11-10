# # 统计
# import openpyxl
# wb =openpyxl.load_workbook(r'D:\BaiduNetdiskDownload\coderesource\2024_第二次模拟训练题\code\代码\excel 自动化\auto_code_excel\base_data\data01.xlsx')
# print(wb.sheetnames) #获取名称
#
# data=wb["Sheet1"]
# # 获取单个值
# # value1=data.cell(row=2,column=3).value
# # # value2=data.cell['C3'].value
# # print(value1)
#
# # 获取多个行列值
# # cells=data['c1':'c14']
# # for row in cells:
# #     for cell in row:
# #         print(cell.value)
# # cell_rows_6_10 =data[6:10]
# # print(cell_rows_6_10)
# # for row in cell_rows_6_10:
# #     for cell in row:
# #         print(cell.value)
#
# # # 按行找列（行遍历）/按列找行（列遍历） 提取
# # for rows in data.rows:
# #     for cell in data.rows:
# #         print(cell)
# # for columns in data.columns:
# #     for cell in data.columns:
# #         print(cell)
#
# # 获取 行列数
# # print(data.max_row)
# # print(data.max_column)
#
# import numpy as np
#
# x=np.arange(1,13)
# a=x.reshape(4,3)
# print(a)
# print(a[1])
# print(a[-1]) #获取最后一行
#
# print(a[1,1])
# print(a[1:3,1:3])
# print(a[0,1::2])
# print(a[(0,0),(0,2)])
#
# print(a[::-1]) #行倒序
# print(a[::-1,::-1]) #行列倒序
#
# # 多维数组变成一维数组 压平flatten() ravel()
# a=np.arange(24)
# b=a.reshape(2,4,3)
# c=a.reshape(3,8)
# a1=c.flatten()
# a2=b.ravel()
# a1[0]=100
# print(b) #修改a1 b相应位置元素值变
# a2[0]=100
# print(c) #修改a2 c相应位置元素值不变
#
# # 二维数组的拼接
# a=np.arange(1,7).reshape(2,3)
# b=np.array([['a','b','c'],['d','e','f']])
# print(np.hstack([a,b])) #横向拼接--水平
# print(np.vstack([a,b])) #纵向拼接--垂直
#
# # 转置
# a=np.arange(1,7).reshape(2,3)
# print(a.T)
#
# # 数组分隔
# x=np.arange(1,9)
# a=np.split(x,4)
# print(a)
#
# b=np.split(x,[3,5])
# print(b)
#
# grid=np.arange(16).reshape(4,4)
# np.hsplit(grid,2)  # 横向分隔
# np.vsplit(grid,2) # 纵向分隔
#
# x=np.arange(1,5)
# y=np.empty_like(x)
# np.power(x,2,out=y)
#
# a=np.array([4,2,1,3])
# np.sort(a)
# np.median(a)
# t=np.arange(1,11).reshape(2,5)
#
#
# # 多维数组不传递指令 默认对所有元素求均值
# np.mean(t)
# np.mean(t,axis=0) # 求列（在0轴即垂直）求均值
# np.mean(t,axis=1) # 求行（在1轴即水平）求均值
#
# d=np.array([21,18,12,11,6])
# np.unique(d) #去重 /排序
#
# e=np.array([12,18,0])
# np.nonzero(e) #获取非零元素索引
#
# np.argmax(e) #获取最大值索引
# np.argmin(e) #获取最小值索引
import pandas as  pd
import matplotlib.pyplot as plt
#解决中文乱码
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# data=pd.read_csv(r'D:\BaiduNetdiskDownload\coding\vscode\python\源码\itbaizhan\car\1_二手车价格预测\data.csv')
# # 数量前十的品牌
# amount_top=data['brand'].value_counts().sort_values(ascending=False).head(10)
# # 品牌销量与销售占比占比
# amount_top.plot(kind='pie', figsize=(10, 6), color='skyblue')
# plt.show()

# home = pd.read_excel(r"D:\BaiduNetdiskDownload\coding\vscode\python\源码\itbaizhan\pre machine\home_income.xlsx")  # 读取excel文件
# # plt.figure(figsize=(10, 6))
# home.plot.scatter("s3","index1")
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df1=pd.read_excel(r'D:\BaiduNetdiskDownload\coding\vscode\python\源码\itbaizhan\mathematic model\2023\C题\附件1.xlsx')
df2=pd.read_excel(r'D:\BaiduNetdiskDownload\coding\vscode\python\源码\itbaizhan\mathematic model\2023\C题\附件2.xlsx')
df3=pd.read_excel(r'D:\BaiduNetdiskDownload\coding\vscode\python\源码\itbaizhan\mathematic model\2023\C题\附件3.xlsx')
df4=pd.read_excel(r'D:\BaiduNetdiskDownload\coding\vscode\python\源码\itbaizhan\mathematic model\2023\C题\附件4.xlsx')

data_01=pd.merge(df1,df2,on='单品编码',how='left')

data_g=data_01.groupby('分类名称')
tu_1=data_g['销量(千克)'].sum().sort_values(ascending=False)

total = tu_1.sum()  # 计算所有类别的总销量
percentages = (tu_1/ total) * 100  # 每个类别占比（保留原始精度，绘图时再格式化）

data_01.drop(columns=['单品名称','分类编码'])

# 确保销售日期列的格式正确
data_01['销售日期'] = pd.to_datetime(data_01['销售日期'])

# 添加各种时间维度
data_01['年'] = data_01['销售日期'].dt.year
data_01['月'] = data_01['销售日期'].dt.month
data_01['日'] = data_01['销售日期'].dt.day

# 创建用于分析的时间格式
data_01['年月'] = data_01['销售日期'].dt.strftime('%Y-%m')
data_01['年月日'] = data_01['销售日期'].dt.strftime('%Y-%m-%d')
data_01['月周期'] = data_01['销售日期'].dt.to_period('M')  # 用于绘图
data_01['星期'] = data_01['销售日期'].dt.weekday  # 0=周一, 6=周日

pivot_corr = data_01.pivot_table(
    index='销售日期',
    columns='分类名称',
    values='销量(千克)',
    aggfunc='sum',
    fill_value=0
)
print(pivot_corr)

correlation_matrix = pivot_corr.corr()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from surprise import Reader, Dataset, KNNBasic
from surprise.model_selection import train_test_split

# ---------------------- 1. 数据准备 ----------------------
# 定义Reader（指定销量范围为非负）
reader = Reader(rating_scale=(0, float('inf')))

# 准备数据（使用data_01中的关键列）
data = Dataset.load_from_df(
    data_01[['年月', '分类名称', '销量(千克)']],  # 统一使用data_01作为数据源
    reader
)

# 划分训练集和测试集
trainset, testset = train_test_split(data, test_size=0.2)

# ---------------------- 2. 模型训练（仅训练一次） ----------------------
# 定义基于物品的协同过滤模型（余弦相似度）
sim_options = {'name': 'cosine', 'user_based': False}
algo = KNNBasic(sim_options=sim_options)
algo.fit(trainset)  # 单次训练，供后续所有分析使用

# ---------------------- 3. 预测与关联类别分析 ----------------------
# 预测测试集销量
predictions = algo.test(testset)

# 定义函数：获取与目标类别最相关的n个类别
def get_top_n_related_items(algo, item_id, n=5):
    inner_id = algo.trainset.to_inner_iid(item_id)
    similarities = algo.sim[inner_id]
    related_indices = similarities.argsort()[::-1][1:n+1]  # 排除自身
    return [algo.trainset.to_raw_iid(i) for i in related_indices]

# 示例：获取与'水生根茎类'最相关的5个类别
top_related = get_top_n_related_items(algo, '水生根茎类', 5)
print("与 '水生根茎类' 最相关的 5 个蔬菜类别:", top_related)

# ---------------------- 4. 提取类别相似度矩阵（复用训练好的模型） ----------------------
# 获取所有蔬菜类别（原始名称）
all_items = trainset.all_items()
raw_item_ids = [trainset.to_raw_iid(iid) for iid in all_items]

# 构建相似度矩阵（行和列均为类别名称）
sim_matrix = pd.DataFrame(
    algo.sim,  # 直接使用训练好的模型中的相似度矩阵
    index=raw_item_ids,
    columns=raw_item_ids
)

# 可在此处添加基于sim_matrix的可视化或进一步分析
# 例如：打印相似度矩阵前5行
print("\n类别相似度矩阵（前5行）:\n", sim_matrix.head())


def plot_top_related(item_id, n=5):
    """绘制与目标类别最相关的n个类别的条形图"""
    # 获取目标类别的内部ID
    inner_id = trainset.to_inner_iid(item_id)
    # 获取与目标类别的相似度（排除自身）
    similarities = algo.sim[inner_id]
    # 按相似度排序，取前n个
    related_indices = similarities.argsort()[::-1][1:n + 1]  # [1:]排除自身
    related_items = [trainset.to_raw_iid(i) for i in related_indices]
    related_scores = [similarities[i] for i in related_indices]

    # 绘制条形图
    plt.figure(figsize=(8, 5), dpi=100)
    sns.barplot(x=related_scores, y=related_items, palette="Reds_d")
    plt.xlabel("相似度分数（余弦相似度）", fontsize=12)
    plt.ylabel("蔬菜类别", fontsize=12)
    plt.title(f"与'{item_id}'最相关的{len(related_items)}个蔬菜类别", fontsize=14, pad=10)
    # 在条形上标注相似度分数
    for i, score in enumerate(related_scores):
        plt.text(score + 0.01, i, f"{score:.2f}", va="center")
    plt.tight_layout()
    plt.show()


# 示例：绘制与“水生根茎类”最相关的5个类别
plot_top_related("水生根茎类", n=5)


def plot_relation_network(min_similarity=0.5):
    """绘制类别关系网络（仅展示相似度≥min_similarity的关联）"""
    G = nx.Graph()  # 创建无向图

    # 添加节点（所有蔬菜类别）
    G.add_nodes_from(raw_item_ids)

    # 添加边（相似度≥阈值的类别对）
    for i, item1 in enumerate(raw_item_ids):
        for j, item2 in enumerate(raw_item_ids):
            if i < j:  # 避免重复添加边
                sim = sim_matrix.loc[item1, item2]
                if sim >= min_similarity:
                    G.add_edge(item1, item2, weight=sim)  # 边的权重为相似度

    # 设置节点位置（布局）
    pos = nx.spring_layout(G, k=0.5, seed=42)  # 弹簧布局，k控制节点间距

    # 绘制网络
    plt.figure(figsize=(12, 10), dpi=100)
    # 绘制节点
    nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="lightblue")
    # 绘制边（根据权重调整粗细）
    edges = G.edges()
    weights = [G[u][v]['weight'] * 5 for u, v in edges]  # 放大权重用于可视化
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=weights, edge_color="gray")
    # 绘制节点标签（类别名称）
    nx.draw_networkx_labels(G, pos, font_size=12, font_family=['KaiTi', 'SimHei'])
    # 添加边标签（相似度）
    edge_labels = {(u, v): f"{G[u][v]['weight']:.2f}" for u, v in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title(f"蔬菜类别关联网络图（相似度≥{min_similarity}）", fontsize=16, pad=20)
    plt.axis("off")  # 关闭坐标轴
    plt.tight_layout()
    plt.show()


# 示例：绘制相似度≥0.5的类别关系网络（可根据实际数据调整阈值）
plot_relation_network(min_similarity=0.5)