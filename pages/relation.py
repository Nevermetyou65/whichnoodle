import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from app import app

from charts.relaplot import fig
from charts.relaplothilight import fig_hi

layout = html.Div([

    html.Div([
        html.H2('โอเคคคค แล้วซื้ออันไหนดีเนี่ยยยยยย??? ดูมาขนาดนี้แล้วยัง งงๆ'),
        html.H2('ลองดู chart นี้สิจะได้ตัดสินได้จาก ทั้ง "ความคุ้ม" และ "เส้นแน่น" เลย')
    ], 
        className='top-text'
    ),

    html.Div([
        dcc.Graph(
            figure=fig_hi, 
            config={'displayModeBar' : False},
            id='relation-plot',
        )
    ],
        className='fig-center'
    ),

    html.Div(
       dcc.RadioItems(
            options=[
                {'label':'hi-light','value':'hi-light'},
                {'label':'normal', 'value':'normal'}
            ],
            value='normal',
            id='radio-item',
            className='item-center'
        )
    ),

    html.Div([
        html.H3('เห็นเป็น cluster เลยใช่ไหมว่ากลุ่มไหนน่าจะ "ดีวว" อะ มันก็น่าจะเป็น ยำยำ มาม่า และ ควิกนะ'),
        html.H3('แต่ว่ากินบะหมี่กึ่งสำเร็จรูปเยอะมันก็ไม่ดีทุกคนก็รู้เพราะว่าโซเดียมมันเยอะ'),
        html.H4('แล้วถ้างั้น ใน 3 ยี่ห้อที่เราบอกว่า "ดีวว" เนี่ย อันไหนควรเลือกนะ..ลองใช้ปริมาณโซเดียมตัดสินดู..หน้าต่อไป!!'),
    ], 
        className='bottom-text'
    ),

], id='relation')

@app.callback(
    Output('relation-plot', 'figure'),
    Input('radio-item', 'value')
)
def display_chart(value):
    if value == 'normal':
        return fig
    else:
        return fig_hi


