import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from flask import Flask, render_template

# 1. Initialize the Flask server
server = Flask(__name__)

# A simple Flask route for the home page.
@server.route('/')
def home():
    return '<h1>Welcome to the Flask App!</h1><p>Navigate to /dash_app to see the dashboard.</p>'

# 2. Create the Dash application and pass the Flask server to it
# The url_base_pathname specifies the route where the Dash app will be served.
dash_app = dash.Dash(__name__, server=server, url_base_pathname='/dash_app/')

# 3. Create sample data and a Plotly figure for the Dash app
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# 4. Define the layout of the Dash app
dash_app.layout = html.Div([
    html.H1(children='Dash Dashboard within a Flask App'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# 5. Run the Flask server if the script is executed directly
if __name__ == '__main__':
    server.run(debug=True, port=8050)
