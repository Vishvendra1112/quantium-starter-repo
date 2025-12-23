# Run this app with `python app.py`
# Visit http://127.0.0.1:8050/ in your browser

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Create Dash app
app = Dash(__name__)

# Load formatted sales data
df = pd.read_csv("formatted_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Before and After Price Increase",
    labels={
        "date": "Date",
        "sales": "Total Sales ($)"
    }
)

# App layout
app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods Sales Visualiser",
            style={"textAlign": "center"}
        ),

        html.P(
            "This chart shows Pink Morsel sales over time. "
            "The price increase occurred on 15 January 2021.",
            style={"textAlign": "center"}
        ),

        dcc.Graph(
            id="sales-line-chart",
            figure=fig
        )
    ]
)

# Run server (Dash v2.14+)
if __name__ == "__main__":
    app.run(debug=True)
