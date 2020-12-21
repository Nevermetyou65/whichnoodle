import dash_core_components as dcc
import dash_html_components as html

from pages import price, energy, density, relation, sodium, home, summary
from app import app




app.layout = html.Div([
    home.layout,
    price.layout,
    energy.layout,
    density.layout,
    relation.layout,
    sodium.layout,
    summary.layout
])

if __name__ == '__main__':
    app.run_server(debug=True)