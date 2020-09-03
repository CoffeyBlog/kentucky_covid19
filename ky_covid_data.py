import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

df = pd.read_csv('daily.csv')

# create infection rate
# total infected / total tested = _____%


# csv data
fig_inc = go.Figure(go.Line(x=df['date'], y=df['positive'], name='Infected', mode='lines+markers',
                            marker=dict(size=10, color='indianred')))

fig_inc.add_trace(go.Line(x=df['date'], y=df['recovered'], name='Recovered', mode='lines+markers',
                            marker=dict(size=10, color='lightseagreen')))

fig_inc.add_trace(go.Line(x=df['date'], y=df['death'], name='Deaths', mode='lines+markers',
                            marker=dict(size=10, color='gray')))

fig_inc.add_trace(go.Line(x=df['date'], y=df['positiveIncrease'], name='Daily', mode='lines+markers',
                            marker=dict(size=10, color='orange')))

#fig_inc.add_trace(go.Line(x=df['date'], y=df['totalTestResults'], name='Total Tested', mode='lines+markers',
#                            marker=dict(size=10, color='Purple')))



# layout
fig_inc.update_layout(xaxis_showgrid=True, yaxis_showgrid=True, plot_bgcolor='whitesmoke',
                      title={
                          'text': 'Kentucky COVID-19 Cases',
                          'y': 0.75,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top'}, xaxis_type='category')
fig_inc.update_xaxes(title='------>Timeline', showline=False)
fig_inc.update_yaxes(title='------>Number of incremental cases', showline=False)

fig_inc.show()
