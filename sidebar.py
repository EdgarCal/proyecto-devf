from dash import Dash, dcc, html
import htmlElements
from variables import estados, areas, codigos

def generarSidebar(tipo_analisis="analisis-total", anio_min=2010, anio_max=2021):

        side1 = html.Div(children="Tipo de Análisis", style={"width": "100%"}, className="texto-blanco")

        side2 = html.Div(children=[dcc.RadioItems(
                id="tipo-analisis",
                options=[{"label": "Total", "value": "analisis-total"},
                         {"label": "Comparativo", "value": "analisis-comparativo"}],
                value=tipo_analisis, className="texto-blanco",
                labelStyle={"display": "inline-block", "margin-left": "10px", "margin-right": "10px"})],
                style={"width": "100%"})

        side4 = html.Div(children="Rango de tiempo", style={"width": "100%"}, className="texto-blanco")

        side5 = html.Div(children=[
                dcc.RangeSlider(min=2010, max=2021, value=[anio_min, anio_max], step=1, marks={x: str(x) for x in range(2010, 2022)}, className="range-slider", id="range-slider")
        ], style={"width": "100%", "margin-top": "20px"})

        if tipo_analisis == "analisis-total":
                side3 = html.Div(children=[
                        html.Div(children="Estado a analizar", className="texto-blanco"),
                        dcc.Dropdown(options=[{"label": "Todo el pais", "value": "Todo el pais"}] + estados,
                                     value="Todo el pais", id="estados",
                                     style={"margin-top": "10px", "margin-bottom": "10px"}),
                        html.Div(children="Area a analizar", className="texto-blanco"),
                        dcc.Dropdown(options=areas, value="43", id="areas",
                                     style={"margin-top": "10px", "margin-bottom": "10px"})], id="side3", style={"margin-top" : "20px", "margin-bottom" : "20px"})

        else:

                side6a = html.Div(children=[dcc.RadioItems(
                        id="tipo-analisis2",
                        options=[{"label": "Estado", "value": "analisis-estado"},
                                 {"label": "Area", "value": "analisis-area"}],
                        value="analisis-estado", className="texto-blanco",
                        labelStyle={"display": "inline-block", "margin-left": "10px", "margin-right": "10px"})],
                        style={"width": "100%"})

                side6b = html.Div(children=[
                        html.Div(children="Estado a analizar", className="texto-blanco"),
                        dcc.Dropdown(options=estados,
                                     value="Aguascalientes", id="estadosa",
                                     style={"margin-top": "10px", "margin-bottom": "10px"}),
                        html.Div(children="Areas a analizar (Hasta 3)", className="texto-blanco"),
                        dcc.Dropdown(options=areas[1:], id="areas1", style={"margin-top": "10px", "margin-bottom": "10px"}),
                        dcc.Dropdown(options=areas[1:], id="areas2", style={"margin-top": "10px", "margin-bottom": "10px"}),
                        dcc.Dropdown(options=areas[1:], id="areas3", style={"margin-top": "10px", "margin-bottom": "10px"})

                ], style={"margin-top": "20px", "margin-bottom": "20px"})

                side6c = html.Div(children=[
                        html.Div(children="Area a analizar", className="texto-blanco"),
                        dcc.Dropdown(options=areas, value="43", id="areasa",
                                     style={"margin-top": "10px", "margin-bottom": "10px"}),
                        html.Div(children="Estados a analizar (Hasta 3)", className="texto-blanco"),
                        dcc.Dropdown(options=estados, id="estados1",
                                     style={"margin-top": "10px", "margin-bottom": "10px"}),
                        dcc.Dropdown(options=estados, id="estados2",
                                     style={"margin-top": "10px", "margin-bottom": "10px"}),
                        dcc.Dropdown(options=estados, id="estados3",
                                     style={"margin-top": "10px", "margin-bottom": "10px"})

                ], style={"margin-top": "20px", "margin-bottom": "20px"})

                side3 = html.Div(children=[
                        side6a, side6b, side6c
                ], id="side3")

        return [side1, side2, side3, side4, side5]

