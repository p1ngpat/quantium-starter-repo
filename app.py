import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

#read cleaned data
df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)
#create dash buttons
app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales",
        style={
            "textAlign": "center",
            "color": "#d63384",
            "fontFamily": "Arial",
            "marginBottom": "10px"
        }
    ),

    html.P(
        "Use the region filter to compare Pink Morsel sales before and after the January 15, 2021 price increase.",
        style={
            "textAlign": "center",
            "fontFamily": "Arial",
            "fontSize": "18px",
            "color": "#555"
        }
    ),

    html.Div([
        html.Label(
            "Select Region:",
            style={
                "fontWeight": "bold",
                "marginRight": "15px",
                "fontFamily": "Arial"
            }
        ),

        dcc.RadioItems(
            id="radio-items",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "East", "value": "east"}
            ],
            value="all",
            inline=True,
            style={
                "fontFamily": "Arial",
                "fontSize": "16px"
            },
            inputStyle={
                "marginRight": "6px",
                "marginLeft": "12px"
            }
        )
    ],
        style={
            "textAlign": "center",
            "marginBottom": "25px"
        }
    ),

    html.Div([
        dcc.Graph(id="sales-graph")
    ],
        style={
            "backgroundColor": "white",
            "padding": "20px",
            "borderRadius": "12px",
            "boxShadow": "0 4px 12px rgba(0,0,0,0.15)"
        }
    )
],
    style={
        "backgroundColor": "#f8f9fa",
        "padding": "30px",
        "minHeight": "100vh"
    }
)

#callback
@app.callback(
    Output("sales-graph", "figure"),
    Input("radio-items", "value")
)
def update_graph(selected_region):

    if selected_region != "all":
        filtered_df = df[df["region"].str.lower() == selected_region]
    else:
        filtered_df = df

    daily_sales = filtered_df.groupby("date", as_index=False)["sales"].sum()
    daily_sales = daily_sales.sort_values("date")
#line chart
    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Sales"
        }
    )

    fig.add_vline(x="2021-01-15", line_dash="dash")

    return fig


if __name__ == "__main__":
    app.run(debug=True)