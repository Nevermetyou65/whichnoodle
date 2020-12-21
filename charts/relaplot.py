#relation

import plotly.graph_objects as go
import pandas as pd

noodle_df = pd.read_csv('noodle.csv', index_col=0)



fig = go.Figure()

for i in range(len(noodle_df.index.to_list())):
    fig.add_traces(
    go.Scatter(
        x=[noodle_df.เส้นแน่น.iloc[i]],
        y=[noodle_df.ความคุ้ม.iloc[i]],
        mode='markers',
        name=noodle_df.index[i],
        marker=dict(
            size=15,
            color=noodle_df.color.iloc[i],
            opacity=0.85),
        
    )
)
fig.update_yaxes(
    showline=False
)
fig.update_xaxes(
    showline=False
)
    
fig.update_layout(
    xaxis_title="ความหนาแน่นของเส้น (กรัม/ลบ.ซม)",
    yaxis_title="ค่าความคุ้ม (พลังงานที่ได้เป็น kcal / 1บาทที่จ่าย)",
    template='simple_white',
)
#fig.show()