import dash_core_components as dcc
import dash_html_components as html
from charts.bar_ene import fig

layout = html.Div([

    html.Div([
        html.H2('แล้วกินอันไหนถึงคุ้ม?  1 บาท ที่จ่ายไปนี่ได้กี่แคลนะ??'),
        html.H4('(ลองเอา mouse ไปวงบนวงกลมดู..)')
    ],
        className='top-text'
    ),
    
    html.Div([
        dcc.Graph(
            figure=fig, 
            config={'displayModeBar' : False}
        )
    ],
        className='fig-center'
    ),

    html.Div([
        html.H2('แบบนี้ ยำยำ ก็ยังดูดีนะเนี่ยไหนลองดูต่อไปสิ..')
    ],
        className='bottom-text'
    )


    

], id='energy')