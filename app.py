import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read cleaned data
df = pd.read_csv("output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Group by date and sum sales
daily_sales = df.groupby("date", as_index=False)["sales"].sum()

# Sort by date
daily_sales = daily_sales.sort_values("date")

# Create line chart
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

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)