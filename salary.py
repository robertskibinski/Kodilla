import plotly.graph_objects as go

names = ["Mark", "John","Daniel","Greg"]
salary_values = [1000,1500,2300,5000]
layout = {'title': 'Salary'}
fig = go.Figure(go.Bar(x=names, y=salary_values))
fig.show()