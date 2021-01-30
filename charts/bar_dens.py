#เส้นแน่น
import plotly.graph_objects as go
import pandas as pd

noodle_df = pd.read_csv('noodle.csv', index_col=0)


fig = go.Figure()


fig.add_traces(
    go.Scatter(
        x=[noodle_df.เส้นแน่น.iloc[0]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[0],
            size=15
        ),
        name=noodle_df.index[0],
        hovertext=f'{noodle_df.index[0]} {noodle_df.เส้นแน่น.iloc[0]} กรัม/ลบ.ซม.',
        hoverinfo='text'
        
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.เส้นแน่น.iloc[1]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[1],
            size=15,
            opacity=0.5
        ),
        name=noodle_df.index[1],
        hovertext=f'{noodle_df.index[1]} {noodle_df.เส้นแน่น.iloc[1]} กรัม/ลบ.ซม.',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.เส้นแน่น.iloc[2]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[2],
            size=15
        ),
        name=noodle_df.index[2],
        hovertext=f'{noodle_df.index[2]} {noodle_df.เส้นแน่น.iloc[2]} กรัม/ลบ.ซม.',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.เส้นแน่น.iloc[3]],
        y=[1],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[3],
            size=15
        ),
        name=noodle_df.index[3],
        hovertext=f'{noodle_df.index[3]} {noodle_df.เส้นแน่น.iloc[3]} กรัม/ลบ.ซม.',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.เส้นแน่น.iloc[4]],
        y=[1],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[4],
            size=15
        ),
        name=noodle_df.index[4],
        hovertext=f'{noodle_df.index[4]} {noodle_df.เส้นแน่น.iloc[4]} กรัม/ลบ.ซม',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.เส้นแน่น.iloc[5]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[5],
            size=15
        ),
        name=noodle_df.index[5],
        hovertext=f'{noodle_df.index[5]} {noodle_df.เส้นแน่น.iloc[5]} กรัม/ลบ.ซม.',
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