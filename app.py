import dash


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