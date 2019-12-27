import dash_core_components as dcc
import dash_html_components as html
#import plotly.graph_objs as go

from utils import Header

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


# df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
# df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Description"),
                                    html.Br([]),
                                    html.P(
                                        """
                                    The application is used for detecting illegal crops in Colombia, the
                                    the first page is used to search or pick an image, the second one 
                                    is for statistics
                                    """,
                                        style={"color": "#fff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4: Enter the data
                    html.Div(
                        [
                                #Column 1: Enter the coordinates
                            html.Div(
                                [
                                    html.H6(
                                        ["Enter coordinates"], className="subtitle padded"
                                    ),
#                                    html.Table(make_dash_table(df_fund_facts)),
                                    dcc.Input(
                                        id="lat", type='number', 
                                        placeholder="Latitude",
                                    ),
                                    dcc.Input(
                                        id="lon", type='number', 
                                        placeholder="Longitude",
                                    ),
                                    html.Button('Submit', id='button'),
                                    html.Div(id='output-container-button'),
                                ],
                                className="six columns",
                            ),
                                #Column 2: Select a file
                            html.Div(
                                [
                                    html.H6(
                                        "Or enter an image",
                                        className="subtitle padded",
                                    ),
                                    dcc.Upload(
                                            id='upload-data',
                                            children=html.Div([
                                                'Drag and Drop or ',
                                                html.A('Select Files'),
                                                
                                            ]),
                                        style={
                                            'width': '100%',
                                            'height': '60px',
                                            'lineHeight': '60px',
                                            'borderWidth': '1px',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '5px',
                                            'textAlign': 'center',
                                            'margin': '10px',
                                            'fontSize': 14
                                            },
                                          ),
                                    html.Div(id='output-data-upload'),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )



