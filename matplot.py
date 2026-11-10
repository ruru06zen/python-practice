import matplotlib.pyplot as plt
'''
不同组别间y：折线 柱状
同一变量（组别）数值内部分布呈现：直方
散点图：相关性可视化
3D散点图：（聚类结果）
气泡图：散点变大
箱线图：看整个一组数据 （识别异常值--看看）
热力图：相关系数矩阵（excel色阶）
雷达图：属性刻画 多组之间跟最好成绩差距
'''
# #########基础绘图--调节中文不乱、解决负号方框######### #
# # 1.准备数据
# # 2.填充数据
# # 3.展示图表
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签，写入字体需要是系统支持的字体(设置无衬线字体备选列表)
# # plt.rcParams['font.family'] = 'SimHei'  # # 【不推荐规范写法】设置全局字体族为SimHei；font.family标准应填sans-serif/serif这类族名，直接填字体名容易失效
plt.rcParams['axes.unicode_minus'] = False  # 解决负号变成方块
# x=[1, 2, 3, 4, 5]
# y=[1, 4, 9, 16, 25]
#
# plt.plot(x,y,linewidth=2)
#
# # 设置图表信息
# plt.title('折线图',fontdict={'family':'SimHei'})
# plt.xlabel('x轴',fontdict={'family':'YouYuan'})
# plt.ylabel('y轴',fontdict={'family':'SimHei'})
#
#
# plt.show()
#
# # 找需要使用的特定字体
# from matplotlib.font_manager import fontManager as fm
#
# for f in fm.ttflist:
#     if f.fname.find('SIMYOU.TTF') != -1:
#         # print(f.name)
#         print(f.name,'=',f.fname)

# # 导入指定外界的字体(假设有一个ali.ttf字体文件在根目录)
# from matplotlib.font_manager import FontProperties
# x=[1,2,3,4,5,6,7]
# y=[17,17,18,15,11,11,13]
# plt.plot(x,y,linewidth=5)
# plt.title('折线图',fontdict={'fontproperties':FontProperties(fname='./ali.ttf')})
# plt.xlabel('x轴',fontdict={'family':'SimHei'})
# plt.ylabel('y轴')

# #########设置风格######### #
from matplotlib import style

def func01():
    style.use('ggplot')  # 设置样式为ggplot
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x=[1,2,3,4,5]
    y=[1,4,9,16,25]
    plt.plot(x,y,linewidth=2)
    #设置标题，加上坐标轴的标签
    plt.title('数字的平方')
    plt.xlabel('值')
    plt.ylabel('值的平方')
    plt.show()

def func00():
    #查看样式
    from matplotlib import style

    print(style.available)  # 查看所有可用的样式

# #########案例1--某周最高和最低温度折线图表案例#########
def train_1():
    # 1.准备数据
    max_temperature = [30, 32, 34, 33, 31, 29, 28] #导入自己需要的最高温度
    min_temperature = [20, 21, 22, 21, 19, 18, 17] #导入自己需要的最低温度
    x=range(7) # 7天
    # 2.填充数据
    plt.plot(x,max_temperature, label='最高温度', color='red', marker='o') # 绘制最高温度折线图
    plt.plot(x,min_temperature,label='最低温度', color='blue', marker='o') # 绘制最低温度折线图

    # 设置标题（中间图片头上 + x，y轴文字说明）
    plt.title('temperature adjustment')
    plt.xlabel('日期') # 设置x轴标签
    xlabels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日'] # 设置x轴刻度标签
    plt.xticks(x, xlabels) # 设置x轴刻度标签
    plt.ylabel('温度：单位℃') # 设置y轴标签'
    # 显示图例
    plt.legend(loc=2, fontsize=10) #可以选择放在图表的左上角2、右上角1、左下角3、右下角4、图表外等位置
    # 3.展示图表
    plt.show()

