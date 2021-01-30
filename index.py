import dash_core_components as dcc
import dash_html_components as html
from app import app
from pages import home, preface, price, energy, density, relation, sodium, summary, ending, joke


server = app.server
app.layout = html.Div([
    home.layout,
    preface.layout,
    price.layout,
    energy.layout,
    density.layout,
    relation.layout,
    sodium.layout,
    summary.layout,
    ending.layout,
    joke.layout
])


if __name__ == '__main__':
    app.run_server(debug=True)