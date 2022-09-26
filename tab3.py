import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def render_tab(df):
    layout = html.Div([html.H1('Kanały', id="placeholder", style={'text-align':'center'}),
            html.Div([html.Div([dcc.Graph(id="scatter-plot")])]),
            html.Div([html.Div([dcc.Graph(id='male-store-type')], style={'width':'50%'}),html.Div([dcc.Graph(id='female-store-type')]
            ,style={'width':'50%'})], style={'display':'flex'}
            )]
            )
    return layout