import plotly.graph_objects as go
from datetime import datetime, date, timedelta

starting_date = date.fromisoformat("2020-01-01")
xlist = []

ylist = []
y2list = []

for i in range (1000):
    xlist.append(starting_date)
    starting_date += timedelta(days=1)

for j in range(1000):
    ylist.append(j)
    y2list.append(j * 0.75)

fig = go.Figure(

    data=[go.Scatter(x=xlist, y=ylist, line_color="crimson")],
    layout_title_text="Another Graph Object Figure With Magic Underscore Notation"
)

fig.add_trace(go.Scatter(x=xlist, y=y2list))

fig.show()