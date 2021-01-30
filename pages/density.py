import dash_core_components as dcc
import dash_html_components as html
from charts.bar_dens import fig

layout = html.Div([

    html.Div([
        html.H2('ราคาไปแล้ว คุ้มไปแล้ว แล้วอิ่มอะะ? เห็นก้อนใหญ่ๆแต่จริงๆแล้วมันพรุนรึเปล่านะ?'),
        html.H2('ไหนลองดู "ความหนาแน่นเส้น" กัน'),
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
        html.H2('คราวนี้เป็น ควิก แฮะที่เส้น แน๊นแน่นๆๆๆๆ')
    ],
        className='bottom-text'
    )


], id='density')