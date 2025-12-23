from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Create app
app = Dash(__name__)

# Load data
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# ---------- Styling ----------
PAGE_STYLE = {
    "backgroundColor": "#0f172a",
    "minHeight": "100vh",
    "padding": "30px",
    "fontFamily": "Arial"
}

CARD_STYLE = {
    "backgroundColor": "#1e293b",
    "padding": "20px",
    "borderRadius": "12px",
    "marginBottom": "20px"
}

TEXT_STYLE = {
    "color": "#e5e7eb",
    "textAlign": "center"
}

# ---------- Layout ----------
app.layout = html.Div(
    style=PAGE_STYLE,
    children=[

        # Header
        html.Div(
            style=CARD_STYLE,
            children=[
                html.H1(
                    "Soul Foods – Pink Morsel Sales Dashboard",
                    style={**TEXT_STYLE, "fontSize": "36px"}
                ),
                html.P(
                    "Analyse sales trends before and after the 15 January 2021 price increase.",
                    style={**TEXT_STYLE, "fontSize": "16px"}
                )
            ]
        ),

        # Radio buttons
        html.Div(
            style=CARD_STYLE,
            children=[
                html.H3(
                    "Filter Sales by Region",
                    style={**TEXT_STYLE, "marginBottom": "10px"}
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": " All Regions", "value": "all"},
                        {"label": " North", "value": "north"},
                        {"label": " East", "value": "east"},
                        {"label": " South", "value": "south"},
                        {"label": " West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={
                        "textAlign": "center",
                        "color": "#cbd5f5",
                        "fontSize": "16px"
                    }
                )
            ]
        ),

        # Graph
        html.Div(
            style=CARD_STYLE,
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# ---------- Callback ----------
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Total Sales ($)"
        }
    )

    fig.update_layout(
        plot_bgcolor="#1e293b",
        paper_bgcolor="#1e293b",
        font_color="#e5e7eb",
        title_x=0.5
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)
