import dash
import dices
import plotly
import plotly.graph_objs as go
from pandas.core.interchange import column
from plotly import colors
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.io as pio
from dash import html
from dash import dcc

import numpy as np
import pandas as pd

df = pd.read_csv('Data/authors_rate.csv')
df2 = pd.read_csv('Data/countries_rate.csv')
df3 = pd.read_csv('Data/funding_rate.csv')
df4 = pd.read_csv('Data/organizations_rate.csv')
df5 = pd.read_csv('Data/publications_dinamic.csv')
df6 = pd.read_csv('Data/sources_rate.csv')


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children='SCOPUS AI DASHBOARD'),

        html.Div(children='''
            Artificial Intelligence
        '''),

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df['Title'],
                        "y": df['Count'],
                        "type": "bar"
                    }
                ],
                "layout": {"title": "Authors Rate"},
            },
        ),

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df2['Title'],
                        "y": df2['Count'],
                        "type": "bar"
                    }
                ],
                "layout": {"title": "Countries Rate"},
            },
        ),

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df3['Title'],
                        "y": df3['Count'],
                        "type": "bar"
                    }
                ],
                "layout": {"title": "Funding Rate"},
            },
        ),

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df4['Title'],
                        "y": df4['Count'],
                        "type": "bar"
                    }
                ],
                "layout": {"title": "Organizations Rate"},
            },
        ),

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df6['Title'],
                        "y": df6['Count'],
                        "type": "bar"
                    }
                ],
                "layout": {"title": "Sources Rate"},
            },
        ),


        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df5['Title'],
                        "y": df5['Count'],
                        "type": "lines"
                    }
                ],
                "layout": {"title": "Publications dinamic"},
            },
        )

])

if __name__ == '__main__':
    app.run_server(debug=True)