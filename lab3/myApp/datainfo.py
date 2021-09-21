# -*- coding: utf-8 -*-


import pandas as pd;

from matplotlib import pyplot as plt

df=pd.read_csv("./dataset/black-friday/BlackFriday.csv")





#做出不同城市的用户画像
#饼图： 对商品的销量进行统计，对售卖商品进行优化


#做出商品的销量情况
#柱状图：统计年龄段、性别、居住年限的购买金额，并且分城市来看。 并且可以动态选择



#Age 处理
data=pd.DataFrame()
data['Age']=df['Age']
data['Purchase']=df['Purchase']
data['City_Category']=df['City_Category']

temp=data.groupby(['Age','City_Category']).sum()
temp.to_csv('AgePurchase.csv')


#性别处理
data=pd.DataFrame()
data['Gender']=df['Gender']
data['Purchase']=df['Purchase']
data['City_Category']=df['City_Category']

temp=data.groupby(['Gender','City_Category']).sum()
temp.to_csv('GenderPurchase.csv')


#居住年限处理

data=pd.DataFrame()
data['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years']
data['Purchase']=df['Purchase']
data['City_Category']=df['City_Category']

temp=data.groupby(['Stay_In_Current_City_Years','City_Category']).sum()
temp.to_csv('Stay_In_Current_City_YearsPurchase.csv')


#商品类别处理

data=pd.DataFrame()
data['Product_Category_1']=df['Product_Category_1']
data['Purchase']=df['Purchase']
data['User_ID']=df['User_ID']

temp=data.groupby('Product_Category_1').sum()
temp.to_csv('CategoryPurchase.csv')




#商品销量处理

data=pd.DataFrame()
data['Product_ID']=df['Product_ID']
data['Purchase']=df['Purchase']


temp=data.groupby('Product_ID').sum()
temp.to_csv('Product_Purchase.csv')


#职业处理
data=pd.DataFrame()
data['Occupation']=df['Occupation']
data['Purchase']=df['Purchase']


temp=data.groupby('Product_ID').sum()
temp.to_csv('Product_Purchase.csv')