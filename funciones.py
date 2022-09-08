from dash.dependencies import Input, Output
from sidebar import *
from test1 import app

@app.callback(
    Output(component_id="mySidebar", component_property="children"),
    Input(component_id="tipo-analisis", component_property="value")
)
def cambiarTipoAnalisis(input_value):
    if input_value == "analisis-comparativo":
        return [side1, side2, side6, side4, side5]
    else:
        return [side1, side2, side6, side4, side5]