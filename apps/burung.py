from dash import Dash, html, dcc, Output, Input, callback, dash_table
import pandas as pd
# import plotly.express as px  # (version 4.7.0)
# from app import app
import pathlib
import plotly.express as px

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("employees.csv"))

df['Age'] = round(df.Age, 0)
age = df['Age'].value_counts()
service = df['Length_Service']
absent = df['Absent_Hours']
dci = df['distribution_centers_id']

merak = px.scatter(df, x=age.index, y=age, color=age, template='plotly_dark').update_layout(
    xaxis_title="Umur", yaxis_title="Total Pegawai")

camar = px.scatter(df, x=dci, y=service, color=service, template='plotly_dark').update_layout(
    xaxis_title="Id", yaxis_title="Total Service")

murai = px.scatter(df, x=dci, y=absent, color=absent, template='plotly_dark').update_layout(
    xaxis_title="Id", yaxis_title="Total Absent")

layout = html.Div([
    html.H2("Human Resource", style={'text-align': 'center', 'color': "white", 'margin-top': "0px",
                                     'padding-top': "25px"}),
    html.Div([
        html.Div([
            html.H5("Age", style={'text-align': 'center', 'color': "white"}),
            dcc.Graph(
                id='example-graph',
                figure=merak
            )], className='row'),
        html.Div([
            html.H5("Length Service", style={'text-align': 'center', 'color': "white"}),
            dcc.Graph(
                id='example-graph',
                figure=camar
            )], className='row'),
        html.Div([
            html.H5("Absent", style={'text-align': 'center', 'color': "white"}),
            dcc.Graph(
                id='example-graph',
                figure=murai
            )], className='row'),
    ], style={'display': "flex"})

], style={'height': "700px", 'background-color': "black", 'width': "100%"})
