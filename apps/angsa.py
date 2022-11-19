from dash import Dash, html, dcc, Output, Input, callback, dash_table
import pandas as pd
import plotly.express as px  # (version 4.7.0)
# from app import app
import pathlib


# from dash.dependencies import Input, Output

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv(DATA_PATH.joinpath("dproduk.csv"))

di = df.copy()
traffict = di['traffic_source'].value_counts()
twt = px.pie(di, values=traffict, names=traffict.index, template='plotly_dark', hole=.6, color=traffict.index,
             color_discrete_map={'Email': 'cyan',
                                 'Adwords': 'blue',
                                 'Facebook': 'darkblue',
                                 'YouTube': 'red',
                                 'Organic': 'lightcyan'})
tsx = di['browser'].value_counts()
tik = px.bar(
    data_frame=di,
    x=tsx,
    y=tsx.index,
    template='plotly_dark',
    color=tsx.index,
    orientation='h',
    color_discrete_map={'IE': 'cyan',
                        'Safari': 'blue',
                        'Chrome': 'darkblue',
                        'Firefox': 'royalblue',
                        'Other': 'lightcyan'}
).update_layout(
    xaxis_title="Total Browser", yaxis_title="Browser")

tsy = di['status'].value_counts()
tok = px.bar(
    data_frame=di,
    x=tsy,
    y=tsy.index,
    template='plotly_dark',
    color=tsy.index,
    orientation='h',
    color_discrete_map={'Cancelled': 'cyan',
                        'Processing': 'blue',
                        'Shipped': 'darkblue',
                        'Complete': 'royalblue',
                        'Returned': 'lightcyan'}
).update_layout(
    xaxis_title="Total Status", yaxis_title="Status")

layout = html.Div([
    html.H2("Products", style={'text-align': 'center', 'color': "white", 'margin-top': "0px", 'padding-top': "25px"}),
    html.Div([
        html.Div([
            html.H5("Browser", style={'text-align': 'center', 'color': "white"}),
            dcc.Graph(
                id='example-graph',
                figure=tik
            )], className='row'),
        html.Div([
            html.H5("Traffic", style={'text-align': 'center', 'color': "white"}),
            dcc.Graph(
                id='example-graph',
                figure=twt
            )], className='row'),
        html.Div([
            html.H5("Status", style={'text-align': 'center', 'color': "white"}),
            dcc.Graph(
                id='example-graph',
                figure=tok
            )], className='row'),
    ], style={'display': "flex"})

], style={'height': "700px", 'background-color': "black", 'width': "100%"})
