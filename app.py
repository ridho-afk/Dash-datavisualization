import dash
from dash import Dash, html, dcc, Output, Input, callback
# Connect to your app pages
from apps import ayam, bebek, home, angsa, burung

# Connect to main app.py file
# from app import app
# from app import server

# meta_tags are required for the app layout to be mobile responsive
app = Dash(__name__, suppress_callback_exceptions=True,
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0'}]
           )
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H1("Looker", style={'text-align': 'left', 'color': "white", 'margin': "0px",
                                 'background-color': '#111111', 'padding': '12px', 'padding-left': '20px',
                                 'font-family': "Cursive"}),
        html.Div([
            dcc.Link('Home', href='/apps/home', style={'padding-right': "20px", 'color': "white",
                                                       'font-family': "Cursive"}),
            dcc.Link('Sales', href='/apps/ayam', style={'padding-right': "20px", 'color': "white",
                                                        'font-family': "Cursive"}),
            dcc.Link('Marketing', href='/apps/bebek', style={'padding-right': "20px", 'color': "white",
                                                             'font-family': "Cursive"}),
            dcc.Link('Products', href='/apps/angsa', style={'padding-right': "20px", 'color': "white",
                                                            'font-family': "Cursive"}),
            dcc.Link('HR', href='/apps/burung', style={'padding-right': "20px", 'color': "white",
                                                       'font-family': "Cursive"}),
        ], className="nav"),
    ], style={'display': "flex", 'width': "100%"}),
    html.Div(id='page-content', children=[])
], style={'background-color': "#111111", 'width': "100%"})


@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/ayam':
        return ayam.layout
    if pathname == '/apps/bebek':
        return bebek.layout
    if pathname == '/apps/angsa':
        return angsa.layout
    if pathname == '/apps/burung':
        return burung.layout
    if pathname == '/apps/home':
        return home.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=False)