def generarSide3(tipo_analisis, tipo_analisis2="analisis-estado"):

    if tipo_analisis == "analisis-total":
        side3 = html.Div(children=[
            html.Div(children="Estado a analizar", className="texto-blanco"),
            dcc.Dropdown(options=[{"label": "Todo el pais", "value": "Todo el pais"}] + estados,
                         value="Todo el pais", id="estados",
                         style={"margin-top": "10px", "margin-bottom": "10px"}),
            html.Div(children="Area a analizar", className="texto-blanco"),
            dcc.Dropdown(options=areas, value="43", id="areas",
                         style={"margin-top": "10px", "margin-bottom": "10px"})], id="side3",
            style={"margin-top": "20px", "margin-bottom": "20px"})

    else:

        side3a = html.Div(children=[dcc.RadioItems(
            id="tipo-analisis2",
            options=[{"label": "Estado", "value": "analisis-estado"},
                     {"label": "Area", "value": "analisis-area"}],
            value="analisis-estado", className="texto-blanco",
            labelStyle={"display": "inline-block", "margin-left": "10px", "margin-right": "10px"})],
            style={"width": "100%"})

        if tipo_analisis2 == "analisis-estado":
            side3b = html.Div(children=[
                html.Div(children="Estado a analizar", className="texto-blanco"),
                dcc.Dropdown(options=[{"label": "Todo el pais", "value": "Todo el pais"}] + estados,
                             value="Todo el pais", id="estadosa",
                             style={"margin-top": "10px", "margin-bottom": "10px"}),
                html.Div(children="Areas a analizar (Hasta 3)", className="texto-blanco"),
                dcc.Dropdown(options=areas, id="areas1", style={"margin-top": "10px", "margin-bottom": "10px"}),
                dcc.Dropdown(options=areas, id="areas2", style={"margin-top": "10px", "margin-bottom": "10px"}),
                dcc.Dropdown(options=areas, id="areas3", style={"margin-top": "10px", "margin-bottom": "10px"})

            ], id="side3b", style={"margin-top": "20px", "margin-bottom": "20px"})
        else:
            side3b = html.Div(children=[
                html.Div(children="Area a analizar", className="texto-blanco"),
                dcc.Dropdown(options=areas, value="43", id="areasa",
                             style={"margin-top": "10px", "margin-bottom": "10px"}),
                html.Div(children="Estados a analizar (Hasta 3)", className="texto-blanco"),
                dcc.Dropdown(options=estados, id="estados1",
                             style={"margin-top": "10px", "margin-bottom": "10px"}),
                dcc.Dropdown(options=estados, id="estados2",
                             style={"margin-top": "10px", "margin-bottom": "10px"}),
                dcc.Dropdown(options=estados, id="estados3",
                             style={"margin-top": "10px", "margin-bottom": "10px"})

            ], id="side3b", style={"margin-top": "20px", "margin-bottom": "20px"})


        side3 = html.Div(children=[
            side3a, side3b
        ], id="side3")


    return side3

def generarSide3b(tipo_analisis2):
    if tipo_analisis2 == "analisis-estado":
        content = [
                html.Div(children="Estado a analizar", className="texto-blanco"),
                dcc.Dropdown(options=estados,
                             value="Aguascalientes", id="estadosa",
                             style={"margin-top": "10px", "margin-bottom": "10px"}),
                html.Div(children="Areas a analizar (Hasta 3)", className="texto-blanco"),
                dcc.Dropdown(options=areas, id="areas1", value="431", style={"margin-top": "10px", "margin-bottom": "10px"}),
                dcc.Dropdown(options=areas, id="areas2", style={"margin-top": "10px", "margin-bottom": "10px"}),
                dcc.Dropdown(options=areas, id="areas3", style={"margin-top": "10px", "margin-bottom": "10px"})

            ]
    else:
        content = [
                html.Div(children="Area a analizar", className="texto-blanco"),
                dcc.Dropdown(options=areas[1:], value="431", id="areasa",
                             style={"margin-top": "10px", "margin-bottom": "10px"}),
                html.Div(children="Estados a analizar (Hasta 3)", className="texto-blanco"),
                dcc.Dropdown(options=estados, id="estados1", value="Aguascalientes",
                             style={"margin-top": "10px", "margin-bottom": "10px"}),
                dcc.Dropdown(options=estados, id="estados2",
                             style={"margin-top": "10px", "margin-bottom": "10px"}),
                dcc.Dropdown(options=estados, id="estados3",
                             style={"margin-top": "10px", "margin-bottom": "10px"})

            ]
    return content