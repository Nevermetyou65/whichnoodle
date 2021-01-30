#relation hi-light
import plotly.graph_objects as go
import pandas as pd

noodle_df = pd.read_csv('noodle.csv', index_col=0)


fig_hi = go.Figure()


for i in range(len(noodle_df.index.to_list())):
    
    if i in [0, 4, 5]:
        fig_hi.add_traces(
        go.Scatter(
            x=[noodle_df.เส้นแน่น.iloc[i]],
            y=[noodle_df.ความคุ้ม.iloc[i]],
            mode='markers',
            name=noodle_df.index[i],
            marker=dict(
                size=15,
                color=noodle_df.color.iloc[i],
                opacity=0.4),
        
            )
        )
    else:
        fig_hi.add_traces(
        go.Scatter(
            x=[noodle_df.เส้นแน่น.iloc[i]],
            y=[noodle_df.ความคุ้ม.iloc[i]],
            mode='markers',
            name=noodle_df.index[i],
            marker=dict(
                size=15,
                color=noodle_df.color.iloc[i],
                line=dict(width=1.5, color='black')),
        
            )
        
        )
fig_hi.update_yaxes(
    showline=False
)
fig_hi.update_xaxes(
    showline=False
)
fig_hi.update_layout(
    xaxis_title="ความหนาแน่นเส้น (กรัม / ลบ.ซม.)",
    yaxis_title="ความคุ้ม (kcal / 1บาท)",
    template='simple_white',
    
)
#fig.show()