# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
from dash_core_components import Input
import dash_html_components as html
from dash_html_components import Output
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("./dataset/black-friday/BlackFriday.csv")
Stay_In_Current_City_YearsPurchase=pd.read_csv('./dataset/Stay_In_Current_City_YearsPurchase.csv')
GenderPurchase=pd.read_csv('./dataset/GenderPurchase.csv')
AgePurchase=pd.read_csv('./dataset/AgePurchase.csv')


CategoryPurchase=pd.read_csv('./dataset/CategoryPurchase.csv')

CategoryFigure=px.pie(CategoryPurchase,names="Product_Category_1",values="Purchase",color="Product_Category_1")
Stay_In_Current_City_YearsFigure=px.bar(Stay_In_Current_City_YearsPurchase,x='Stay_In_Current_City_Years',y='Purchase',color="City_Category",barmode="group")
GenderFigure=px.bar(GenderPurchase,x='Gender',y='Purchase',color="City_Category",barmode="group")
AgeFigure=px.bar(AgePurchase,x='Age',y='Purchase',color="City_Category",barmode="group")

DropDownFigure=px.bar(AgePurchase,x='Age',y='Purchase',color="City_Category",barmode="group")

BoxFigure=px.box(df,x="Occupation",y="Purchase",color="Occupation")

app.layout = html.Div(children=[

    html.H1(children='        The data visualization of The Black Friday.'),

    html.Div(children='''
        HomeWork 3 by huajiaohuixiang
    '''),

    html.H4(children='         各商品销售情况'),

    dcc.Graph(
        id='pie-graph',
        figure=CategoryFigure
    ),
    


    html.H4(children='         年龄、性别、居住时间的购买额情况'),
    html.Div([
            dcc.Dropdown(
                id='info-col',
                options=[{'label': i, 'value': i} for i in ['Age','Gender','Stay_In_Current_City_Years']],
                value='Age'
            )
    ],
    style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(
        id='DropDown-graph',
        figure=DropDownFigure
    ),
    html.H4(children='         数据离散情况箱型图'),
    dcc.Graph(
        id='box-graph',
        figure=BoxFigure
    ),
])


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






if __name__ == '__main__':    
    app.run_server(debug=True)