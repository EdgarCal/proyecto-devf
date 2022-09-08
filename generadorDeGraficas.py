import plotly.express as px
import pandas as pd
from dash import dcc
from variables import codigos_to_areas, mex_geo

df = pd.read_csv("cleaned2.csv")

def generarGrafica2(tipo_analisis="analisis-total", area_analisis="43", estado_analisis="Todo el pais", rango_tiempo=[2010,2021],
                    tipo_analisis2="analisis-estado", estado_analisis2="Aguascalientes", area1=None, area2=None, area3=None,
                    area_analisis2 = "431", estado1=None, estado2=None, estado3= None):

    if rango_tiempo==None: rango_tiempo = [2010,2021]

    if tipo_analisis == "analisis-total":

        if estado_analisis == "Todo el pais":
            df_temporal = df.iloc[::]
        else:
            df_temporal = df[df["entidad"] == estado_analisis]

        if area_analisis == "43":
            pass

        else:
            if int(area_analisis) < 1000:
                df_temporal = df_temporal[df_temporal["codigo_act"] == int(area_analisis)]
            else:
                df_temporal = df_temporal[df_temporal["codigo_act2"] == int(area_analisis)]


        df_temporal = df_temporal[df_temporal["fecha_alta"].apply(lambda x: int(x)) >= rango_tiempo[0]]
        df_temporal = df_temporal[df_temporal["fecha_alta"].apply(lambda x: int(x)) <= rango_tiempo[1]]
        df_temporal2 = df_temporal.iloc[::]


        if estado_analisis == "Todo el pais":
            df_temporal = df_temporal["entidad"].value_counts()
        else:
            df_temporal = df_temporal["municipio"].value_counts()

        df_temporal = df_temporal.to_frame()
        df_temporal.reset_index(inplace=True)
        df_temporal = df_temporal.head(10)[::-1]

        if estado_analisis == "Todo el pais":
            fig = px.bar(df_temporal, x="entidad", y="index", orientation='h', labels={"entidad" : "Número de comercios", "index" : "Estado"}, title=f"Comercios en {estado_analisis}", width=900)
        else:
            fig = px.bar(df_temporal, x="municipio", y="index", orientation='h', labels={"municipio" : "Número de comercios", "index" : "Municipio"}, title=f"Comercios en {estado_analisis}", width=900)
        graph1 = dcc.Graph(figure=fig)

        df_temporal2 = df_temporal2["fecha_alta"].value_counts()
        df_temporal2 = df_temporal2.to_frame()
        df_temporal2.reset_index(inplace=True)

        fig2 = px.pie(df_temporal2, values="fecha_alta", names="index", title="Registros por año", labels={"index": "Año", "fecha_alta": "Número de comercios"})
        graph2 = dcc.Graph(figure=fig2)

        # Gráfica de mapa
        df_temporal3 = df.iloc[::]
        if int(area_analisis) == 43:
            pass
        elif int(area_analisis) < 1000:
            df_temporal3 = df_temporal3[df_temporal3["codigo_act"] == int(area_analisis)]
        else:
            df_temporal3 = df_temporal3[df_temporal3["codigo_act2"] == int(area_analisis)]
        df_temporal3 = df_temporal3[df_temporal3["fecha_alta"].apply(lambda x: int(x)) >= rango_tiempo[0]]
        df_temporal3 = df_temporal3[df_temporal3["fecha_alta"].apply(lambda x: int(x)) <= rango_tiempo[1]]
        df_temporal3 = df_temporal3["entidad"].value_counts()
        df_temporal3 = df_temporal3.to_frame()
        df_temporal3.reset_index(inplace=True)


        fig3 = px.choropleth(df_temporal3, geojson=mex_geo, color="entidad", locations="index", fitbounds="locations", color_continuous_scale="greens",
                             title=f"Comercio de {codigos_to_areas[int(area_analisis)]} en todo México", labels={"index": "Estado", "entidad": "Número de comercios"}, width=1600, height=900)
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        graph3 = dcc.Graph(figure=fig3)
        return graph3, graph1, graph2

    else:

        df_temporal = df.iloc[::]

        if tipo_analisis2 == "analisis-estado":

            df_temporal = df_temporal[df["entidad"] == estado_analisis2]

            if area2 == area1:
                area2 = None
            if area3 == area1 or area3 == area2:
                area3 = None

            if area1:
                if int(area1) < 1000:
                    filtro1 = df_temporal["codigo_act"] == int(area1)
                else:
                    filtro1 = df_temporal["codigo_act2"] == int(area1)
            else:
                filtro1 = df_temporal["fecha_alta"] == 1990

            if area2:
                if int(area2) < 1000:
                    filtro2 = df_temporal["codigo_act"] == int(area2)
                else:
                    filtro2 = df_temporal["codigo_act2"] == int(area2)
            else:
                filtro2 = df_temporal["fecha_alta"] == 1990

            if area3:
                if int(area3) < 1000:
                    filtro3 = df_temporal["codigo_act"] == int(area3)
                else:
                    filtro3 = df_temporal["codigo_act2"] == int(area3)
            else:
                filtro3 = df_temporal["fecha_alta"] == 1990

            df_temporal = df_temporal[((filtro1) | (filtro2) | (filtro3))]

            if area1:
                if int(area1) < 1000:
                    temp1 = df_temporal[df_temporal["codigo_act"] == int(area1)]
                    temp1 = temp1["fecha_alta"].value_counts()
                else:
                    temp1 = df_temporal[df_temporal["codigo_act2"] == int(area1)]
                    temp1 = temp1["fecha_alta"].value_counts()
                temp1 = temp1.to_frame()
                temp1.reset_index(inplace=True)
                temp1 = temp1.sort_values(by="index")
                temp1.insert(1, "numero", codigos_to_areas[int(area1)])
            else:
                temp1 = None

            if area2:
                if int(area2) < 1000:
                    temp2 = df_temporal[df_temporal["codigo_act"] == int(area2)]
                    temp2 = temp2["fecha_alta"].value_counts()
                else:
                    temp2 = df_temporal[df_temporal["codigo_act2"] == int(area2)]
                    temp2 = temp2["fecha_alta"].value_counts()
                temp2 = temp2.to_frame()
                temp2.reset_index(inplace=True)
                temp2 = temp2.sort_values(by="index")
                temp2.insert(1, "numero", codigos_to_areas[int(area2)])
            else:
                temp2 = None

            if area3:
                if int(area3) < 1000:
                    temp3 = df_temporal[df_temporal["codigo_act"] == int(area3)]
                    temp3 = temp3["fecha_alta"].value_counts()
                else:
                    temp3 = df_temporal[df_temporal["codigo_act2"] == int(area3)]
                    temp3 = temp3["fecha_alta"].value_counts()
                temp3 = temp3.to_frame()
                temp3.reset_index(inplace=True)
                temp3 = temp3.sort_values(by="index")
                temp3.insert(1, "numero", codigos_to_areas[int(area3)])
            else:
                temp3 = None

            temp4 = []
            if area1:
                temp1.reset_index(drop=True, inplace=True)
                lista_temp1 = list(temp1["fecha_alta"])
                for i in range(1, len(lista_temp1)):
                    lista_temp1[i] += lista_temp1[i-1]
                series_temp1 = pd.Series(lista_temp1)
                temp1["fecha_alta_2"] =series_temp1
                temp4.append(temp1)
            if area2:
                temp2.reset_index(drop=True, inplace=True)
                lista_temp2 = list(temp2["fecha_alta"])
                for i in range(1, len(lista_temp2)):
                    lista_temp2[i] += lista_temp2[i - 1]
                series_temp2 = pd.Series(lista_temp2)
                temp2["fecha_alta_2"] = series_temp2
                temp4.append(temp2)
            if area3:
                temp3.reset_index(drop=True, inplace=True)
                lista_temp3 = list(temp3["fecha_alta"])
                for i in range(1, len(lista_temp3)):
                    lista_temp3[i] += lista_temp3[i - 1]
                series_temp3 = pd.Series(lista_temp3)
                temp3["fecha_alta_2"] = series_temp3
                temp4.append(temp3)

            if not temp4:
                all_data = pd.DataFrame({"fecha_alta" : [], "index" : [], "numero" : []})
            else:
                all_data = pd.concat(temp4, ignore_index=True)

            all_data = all_data[all_data["index"].apply(lambda x: int(x)) >= rango_tiempo[0]]
            all_data = all_data[all_data["index"].apply(lambda x: int(x)) <= rango_tiempo[1]]
            fig1 = px.line(all_data, x="index", y="fecha_alta", color="numero", markers=True, labels={"index": "Año", "fecha_alta": "Número de comercios nuevos", "numero": "Área"}, title="Registros nuevos por año")
            fig1.update_traces(showlegend=False)
            graph1 = dcc.Graph(figure=fig1)
            fig2 = px.line(all_data, x="index", y="fecha_alta_2", color="numero", markers=True,
                           labels={"index": "Año", "fecha_alta_2": "Número de comercios totales", "numero": "Área"}, title="Registros progresivos")
            graph2 = dcc.Graph(figure=fig2)
            all_data = all_data[all_data["index"] == int(rango_tiempo[1])]
            fig3 = px.pie(all_data, values="fecha_alta_2", names="numero", title="Registros al final del periodo", labels={"numero": "Área", "fecha_alta_2": "Número de comercios totales"})
            fig3.update_traces(showlegend=False)
            graph3 = dcc.Graph(figure=fig3)
            return graph2, graph1, graph3

        else:

            if int(area_analisis2) < 1000:
                df_temporal = df_temporal[df["codigo_act"] == int(estado_analisis2)]
            else:
                df_temporal = df_temporal[df["codigo_act2"] == int(estado_analisis2)]

            if estado2 == estado1:
                estado2 = None
            if estado3 == estado1 or estado3 == estado2:
                estado3 = None

            if estado1:
                filtro1 = df_temporal["entidad"] == estado1
            else:
                filtro1 = df_temporal["fecha_alta"] == 1990

            if estado2:
                filtro2 = df_temporal["entidad"] == estado2
            else:
                filtro2 = df_temporal["fecha_alta"] == 1990

            if estado3:
                filtro3 = df_temporal["entidad"] == estado3
            else:
                filtro3 = df_temporal["fecha_alta"] == 1990

            df_temporal = df_temporal[((filtro1) | (filtro2) | (filtro3))]

            if estado1:
                temp1 = df_temporal[df_temporal["entidad"] == estado1]
                temp1 = temp1["fecha_alta"].value_counts()
                temp1 = temp1.to_frame()
                temp1.reset_index(inplace=True)
                temp1 = temp1.sort_values(by="index")
                temp1.insert(1, "numero", estado1)
            else:
                temp1 = None

            if estado2:
                temp2 = df_temporal[df_temporal["entidad"] == estado2]
                temp2 = temp2["fecha_alta"].value_counts()
                temp2 = temp2.to_frame()
                temp2.reset_index(inplace=True)
                temp2 = temp2.sort_values(by="index")
                temp2.insert(1, "numero", estado2)
            else:
                temp2 = None

            if estado3:
                temp3 = df_temporal[df_temporal["entidad"] == estado3]
                temp3 = temp3["fecha_alta"].value_counts()
                temp3 = temp3.to_frame()
                temp3.reset_index(inplace=True)
                temp3 = temp3.sort_values(by="index")
                temp3.insert(1, "numero", estado3)
            else:
                temp3 = None

            temp4 = []
            if area1:
                temp1.reset_index(drop=True, inplace=True)
                lista_temp1 = list(temp1["fecha_alta"])
                for i in range(1, len(lista_temp1)):
                    lista_temp1[i] += lista_temp1[i - 1]
                series_temp1 = pd.Series(lista_temp1)
                temp1["fecha_alta_2"] = series_temp1
                temp4.append(temp1)
            if area2:
                temp2.reset_index(drop=True, inplace=True)
                lista_temp2 = list(temp2["fecha_alta"])
                for i in range(1, len(lista_temp2)):
                    lista_temp2[i] += lista_temp2[i - 1]
                series_temp2 = pd.Series(lista_temp2)
                temp2["fecha_alta_2"] = series_temp2
                temp4.append(temp2)
            if area3:
                temp3.reset_index(drop=True, inplace=True)
                lista_temp3 = list(temp3["fecha_alta"])
                for i in range(1, len(lista_temp3)):
                    lista_temp3[i] += lista_temp3[i - 1]
                series_temp3 = pd.Series(lista_temp3)
                temp3["fecha_alta_2"] = series_temp3
                temp4.append(temp3)

            if not temp4:
                all_data = pd.DataFrame({"fecha_alta": [], "index": [], "numero": []})
            else:
                all_data = pd.concat(temp4, ignore_index=True)

            all_data = all_data[all_data["index"].apply(lambda x: int(x)) >= rango_tiempo[0]]
            all_data = all_data[all_data["index"].apply(lambda x: int(x)) <= rango_tiempo[1]]
            fig1 = px.line(all_data, x="index", y="fecha_alta", color="numero", markers=True,
                           labels={"index": "Año", "fecha_alta": "Número de comercios nuevos", "numero": "Área"},
                           title="Registros nuevos por año")
            fig1.update_traces(showlegend=False)
            graph1 = dcc.Graph(figure=fig1)
            fig2 = px.line(all_data, x="index", y="fecha_alta_2", color="numero", markers=True,
                           labels={"index": "Año", "fecha_alta_2": "Número de comercios totales", "numero": "Área"},
                           title="Registros progresivos")
            graph2 = dcc.Graph(figure=fig2)
            all_data = all_data[all_data["index"] == int(rango_tiempo[1])]
            fig3 = px.pie(all_data, values="fecha_alta_2", names="numero", title="Registros al final del periodo",
                          labels={"numero": "Área", "fecha_alta_2": "Número de comercios totales"})
            fig3.update_traces(showlegend=False)
            graph3 = dcc.Graph(figure=fig3)
            return graph2, graph1, graph3