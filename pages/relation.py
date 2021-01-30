import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from charts.relaplot import fig
from charts.relaplothilight import fig_hi
from app import app

layout = html.Div([

    html.Div([
        html.H2('แล้วซื้ออันไหนดีเนี่ย??'),
        html.H2('ถ้างั้นลองดู "ความคุ้ม" และ "เส้นแน่น" พร้อมกันเลย')
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
        html.H3('เห็นเลยใช่ไหมว่ากลุ่มไหนน่าจะ "ดี" มันก็น่าจะเป็น ยำยำ มาม่า และ ควิกนะ'),
        html.H3('แล้วถ้างั้น ใน 3 ยี่ห้อที่เราบอกว่า "ดี" เนี่ย อันไหนโซเดียมมันน้อย ดีต่อไตนะ??'),
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


