#ราคา 
import plotly.graph_objects as go
import pandas as pd

noodle_df = pd.read_csv('noodle.csv', index_col=0)

fig = go.Figure()


fig.add_traces(
    go.Scatter(
        x=[noodle_df.ราคา.iloc[0]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[0],
            size=15
        ),
        name=noodle_df.index[0],
        hovertext=f'{noodle_df.index[0]} ราคา {noodle_df.ราคา.iloc[0]}',
        hoverinfo='text'
        
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ราคา.iloc[1]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[1],
            size=15,
            opacity=0.5
        ),
        name=noodle_df.index[1],
        hovertext=f'{noodle_df.index[1]} ราคา {noodle_df.ราคา.iloc[1]}',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ราคา.iloc[2]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[2],
            size=15
        ),
        name=noodle_df.index[2],
        hovertext=f'{noodle_df.index[2]} ราคา {noodle_df.ราคา.iloc[2]}',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ราคา.iloc[3]],
        y=[1],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[3],
            size=15
        ),
        name=noodle_df.index[3],
        hovertext=f'{noodle_df.index[3]} ราคา {noodle_df.ราคา.iloc[3]}',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ราคา.iloc[4]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[4],
            size=15
        ),
        name=noodle_df.index[4],
        hovertext=f'{noodle_df.index[4]} ราคา {noodle_df.ราคา.iloc[4]}',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ราคา.iloc[5]],
        y=[2],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[5],
            size=15
        ),
        name=noodle_df.index[5],
        hovertext=f'{noodle_df.index[5]} ราคา {noodle_df.ราคา.iloc[5]}',
        hoverinfo='text'
    )
)

fig.update_yaxes(
    showticklabels=False
)
fig.update_xaxes(
    ticks='inside',
    dtick=1
)
fig.update_layout(
    height=330,
    plot_bgcolor='#FFFFFF',
    hovermode='x',
)


#fig.show()