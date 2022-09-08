import plotly.express as px
import json

with open("georef-mexico-state-millesime.json") as geo_file:
    geo = json.load(geo_file)

