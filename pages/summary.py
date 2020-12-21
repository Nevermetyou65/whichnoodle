import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from app import app




layout = html.Div([
    html.Div([
        html.H1('สรุป!! ถ้าเราต้องการความ...')
    ],
        className='top-text'
    ),

    html.Div([
        dcc.RadioItems(
        id='radio-item2',
        options=[
            {'label': 'ถูกและคุ้ม', 'value': 1},
            {'label': 'เส้นแน่น', 'value': 2},
            {'label': 'คุ้ม+เส้นแน่น', 'value': 3},
            {'label':'คุ้ม+เส้นแน่น+โซเดียมน้อย', 'value': 4},
            {'label':'โซเดียมน้อยอย่างเดียว', 'value': 5}
        ],
        value=1,
        labelStyle={'display': 'inline-block'}
        ) 
    ],
        className='choice'
    ),
    html.Div([
        html.H2('ก็ต้องเลือก!!')
    ],
        className='bottom-text'
    ),
    
    html.Div(id='img-container', className='fig-center')


],
    id='summary'
)

@app.callback(
    Output('img-container', 'children'),
    Input('radio-item2', 'value')
)
def display_img(value):
    if value == 1:
        return [
            html.Img(src=app.get_asset_url('ยำยำต้มยำกุ้ง.png'))
        ]
    elif value == 2:
        return [
            html.Img(src=app.get_asset_url('ควิกต้มยำกุ้ง.png'))
        ]
    elif value == 3:
        return [
            html.Div([
                html.Img(src=app.get_asset_url('ยำยำต้มยำกุ้ง.png')),
                html.Img(src=app.get_asset_url('ควิกต้มยำกุ้ง.png')),
                html.Img(src=app.get_asset_url('มาม่าต้มยำกุ้ง.png'))
            ],
                className='img-group'
            )
        ]
    elif value == 4:
        return [
            html.Img(src=app.get_asset_url('มาม่าต้มยำกุ้ง.png'))
        ]
    elif value == 5:
        return [
            html.Img(src=app.get_asset_url('ซื่อสัตย์ต้มยำกุ้ง.png'))
        ]

