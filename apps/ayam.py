# Solution to bar challenge.
# Changed code lines 64 to 71

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
df = pd.read_csv(DATA_PATH.joinpath("datapenjualan.csv"))
df['created_at_x'] = pd.to_datetime(df['created_at_x'], format="%Y-%m-%d %H:%M:%S")

# ------------------------------------------------------------------------------
# App layout
layout = html.Div([

    html.H2("Sales", style={'text-align': 'center', 'color': "white", 'margin-top': "0px", 'padding-top': "25px"}),

    html.Div([
        dcc.Dropdown(id="slct_year",
                     options=[
                         {"label": "2019", "value": 2019},
                         {"label": "2020", "value": 2020},
                         {"label": "2021", "value": 2021},
                         {"label": "2022", "value": 2022}],
                     multi=False,
                     value=2019,
                     style={'width': "30%"})
    ], className='pilihan', style={'margin-left': "30px"}),

    html.Div([
        html.Div([
            html.H3("Total User"),
            html.Div(id='head3', children=[], className='five columns', style={'color': "lightgreen",
                                                                               'font-size': "20px"}),
        ], className='head', style={'padding-top': '40px'}),
        html.Div([
            html.H3("Men"),
            html.Img(src="/assets/icons8-man-96.png", className='image1'),
            html.Div(id='head', children=[], className='five columns', style={'color': "#3885FB", 'font-size': "20px"}),
        ], className='head'),

        html.Div([
            html.H3("Women"),
            html.Img(src="/assets/icons8-woman-96.png", className='image1'),
            html.Div(id='head2', children=[], className='five columns', style={'color': "#DA3176",
                                                                               'font-size': "20px"}),
        ], className='head'),
    ], style={'display': "flex"}),

    html.Div([
        html.Div([
            html.H5("Sales", style={'text-align': 'center', 'color': "white"}),
            html.Div(id='graph1', children=[], className='six columns'),
        ], className='row'),

        html.Div([
            html.H5("Pesanan", style={'text-align': 'center', 'color': "white"}),
            html.Div(id='graph2', children=[], className='six columns'),
        ], className='row'),
        html.Div([
            html.H5("Status", style={'text-align': 'center', 'color': "white"}),
            html.Div(id='graph3', children=[], className='six columns'),
        ], className='row'),
    ], style={'display': "flex"}),

], style={'height': "100%", 'background-color': "black", 'width': "100%"})


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@callback(
    # [Output(component_id='output_container', component_property='children'),
    Output('graph1', 'children'),
    Input('slct_year', 'value')
)
def Ayam(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # container = "The year chosen by user was: {}".format(option_slctd)

    df1 = df.copy()
    df1["yyyy"] = pd.to_datetime(df1['created_at_x']).dt.year
    df1["yyyy"].astype(str)
    df1 = df1[df1["yyyy"] == option_slctd]
    salet = df1.groupby(df1.created_at_x.dt.strftime('%m'))['sale_price'].sum()

    fig = px.area(
        data_frame=df1,
        x=salet.index,
        y=salet,
        template='plotly_dark',
    ).update_layout(
        xaxis_title="Bulan", yaxis_title="Total Penghasilan")

    return dcc.Graph(figure=fig)


@callback(
    # [Output(component_id='output_container1', component_property='children'),
    Output('graph2', 'children'),
    Input('slct_year', 'value')
)
def Bebek(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # container = "The year chosen by user was: {}".format(option_slctd)

    di = df.copy()
    di["yyyy"] = pd.to_datetime(di['created_at_x']).dt.year
    di["yyyy"].astype(str)
    di = di[di["yyyy"] == option_slctd]
    tsx = di['created_at_x'].dt.month.value_counts()
    tik = px.bar(
        data_frame=di,
        x=tsx.index,
        y=tsx,
        template='plotly_dark',
        color=tsx.index,
    ).update_layout(
        xaxis_title="Bulan", yaxis_title="Total Pesanan")

    return dcc.Graph(figure=tik)


@callback(
    # [Output(component_id='output_container1', component_property='children'),
    Output('graph3', 'children'),
    Input('slct_year', 'value')
)
def Pinguin(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # container = "The year chosen by user was: {}".format(option_slctd)

    di = df.copy()
    di["yyyy"] = pd.to_datetime(di['created_at_x']).dt.year
    di["yyyy"].astype(str)
    di = di[di["yyyy"] == option_slctd]
    statust = di['status'].value_counts()
    twt = px.pie(di, values=statust, names=statust.index, template='plotly_dark', color=statust.index,
                 color_discrete_map={'Shipped': 'lightcyan',
                                     'Processing': 'royalblue',
                                     'Complete': 'darkblue'})

    return dcc.Graph(figure=twt)


@callback(
    # [Output(component_id='output_container1', component_property='children'),
    Output('head', 'children'),
    Input('slct_year', 'value')
)
def Itik(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # container = "The year chosen by user was: {}".format(option_slctd)

    di = df.copy()
    di["yyyy"] = pd.to_datetime(di['created_at_x']).dt.year
    di["yyyy"].astype(str)
    di = di[di["yyyy"] == option_slctd]
    yaya = di['department'].value_counts()
    yaya = yaya.sum()
    di = di[di["department"] == "Men"]
    yiyi = di['department'].value_counts()
    yiyi = yiyi.sum()
    yuyu = (yiyi / yaya) * 100
    yuyu.astype(str)
    yuyu = round(yuyu, 1)
    container = "{}%".format(yuyu)

    return container


@callback(
    # [Output(component_id='output_container1', component_property='children'),
    Output('head2', 'children'),
    Input('slct_year', 'value')
)
def Kalkun(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # container = "The year chosen by user was: {}".format(option_slctd)

    di = df.copy()
    di["yyyy"] = pd.to_datetime(di['created_at_x']).dt.year
    di["yyyy"].astype(str)
    di = di[di["yyyy"] == option_slctd]
    yaya = di['department'].value_counts()
    yaya = yaya.sum()
    di = di[di["department"] == "Women"]
    yiyi = di['department'].value_counts()
    yiyi = yiyi.sum()
    yuyu = (yiyi / yaya) * 100
    yuyu.astype(str)
    yuyu = round(yuyu, 1)
    container = "{}%".format(yuyu)

    return container


@callback(
    # [Output(component_id='output_container1', component_property='children'),
    Output('head3', 'children'),
    Input('slct_year', 'value')
)
def Soang(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # container = "The year chosen by user was: {}".format(option_slctd)

    di = df.copy()
    di["yyyy"] = pd.to_datetime(di['created_at_x']).dt.year
    di["yyyy"].astype(str)
    di = di[di["yyyy"] == option_slctd]
    yaya = di['department'].value_counts()
    yaya = yaya.sum()
    container = "{0:,}".format(yaya)

    return container

# ------------------------------------------------------------------------------
# if __name__ == '__main__':
#     app.run_server(debug=True)
