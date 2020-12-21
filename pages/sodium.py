import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output
from charts.sodiplot import fig

layout = html.Div([
    
    html.Div([
        html.H2('อ้างอิงจากเว็บ siriraj online เขาบอกว่า เขาบอกว่า 1 วันไม่ควรบริโภคโซเดียมเกิน 2300 มิลลิกรัมนะ'),
        html.H2('งั้นลองใช้ chart นี้พิจารณาดู ขนาดวงกลมแทน ปริมาณโซเดียมนะ (มิลลิกรัม)'),
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
        html.H2('ก็จะเห็นว่า ใน cluster ของ "ยำยำ ควิก มาม่า" น่ะ ถ้าคนไหนสายสุขภาพละก็ คงต้องมาม่านั่นละนะ'),
        html.H2('แต่ว่าในทั้งหมด 6 แบรนด์เนี่ย จริงๆแล้วแบรนด์ที่ปริมาณโซเดียมน้อยที่สุด คือ "ซื่อสัตย์" นะเอออออ')
    ],
        className='bottom-text'
    )

], id='sodium')