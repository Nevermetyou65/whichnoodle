#ราคา 
import plotly.graph_objects as go
import pandas as pd

noodle_df = pd.read_csv('noodle.csv', index_col=0)


fig = go.Figure()


fig.add_traces(
    go.Scatter(
        x=[1],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[2],
            size=noodle_df.โซเดียม.iloc[2]/10,
            opacity=0.9,
            line=dict(width=1.5, color='black')),
        name=noodle_df.index[2],
        hovertext=f'{noodle_df.index[2]} มีโซเดียม {noodle_df.โซเดียม.iloc[2]} มิลลิกรัม',
        hoverinfo='text'
        
    )
)

fig.add_traces(
    go.Scatter(
        x=[2],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[1],
            size=noodle_df.โซเดียม.iloc[1]/10,
            opacity=0.9,
            line=dict(width=1.5, color='black')),
        name=noodle_df.index[1],
        hovertext=f'{noodle_df.index[1]} มีโซเดียม {noodle_df.โซเดียม.iloc[1]} มิลลิกรัม',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[3],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[3],
            size=noodle_df.โซเดียม.iloc[3]/10,
            opacity=0.9,
            line=dict(width=1.5, color='black')),
        name=noodle_df.index[3],
        hovertext=f'{noodle_df.index[3]} มีโซเดียม {noodle_df.โซเดียม.iloc[3]}',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[4],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[4],
            size=noodle_df.โซเดียม.iloc[4]/10,
            opacity=0.4),
        name=noodle_df.index[4],
        hovertext=f'{noodle_df.index[4]} มีโซเดียม {noodle_df.โซเดียม.iloc[4]}',
        hoverinfo='text'
    )
)



fig.update_yaxes(
    showticklabels=False
)
fig.update_xaxes(
    showticklabels=False
)
fig.update_layout(
    height=370,
    plot_bgcolor='#FFFFFF',
    hovermode='y'
)


#fig.show()