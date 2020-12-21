import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output
from charts.bar_pri import fig

layout = html.Div([
    
    html.Div([
        html.H2('ถ้างั้นมาเริ่มจาก "อันไหนถูดสุดนะ?" ลองดู chart ก็จะเห็นว่า...'),
        html.H4('(ลองเอา mouse ไปวงบนวงกลมดู..)')
    ],
        className='top-text'
    ),

    html.Div(
        dcc.Graph(
            figure=fig, 
            config={'displayModeBar' : False}
        ),
        className='fig-center'
    ),

    html.Div([
        html.H2('ยำยำ ถูกสุด แต่ ไวไว แพงจังเลย'),
        html.H4('**เป็นราคา 1 ซองใน 1 pack ใหญ่')
    ],
        className='bottom-text'
    )

], id = 'price')