# #########多图分布--子图创造######### # 常用 plt.subplot()  ply.subplots() Figure.subplots()
def func02_1():
    # 1.准备画布
    plt.figure(figsize=(20,8))#figsize设置画布宽度、高度
    # 2.创建子图
    ax1=plt.subplot(2,2,1) # 2行2列第1个子图
    ax2=plt.subplot(2,2,2) # 2行2列第2个子图
    ax3=plt.subplot(2,2,3) # 2行2列第3个子图
    ax4=plt.subplot(2,2,4) # 2行2列第4个子图
    #找到对象--ax.调用方法
    ax1.plot([1,2,3],[1,4,9],color='red',marker='o') # 绘制第一个子图
    plt.show()

def func02_2():
    fig,ax=plt.subplots(2,2,figsize=(20,8),facecolor='lightskyblue',layout='constrained') # 创建一个画布figure和子图axes
    # 找到对象--ax[][].调用方法
    ax[0][0].plot([1,2,3],[1,4,9],color='red',marker='o') # 绘制第一个子图
    ax[0][0].set_title('子图1') # 给标题要用指定的set_title
    plt.show()

    '''
    fig=plt.figure(figsize=(20,8)) # 创建一个画布figure
    ax=fig.subplots(2,2,facecolor='lightskyblue',layout='constrained') # 创建一个画布figure和子图axes
    # 找到对象--ax[][].调用方法
    '''

def func02_3():
    fig=plt.figure(figsize=(20,8),facecolor='lightskyblue') # 创建一个画布figure
    # ax1=fig.add_subplot(2,2,1) # 2行2
    ax1=plt.subplot(2,2,1) # 2行2列第1个子图
    ax2=plt.subplot(2,2,2) # 2行2列
    ax3=plt.subplot(212) # 2行1列第2个子图
    plt.show()

def func02_4():
    '''
    图形的嵌套 add_subplot()
    '''
    fig=plt.figure(figsize=(20,8)) # 创建一个画布figure
    # 绘制一个大图
    ax1=fig.add_subplot(1,1,1) # 一个大图
    ax1.plot([1,2,3],[1,4,9],color='red',marker='o') # 绘制大图
    # 绘制嵌套的图
    ax2=fig.add_subplot(2,2,1) # 2行2列第1个子图
    ax2.plot([1,2,3],[1,16,25],color='blue',marker='o') # 绘制第一个子图
    ax3=fig.add_subplot(2,2,4) # 2行2列第4个子图
    # 另一种方式绘制嵌套的图
    plt.axes((0.5,0.5,0.4,0.4)) # 绘制一个嵌套的图，参数为(x左边距离,y下边距离,宽度width,高度height)
    #
    plt.show()

# #########图表设计--双轴显示######### #
def func03():
    data1=[-5,1,3,6,8,10,12,13,12,10,8,6,5,3,2,1]
    data2=[-8,-6,-3,1,4,7,9,10,9,7,4,1,-2,-4,-6,-7]
    x=range(0,len(data1))
    fig,ax = plt.subplots()
    ax.plot(x,data1,label='温度')
    # 设置共享x轴
    ax2 = ax.twinx()  # 创建共享x轴的第二个y
    ax2.plot(x,data2,color='red',label='湿度')
    # 显示图例
    fig.legend(loc=2, fontsize=10) #loc可以选择放在图表的位置
    # fig.tight_layout() # 自动调整子图参数，使之填充整个图像区域
    plt.show()


def func04():
    '''
    图表的样式 (color linewith宽度 linestyle样式 alpha透明度 marker标记)
    '''
    import matplotlib.colors as mcolors
    data1=[-5,1,3,6,8,10,12,13,12,10,8,6,5,3,2,1]
    data2=[-8,-6,-3,1,4,7,9,10,9,7,4,1,-2,-4,-6,-7]
    x=range(0,len(data1))
    fig,ax = plt.subplots()
    ax.plot(x,data1,color='g',label='温度',linewidth=5,linestyle='dashed',marker='o',alpha=0.5)#alpha透明度百分比
    # #color linewidth linestyle  marker点上标记 mfc--调整点标记颜色 markersize--调整点标记大小 markeredgecolor--调整点标记|边框颜色| markeredgewidth--调整点标记边框宽度
    ax2 = ax.twinx()  # 创建共享x轴的第二个y
    ax2.plot(x,data2,color='tab:blue',label='湿度',linestyle='dashdot',marker='v')
    fig.legend(loc=2, fontsize=10) #loc可以选择放在图表的位置
    plt.show()

def func05():
    '''
    设置坐标轴--plt.xticks plt.yticks
    '''
    # # 单轴
    # data=[1,3,5,7,9,11,13,15,17,19]
    # x=range(1,11)
    # plt.plot(x,data)
    # # ticks
    # x_ticks=[f'{i}点' for i in range(1,len(data)+1)] #####
    # plt.xticks(x,x_ticks) #填x_tick，用x_ticks填充x
    # y_ticks=range(min(data),max(data)+1) #按照图中的数据进行分布
    # plt.yticks(y_ticks)
    # plt.yticks(y_ticks)
    # plt.show()

    # 双轴
    data1=[-5,1,3,6,8,10,12,13,12,10,8,6,5,3,2,1]
    data2=[-8,-6,-3,1,4,7,9,10,9,7,4,1,-2,-4,-6,-7]
    x=range(0,len(data1))
    fig,ax = plt.subplots()
    ax.plot(x,data1,label='温度')
    ax.set_yticks(range(min(data1),max(data1)+1))
    # 设置共享x轴
    ax2 = ax.twinx()  # 创建共享x轴的第二个y
    ax2.plot(x,data2,color='red',label='湿度')
    ax2.set_yticks(range(min(data2),max(data2)+1))
    # 显示图例
    fig.legend(loc=2, fontsize=10) #loc可以选择放在图表的位置
    # fig.tight_layout() # 自动调整子图参数，使之填充整个图像区域
    plt.show()

def func06():
    '''
    设置网格与标题
    plt.grid
    '''
    data=[-5,1,3,6,8,10,12,13,12,10,8,6,5,3,2,1]
    x=range(1,len(data)+1)

    plt.plot(x,data)
    plt.grid(axis='x',ls='--',lw=1,c='gray',alpha=0.4)# 给纵向线格 ls--linestyle lw-linewidth alpha 透明度
    plt.title('网格线',fontsize=10)# fontsize调字体大小
    plt.suptitle('2030年1月1日的温度',fontsize=20)
    plt.show()

def func07():
    '''
    绘制文本
    plt.text 官方文档看需求使用/看最基本需求来画图
    '''
    data=[-5,1,3,6,8,10,12,13,12,10,8,6,5,3,2,1]
    x=range(1,len(data)+1)
    # plt.plot(x,data)
    # plt.text(2,0,'Hello',fontsize=20,color='r',ha='center',va='center',rotation=0) #ha va水平、竖直对齐方式，rotation转角

    # 以下是想要搞数据标签的一般操作
    plt.plot(x,data,marker='o',linestyle='--')
    for i,j in zip(x,data):
        #print(i,j)
        plt.text(i++0.4,j,j,fontsize=10,color='yellow',ha='center',va='center') #x y 位置 -- 写的内容 -- 字体大小 颜色 水平|垂直对齐方式
    plt.show()

