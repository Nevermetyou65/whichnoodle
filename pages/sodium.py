import dash_core_components as dcc
import dash_html_components as html
from charts.sodiplot import fig

siriraj_link = 'https://www.si.mahidol.ac.th/siriraj_online/thai_version/Health_detail.asp?id=1365#:~:text=%E0%B8%A3%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A2%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%B2%E0%B8%93%E0%B9%82%E0%B8%8B%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B8%A2%E0%B8%A1%E0%B9%81%E0%B8%95%E0%B8%81,%E0%B9%82%E0%B8%8B%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B8%A2%E0%B8%A1%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%9E%E0%B8%B5%E0%B8%A2%E0%B8%87%E0%B8%9E%E0%B8%AD%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1'

layout = html.Div([
    
    html.Div([
        html.H2('อ้างอิงจากเว็บ siriraj online เขาบอกว่า 1 วันไม่ควรบริโภคโซเดียมเกิน 2300 มิลลิกรัม'),
        html.A('siriraj online', href=siriraj_link, target='_blank', rel="noopener noreferrer"),
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
        html.H2('ถ้าคนไหนสายสุขภาพละก็ คงต้องมาม่านั่นละนะ'),
        html.H2('แต่ว่าในทั้งหมด 6 แบรนด์เนี่ย จริงๆแล้วแบรนด์ที่ปริมาณโซเดียมน้อยที่สุด คือ "ซื่อสัตย์" นะเอออออ')
    ],
        className='bottom-text'
    )

], id='sodium')