import folium
import pandas

d_volcanoes = pandas.read_csv("Volcanoes.txt")
lat = list(d_volcanoes["LAT"])
lon = list(d_volcanoes["LON"])
name = list(d_volcanoes["NAME"])
elev = list(d_volcanoes["ELEV"])

mapa = folium.Map(location=[lat[0], lon[0]], zoom_start=10, tiles="Stamen terrain", name="Map of Volcanoes")
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding="utf-8-sig").read(), style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] <= 20000000 else "darkred"}))


def set_color():
    if elev[i] > 1000 and elev[i] <= 3000:
        return "orange"
    elif elev[i] > 3000:
        return "red"
    else:
        return "green"

fgv = folium.FeatureGroup(name="Volcanoes")

for i in range(0, len(lat)):
    fgv.add_child(folium.CircleMarker(location=[lat[i], lon[i]], popup=name[i]+"\nElevation: "+str(elev[i]), radius=7, fill_color=set_color(), color="black", fill_opacity=0.6,
    weight=2, tooltip=name[i]))


mapa.add_child(fgp)
mapa.add_child(fgv)
mapa.add_child(folium.LayerControl())

mapa.save("us_volcanoes_map.html")

