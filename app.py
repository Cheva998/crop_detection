# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from PIL import Image
import base64
import ds4a_models
from gmap_gen import GoogleMapImage
from gmaps_settings import Settings

from pages import (
    overview,
    statistics,
)

folder = 'temp'
image_name = 'temp.png'
im_path = folder +'/'+image_name
settings = Settings()


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

app.config.suppress_callback_exceptions = True
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Function to read and parse the contents of the uploaded image
def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    try:
        with open(im_path, 'wb') as f:
            f.write(decoded)
        
        predicted_value = prediction(im_path)
        if predicted_value == 0:
            msg = 'The image has no coca'
        else:
            msg = 'The image has coca'
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.Hr(),  # horizontal line
        html.H5(msg),
        html.Img(src=contents,
                style={
            'width': '100%',
            'height': 'auto'}),
    ])

# Function to read an image and make a prediction, whether it has coca or not
def prediction(fname):
    predicted_value = ds4a_models.predict_KNN(fname)
    return predicted_value


# Main callback, it updatea all the page contentes and tabs
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/statistics":
        return statistics.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            statistics.create_layout(app)
        )
    else:
        return overview.create_layout(app)

    
# Callback to read the image from the page
@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
def update_output(contents, names):
    if contents is not None:
        children = [
            parse_contents(contents, names)]
        return children

    
# Callback to get the coordinates and display the satelital image
@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('lat', 'value'),
     dash.dependencies.State('lon', 'value')])
def update_output(n_clicks, lat, lon):
    
    if (lat is not None) and (lon is not None):
        gmap_img = GoogleMapImage(lat, lon, 'temp', folder, settings)
        gmap_img.make_image_url()
        gmap_img.save()
        encoded_image = base64.b64encode(open(im_path, 'rb').read())
        predicted_value = prediction(im_path)
        if predicted_value == 0:
            msg = 'The image has no coca'
        else:
            msg = 'The image has coca'
#         children = [parse_contents(encoded_image, 'tmp')]

#         return children
        return html.Div([
                html.Hr(),  # horizontal line
                html.H5(msg),
                html.Img(src= gmap_img.url,#'temp/temp.png',# 'data:image/png;base64,{}'.format(encoded_image),
                        style={
                    'width': '100%',
                    'height': 'auto'}),
                ])
#     else:
#         pass
    

if __name__ == "__main__":
    app.run_server(debug=True)
