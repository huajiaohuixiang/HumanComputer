描述所选数据集的数据分析任务（目标、数据集的特征等）；
描述设计仪表板的布局，并简要描述图中显示的模式。

###  1.数据分析任务

#### 1.1Target

The dataset here is a sample of the transactions made in a retail store. The store wants to know better the customer purchase behavior against different products. 

#### 1.2Feature

数据只有12个特征，分别是

| Feature                    | Info |
| -------------------------- | ---- |
| User_ID                    |      |
| Product_ID                 |      |
| Age                        |      |
| Occupation                 |      |
| City_Category              |      |
| Stay_In_Current_City_Years |      |
| Marital_Status             |      |
| Product_Category_1         |      |
| Product_Category_2         |      |
| Product_Category_3         |      |
| Purchase                   |      |

其中有用的特征为：

Age、Occupation、City_Category、Stay_In_Current_City_Years、Marital_Status、Product_Category_1、Purchase 

（因为Product_Category_2和Product_Category_3有大量缺失值所以我丢掉了这两个特征）

#### 1.3想要解决的问题

- 不同年龄段的用户购买情况
- 不同职业的用户购买情况
- 不同性别的用户购买情况
- 不同城市的用户购买情况
- 不同居住年限的用户购买情况
- 哪类商品最受欢迎？
- 整体数据的离散程度怎么样？



#### 2.具体实现

#### 2.1数据处理

使用Dash的过程中我发现直接使用dash渲染原数据会很慢，数据1BlackFriday有58w，因此先对数据进行预处理。具体代码在datainfo.py中：

比如商品类别：

```python
#商品类别处理
data=pd.DataFrame()
data['Product_Category_1']=df['Product_Category_1']
data['Purchase']=df['Purchase']
data['User_ID']=df['User_ID']
temp=data.groupby('Product_Category_1').sum()
temp.to_csv('CategoryPurchase.csv')
```

提前通过data.groupby，然后在读取时直接读取生成的新表

```python
CategoryPurchase=pd.read_csv('./dataset/CategoryPurchase.csv')
```

#### 2.2商品类别销售量统计

通过饼图来展示：

```python
CategoryFigure=px.pie(CategoryPurchase,names="Product_Category_1",values="Purchase",color="Product_Category_1")
```

效果如下所示：

![image-20210623152459371](C:\Users\花椒茴香\AppData\Roaming\Typora\typora-user-images\image-20210623152459371.png)

可以清楚的看到每个商品的销售份额占总额的多少。

#### 2.3年龄、性别、居住时间的购买额统计

直接读取处理后的 数据

```java
Stay_In_Current_City_YearsPurchase=pd.read_csv('./dataset/Stay_In_Current_City_YearsPurchase.csv')
GenderPurchase=pd.read_csv('./dataset/GenderPurchase.csv')
AgePurchase=pd.read_csv('./dataset/AgePurchase.csv')

Stay_In_Current_City_YearsFigure=px.bar(Stay_In_Current_City_YearsPurchase,x='Stay_In_Current_City_Years',y='Purchase',color="City_Category",barmode="group")
GenderFigure=px.bar(GenderPurchase,x='Gender',y='Purchase',color="City_Category",barmode="group")
AgeFigure=px.bar(AgePurchase,x='Age',y='Purchase',color="City_Category",barmode="group")

```

效果如下所示：

在左上角可以选择不同的特征进行查看

通过callback函数实现：

```python
@app.callback(
    Output('DropDown-graph', 'figure'),
    Input('info-col', 'value')
    )
def update_graph(info_col):
    if info_col=='Age':
        DropDownFigure=AgeFigure
    elif info_col=='Gender':
        DropDownFigure=GenderFigure
    else:
        DropDownFigure=Stay_In_Current_City_YearsFigure
    return DropDownFigure
```

![image-20210623152931426](C:\Users\花椒茴香\AppData\Roaming\Typora\typora-user-images\image-20210623152931426.png)

#### 2.4数据离散情况箱型图：

箱型图可以以一种相对稳定的方式描述数据的离散分布情况，通过对职业特征箱型图购买力的刻画，发现我们数据的离散情况基本相同。（可以看到每个职业的购买力平均值、最大值、最小值、75%、25%值）

![image-20210623153632894](C:\Users\花椒茴香\AppData\Roaming\Typora\typora-user-images\image-20210623153632894.png)

