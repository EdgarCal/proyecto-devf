import dash.exceptions
from dash import Dash, dcc, html
import htmlElements
from sidebar import *
from dash.dependencies import Input, Output
from generadorDeGraficas import *

extended = True

app = Dash(__name__)

server = app.server

app.layout = html.Div(children=[
    html.Div(children=generarSidebar(), id="mySidebar", className="sidebar"),
    html.Div(children=[
        html.Div(children=[
            html.Button("+", id="ajuste-button", n_clicks=0),
            "COMERCIOS AL POR MAYOR",
            html.Br(),
            html.Div(children=[], id="grafica-1"),
            html.Div(children=[], id="grafica-2",),
            html.Div(children=[], id="grafica-3",),
            html.Div(children=[], id="grafica-4",),
            html.Div(children=[], id="grafica-5",),
            html.Div(children=[], id="grafica-6",)
        ],
            className="main-top",
                 style={"font-size": "40px", "height": "150px", "width": "100%", "background-color" : "#B2FFF0"})
    ], id="main", style={"margin-left": "600px", "width": "1920px", "padding-left" : "100px", "padding-right": "100px"})
], style={"display": "inline", "background-color" : "#B2FFF0"})

@app.callback(
    Output(component_id="side3", component_property="children"),
    Input(component_id="tipo-analisis", component_property="value")

)
def cambiarTipoAnalisis(input_value):
    return generarSide3(input_value)

@app.callback(
    Output(component_id="side3b", component_property="children"),
    Input(component_id="tipo-analisis2", component_property="value")
)
def cambiarTipoAnalisis2(input_value):
    return generarSide3b(input_value)


@app.callback(
    Output("mySidebar", "style"),
    Output("main", "style"),
    Input("ajuste-button", "n_clicks"), prevent_initial_call=True
)
def ajustarSidebar(input_value):
    global extended
    if extended:
        extended = False
        return {"width" : "0px"} , {"margin-left" : "0px"}
    else:
        extended = True
        return {"width": "600px"}, {"margin-left": "600px"}

@app.callback(
    Output(component_id="grafica-1", component_property="children"),
    Output(component_id="grafica-2", component_property="children"),
    Output(component_id="grafica-3", component_property="children"),
    Input(component_id="tipo-analisis", component_property="value"),
    Input(component_id="estados", component_property="value"),
    Input(component_id="areas", component_property="value"),
    Input(component_id="range-slider", component_property="value")
)
def cambiarGraficas(tipo_analisis, estados, areas, rango):
    return generarGrafica2(tipo_analisis=tipo_analisis, estado_analisis=estados, area_analisis=areas, rango_tiempo=rango)

@app.callback(
    Output(component_id="grafica-4", component_property="children"),
    Output(component_id="grafica-5", component_property="children"),
    Output(component_id="grafica-6", component_property="children"),
    Input(component_id="tipo-analisis2", component_property="value"),
    Input(component_id="estadosa", component_property="value"),
    #Input(component_id="areasa", component_property="value"),
    Input(component_id="areas1", component_property="value"),
    Input(component_id="areas2", component_property="value"),
    Input(component_id="areas3", component_property="value"),
    #Input(component_id="estados1", component_property="value"),
    #Input(component_id="estados2", component_property="value"),
    #Input(component_id="estados3", component_property="value"),
    Input(component_id="range-slider", component_property="value"), prevent_initial_call=True
)
def cambiarGraficas2(tipo_analisis2, estadosa, areas1, areas2, areas3, rango):
    return generarGrafica2(tipo_analisis="analisis-comparativo", rango_tiempo=rango, tipo_analisis2=tipo_analisis2,estado_analisis2=estadosa, area1=areas1, area2=areas2, area3=areas3,)

@app.callback(
    Output(component_id="grafica-1", component_property="style"),
    Output(component_id="grafica-2", component_property="style"),
    Output(component_id="grafica-3", component_property="style"),
    Output(component_id="grafica-4", component_property="style"),
    Output(component_id="grafica-5", component_property="style"),
    Output(component_id="grafica-6", component_property="style"),
    Input(component_id="tipo-analisis", component_property="value")
)
def mostrarOcultarGraficas(tipo_analisis):
    if tipo_analisis == "analisis-total":
        return {"display": "inline", "width" : "60%", "height": "100%"}, {"display": "inline-block"}, {"display": "inline-block"}, {"display": "none"}, {"display": "none"}, {"display": "none"}
    else:
        return {"display": "none"}, {"display": "none"}, {"display": "none"}, {"width": "100%", "display": "inline-block"}, {
            "width": "60%", "display": "inline-block"}, {"width": "40%", "display": "inline-block"}


if __name__ == "__main__":
    app.run_server(debug=True)