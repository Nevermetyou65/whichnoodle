#ความุ้ม
import plotly.graph_objects as go
import pandas as pd

noodle_df = pd.read_csv('noodle.csv', index_col=0)


fig = go.Figure()


fig.add_traces(
    go.Scatter(
        x=[noodle_df.ความคุ้ม.iloc[0]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[0],
            size=15
        ),
        name=noodle_df.index[0],
        hovertext=f'{noodle_df.index[0]} {noodle_df.ความคุ้ม.iloc[0]} kcal/1บาท',
        hoverinfo='text'
        
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ความคุ้ม.iloc[1]],
        y=[1],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[1],
            size=15,
            opacity=0.5
        ),
        name=noodle_df.index[1],
        hovertext=f'{noodle_df.index[1]} {noodle_df.ความคุ้ม.iloc[1]} kcal/1บาท',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ความคุ้ม.iloc[2]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[2],
            size=15
        ),
        name=noodle_df.index[2],
        hovertext=f'{noodle_df.index[2]} {noodle_df.ความคุ้ม.iloc[2]} kcal/1บาท',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ความคุ้ม.iloc[3]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[3],
            size=15
        ),
        name=noodle_df.index[3],
        hovertext=f'{noodle_df.index[3]} {noodle_df.ความคุ้ม.iloc[3]} kcal/1บาท',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ความคุ้ม.iloc[4]],
        y=[0],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[4],
            size=15
        ),
        name=noodle_df.index[4],
        hovertext=f'{noodle_df.index[4]} {noodle_df.ความคุ้ม.iloc[4]} kcal/1บาท',
        hoverinfo='text'
    )
)

fig.add_traces(
    go.Scatter(
        x=[noodle_df.ความคุ้ม.iloc[5]],
        y=[2],
        mode='markers',
        marker=dict(
            color=noodle_df.color.iloc[5],
            size=15
        ),
        name=noodle_df.index[5],
        hovertext=f'{noodle_df.index[5]} {noodle_df.ความคุ้ม.iloc[5]} kcal/1บาท',
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