def func08():
    '''
    plt.annotate(文字内容，xy=（ ， ）# 注释点，xytest（ ， ）注释文本位置，arrowprops箭头特征--)
    '''
    data = [-5, 1, 3, 6, 8, 10, 12, 13, 12, 10, 8, 6, 5, 3, 2, 1]
    x=range(1,len(data)+1)

    max_value=max(data)
    max_index=data.index(max_value)+1

    min_value=min(data)
    min_index=data.index(min_value)+1

    plt.plot(x,data,marker='o',ls='--')
    plt.annotate("最大值",(max_index,max_value),(max_index+1,max_value-1),
                 arrowprops={'width':2,"facecolor":'black','headlength':8,'headwidth':6,'shrink':0.2})
    plt.annotate("最小值", (min_index, min_value), (min_index - 1, min_value + 1),
                 arrowprops={'width': 2, "facecolor": 'black', 'headlength': 8, 'headwidth': 6, 'shrink': 0.2})

    # 保存为图片
    plt.savefig('./img/line1')  # 还可以设置dpi大小、.png/.jpg（默认.png）、facecolor=''

    plt.show()

def practice_01():
    '''
    折线图
    '''
    #1.准备数据
    data=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    x=[1,2,3,4,5,6,7]
    max_data=[10,11,13,11,12,12,9]
    min_data=[1,-2,2,5,3,2,0]

    plt.plot(x,max_data,label='最高温度',marker='o',ls='--')
    plt.plot(x,min_data,label='最低温度',marker='*',ls=':')
    plt.xticks(x,data) # 设置刻度
    plt.legend()
    plt.grid(axis='y')
    plt.yticks(range(9,13,2))
    plt.title("折线图")
    plt.show()

def practice_02_1():
    '''
    条形图（柱形图）
    '''
    fruit=['苹果','蓝莓','草莓','橘子']
    counts=[40,100,30,55]
    bar_colors=['tab:red','tab:blue','tab:red','tab:orange']
    labels=['青红色','蓝色','红色','橙色']
    container=plt.bar(fruit,counts,color=bar_colors,label=labels) # 横向加个h变成barh
    plt.bar_label(container)
    plt.legend()
    plt.title('水果颜色区分')
    plt.show()

def practice_02_2():
    '''
    多组条形图（柱形图）--for instance,split the quarter data to show
    '''
    species=("苹果","蓝莓","橘子")
    weight_counts={"第1季度":[70,39,58],"第2季度":[82,37,66]}
    width=0.2
    # 设置x轴[第一组]数据的位置
    x=range(len(species))
    # 设置第二组数据的位置
    x2 = [_+width for _ in x]
    container1=plt.bar(x,weight_counts["第1季度"],label="第1季度",width=width,color='tab:red')
    container2=plt.bar(x2,weight_counts["第2季度"],label="第2季度",width=width,color='tab:blue')
    plt.bar_label(container1)
    plt.bar_label(container2)
    # 计算X轴的刻度的位置
    x_ticks=[_+width/2 for _ in x]
    plt.xticks(x_ticks,species)
    plt.legend()
    plt.show()

def practice_02_3():
    '''
    堆叠条形图（柱形图）--微调上一个多组柱形图就行
    '''
    species=("苹果","蓝莓","橘子")
    weight_counts={"第1季度":[70,39,58],"第2季度":[82,37,66]}
    width=0.2
    container1=plt.bar(species,weight_counts["第1季度"],label="第1季度",width=width,color='tab:red')
    plt.bar_label(container1)

    container2=plt.bar(species,weight_counts["第2季度"],label="第2季度",width=width,color='tab:blue',bottom=weight_counts["第1季度"])
    plt.bar_label(container2)

    # plt.xticks(x_ticks,species)
    plt.legend()
    plt.show()

def practice_03():
    '''
    直方图

    '''
    from random import randint
    data=[randint(1,100) for _ in range(100)]
    plt.hist(data,20,facecolor='tab:orange',edgecolor='white',alpha=0.5,density=False) #density选择显示频率\概率
    plt.show()

