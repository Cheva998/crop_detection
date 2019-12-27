import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_hist_prices = pd.read_csv(DATA_PATH.joinpath("df_hist_prices.csv"))

#layout = dict(
#    autosize=True,
#    automargin=True,
#    margin=dict(l=0, r=0, b=0, t=0),
#    hovermode="closest",
#    plot_bgcolor="#F9F9F9",
#    paper_bgcolor="#F9F9F9",
#    legend=dict(font=dict(size=10), orientation="h"),
#    title="Satellite Overview",
#    mapbox=dict(
##        accesstoken='pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3M' +
#                     'DBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw',
#        style="light",
#        center=dict(lon=.5, lat=-72.54),
#        zoom=12,
#    ),
#)


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Map"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                            id='crop_map',
                                            figure={
                                                'data': [{
#                                                    'lat': 0.5, 'lon': -74.5,
                                                     'type': 'scattermapbox'
                                                }],
                                                'layout': {
                                                    'mapbox': {
                                                        'accesstoken': (
                                                            'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3M' +
                                                            'DBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
                                                        )
#                                                        'center': ('lat'=0.5, 'lon'=-73)
                                                            },
                                                    'margin': {
                                                                'l': 0, 'r': 0, 'b': 0, 't': 0
                                                            },
                                                            }
                                                    }
                                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Percentage of coca by department"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(df_hist_prices)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Percentaje of area with illegal crops", className="subtitle padded"),
                                    
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                   
                  
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
