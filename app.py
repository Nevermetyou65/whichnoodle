import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from pages import price, energy, density, relation, sodium, home, summary
from charts.relaplot import fig
from charts.relaplothilight import fig_hi




external_stylesheets = [
    # 'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # 'https://fonts.googleapis.com/css?family=Chonburi',
    #'https://fonts.googleapis.com/css2?family=Noto+Sans',
    'https://fonts.googleapis.com/css2?family=Kanit&display=swap',

    #dbc.themes.BOOTSTRAP,
    # 'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
    # {
    #     'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    #     'rel': 'stylesheet',
    #     'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
    #     'crossorigin': 'anonymous'
    # }
 ]

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)
server = app.server
app.layout = html.Div([
    home.layout,
    price.layout,
    energy.layout,
    density.layout,
    relation.layout,
    sodium.layout,
    summary.layout
])

@app.callback(
    Output('relation-plot', 'figure'),
    Input('radio-item', 'value')
)
def display_chart(value):
    if value == 'normal':
        return fig
    else:
        return fig_hi

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
    else:
        return [
            html.Img(src=app.get_asset_url('ซื่อสัตย์ต้มยำกุ้ง.png'))
        ]




if __name__ == '__main__':
    app.run_server(debug=True)