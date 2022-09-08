from dash import dcc, html

estados = ["Aguascalientes",
           "Baja California",
           "Baja California Sur",
           "Campeche",
           "Chiapas",
           "Chihuahua",
           "Ciudad de Mexico",
           "Coahuila",
           "Colima",
           "Durango",
           "Estado de Mexico",
           "Guanajuato",
           "Guerrero",
           "Hidalgo",
           "Jalisco",
           "Michoacan",
           "Morelos",
           "Nayarit",
           "Nuevo Leon",
           "Oaxaca",
           "Puebla",
           "Queretaro",
           "Quintana Roo",
           "San Luis Potosi",
           "Sinaloa",
           "Sonora",
           "Tabasco",
           "Tamaulipas",
           "Tlaxcala",
           "Veracruz",
           "Yucatan",
           "Zacatecas"
           ]

codigos = [43, 431, 4311, 4312, 432, 4321, 433, 4331, 4332, 4333, 4334, 4335, 434, 4341, 4342, 4343,
           435, 4351, 4352, 4353, 4354, 436, 4361, 437, 4371, 4372]

estados = [{"label": x, "value": x} for x in estados]

areas = [{"label": x[0].rstrip(), "value": x[1]} for x in zip(open("TotalFormateado.txt").readlines(), codigos)]
areas2 = [{"label": "Ninguna", "value": "ninguna"}] + areas

panel1 = html.Div(children=[
    html.Label(children="Tipo de Análisis"),
    dcc.RadioItems(
        id="tipo-analisis",
        options=[{"label": "Total", "value": "total"}, {"label": "Comparativo", "value": "comparativo"}],
        value="total",
        labelStyle={"display": "inline-block"})
    ],
    style={"display" : "block"}

)

panel2 = html.Div(children=[
    dcc.Dropdown(options=estados, value="Todo el pais", id="estados"),
    dcc.Dropdown(options=areas, value="43", id="areas")

])

panel3 = html.Div(children=[
    dcc.RangeSlider(min=2010, max=2021, step=1, marks={x: str(x) for x in range(2010,2022)})
])

panel4 = html.Div(children=[
    html.Label(children="Tipo por"),
    dcc.RadioItems(
        id="tipo-analisis2",
        options=[{"label": "Estado", "value": "estado"}, {"label": "Area", "value": "area"}],
        value="estado",
        labelStyle={"display": "inline-block"})
    ],
    style={"display" : "block"}

)

#Panel en caso de que se seleccione la opción de Estado
panel5 = html.Div(children=[
        dcc.Dropdown(options=estados, value="Todo el pais", id="estados1"),
        dcc.Dropdown(options=areas2, value="ninguna", id="area1"),
        dcc.Dropdown(options=areas2, value="ninguna", id="area2"),
        dcc.Dropdown(options=areas2, value="ninguna", id="area3")
]

)

#Panel en caso de que se seleccione la opcion de Area
panel6 = html.Div(children=[
        dcc.Dropdown(options=areas2, value="ninguna", id="area1"),
        dcc.Dropdown(options=estados, value="Todo el pais", id="estados1"),
        dcc.Dropdown(options=estados, value="Todo el pais", id="estados2"),
        dcc.Dropdown(options=estados, value="Todo el pais", id="estados3")
]

)