def practice_04():
    '''
    箱线图
    tips:晶须超过箱体1.5倍,就认为是异常值
    '''
    from random import randint
    data1=[randint(1,100) for i in range(100) ]
    data2=[randint(1,100) for i in range(100) ]
    data1.append(150)
    data1.append(-50)
    # notch是否开缺口 patch_artist=True可以改颜色
    bp=plt.boxplot([data1,data2],label=['第一组','第二组'],notch=True,patch_artist=True)
    # 修改箱体颜色
    colors = ["#ffaaaa", "#87ceeb"]  # 第一个粉红，第二个浅蓝，你随便改
    for box, c in zip(bp["boxes"], colors):
        box.set(facecolor=c)
        box.set(edgecolor="black")
    plt.show()

def practice_05():
    '''
    散点图

    '''
    import numpy as np
    np.random.seed(42)
    # 身高
    height = np.random.uniform(155, 190, 80)
    # 合理体重：BMI逻辑
    weight = (height / 100) ** 2 * np.random.uniform(18, 24, 80)

    plt.scatter(height,weight,c='tab:blue')
    plt.show()

def practice_06_1():
    '''
    饼图
    '''
    labels='鱼','猫','狗','鹦鹉'
    size=[15,30,45,10]
    plt.pie(size,colors=['tab:red','tab:blue','tab:green','tab:orange'],labels=labels,autopct='%1.1f%%')
    plt.show()

def practice_06_2():
    '''
    空心饼图
    '''
    labels = '鱼', '猫', '狗', '鹦鹉'
    size = [15, 30, 45, 10]
    # 新增这一行：4个值，0=不炸开，大于0向外突出
    explode = [0, 0.05, 0.1, 0]
    plt.pie(size,
            colors=['tab:red', 'tab:blue', 'tab:green', 'tab:orange'],
            labels=labels,
            autopct='%1.1f%%',
            textprops={'color':'yellow','fontsize':15},
            labeldistance=0.5,
            pctdistance=1.2,
            explode=explode)#分离扇形
    plt.show()

def practice_07():
    days = [
        'Saturday', 'Friday', 'Thursday',
        'Wednesday', 'Tuesday', 'Monday', 'Sunday'
    ]
    hours = [
        '12a', '1a', '2a', '3a', '4a', '5a', '6a',
        '7a', '8a', '9a', '10a', '11a',
        '12p', '1p', '2p', '3p', '4p', '5p',
        '6p', '7p', '8p', '9p', '10p', '11p'
    ]
    # 全部改成24个数字！对齐hours
    data = [
        [5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 1, 1, 3, 4, 6, 4, 4, 3, 3, 2, 5, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 2, 6, 9, 11, 6, 7, 7, 8, 12, 5, 5, 7, 2],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1, 9, 8, 10, 6, 5, 5, 5, 7, 4, 2, 4, 0],
        [7, 3, 0, 0, 0, 0, 1, 0, 5, 4, 7, 14, 13, 12, 9, 5, 5, 10, 6, 4, 4, 1, 0, 0],
        [1, 3, 0, 0, 1, 0, 0, 0, 2, 4, 4, 2, 4, 4, 14, 12, 1, 8, 5, 3, 7, 3, 0, 0],
        [2, 1, 0, 3, 0, 0, 0, 2, 0, 4, 1, 5, 10, 5, 7, 11, 6, 0, 5, 3, 4, 2, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 3, 4, 0, 0, 0, 0, 0, 1, 2, 2, 6, 0]
    ]
    # 绘制热力图
    plt.imshow(data) #,cmap=''可以设置颜色类型
    plt.colorbar()# 展现色条
    plt.xticks(range(0,24),hours)
    plt.yticks(range(7),days)
    # 显示数据
    for i,d in enumerate(data): # i是行--y轴
        for j,h in enumerate(d): # j是列
            plt.text(j,i,data[i][j],ha='center',va='center',size=12)
    plt.show()

def practice_08():
    '''
    3d图
    :return:3d
    '''

if __name__ == "__main__":#当模块（作为独立文件/程序入口）时，下面的代码会被执行
    practice_06_1()


