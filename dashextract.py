import sqlite3
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from pymongo import MongoClient

cluster = "mongodb://localhost:27017"

# To begin accessing database. place cluster link inside MOngoClient parenthesis 
client = MongoClient(cluster)
db = client.test
collection = db.board
#Looking at documents within collection
data1 = collection.find()




small_card = {
         'background-color': '#426793',
         'width': '100%',
         'height':'20%'}

big_card = dbc.CardBody(style={
         'background-color': '#426793',
        'width': '75%',
        'height':'100%',
        'display': 'inline-block'
})



footer =  dbc.CardBody(style={
        'background-color': '#426793',
        'height':'100%',
        'width':'50%'
    })


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    html.Br(),
    dbc.Row([
        html.Div(
            html.H3('Morgan State University 2022 REU'),
            style = {
                'text-align': 'center'
            }
        ),
        html.Div(
            html.H4('FLOOD DETECTION DASHBOARD'),
            style = {
                'text-align': 'center'
            }
        )
    ]),
    html.Br(),
    html.Div([html.Br(),
            html.Div([
                dbc.CardBody([html.H5('AVG. WATER VOLUME:'),
                              html.H5(id = 'water_level')],style=small_card),
                dbc.CardBody([html.H5('LOCATION:'),
                              html.H5(id = 'location',children="ELLICOT CITY")],style=small_card),
                dbc.CardBody([html.H5('TIME:'),
                              html.H5(id = 'Time',children="20:21:03")],style=small_card),
                dbc.CardBody([html.H5('DATA:'),
                              html.H5('06/29/2022')],style=small_card)
                    ], style={
                        'background-color': 'black',
                        'width': '22%',
                        'height':'100%',
                        'display':'flex',
                        'flex-direction':'column',
                        'justify-content':'space-between',
                        'padding':'0.5rem',
                        'gap': '0.5rem'
                        
                    }),
            dbc.CardBody([
                dcc.Graph(id = 'live-graph', animate=True,
                style={
                        # 'background-color': '#426793',
                        'width': '96.5%',
                        'height':'100%'
                    }),
                dcc.Interval(
                id='interval-component',
                interval=1*2000, # in milliseconds
                n_intervals=0)],
                        style={
                        'background-color': 'black',
                        'width': '75%',
                        'height':'100%'
            })
            
            
            ], style={
        'background-color': 'yellow',
        'width': '100%',
        'height':'33rem',
        'display':'flex',
        'align-items':'center'
    }),
    html.Footer([footer, footer],style={
        'background-color': 'black',
        'width': '100%',
        'height':'11rem',
        'display':'flex',
        'flex-direction':'rows',
        'gap':'0.5rem',
        'padding':'0.5rem'
        
    })
], style={
    'background_color': 'black'
})

# Multiple components can update everytime interval gets fired. arguments in Output is id of what you want to update
#and the name of the acutual graph you will update
@app.callback([Output('live-graph', 'figure'), 
               Output('water_level', 'children')], 
             [Input('interval-component', 'n_intervals')]) #first argument tells callback function what id the value causing changes has. 
#second tells callback value, which expains amount of time that should pass before update begins
def update_graph(n):
    
    data1 = collection.find()    
    
    #df should be holding pathway to created mongoDB database
    df = pd.DataFrame(list(data1))

    fig = px.line(df.tail(4000), x="frame_number", y="water_pixels")
    dflast = df.iloc[-1]
    return (fig, dflast[2])

if __name__ == '__main__':
    app.run_server(debug=True)