import folium
import pandas

map1 = folium.Map(location=[-33.923969, 151.258030], zoom_start=6, tiles="Stamen terrain")

# JSON lists
data = pandas.read_json("sightsAUS.json")
coordinates = list(data["Coordinates"])
names = list(data["Name"])
country = list(data["Country"])
color = list(data["Color"])


# Icon setting
def icon_setter(icon_color):
    if icon_color == "green":
        return "info-sign"
    else:
        return "cloud"


fg = folium.FeatureGroup(name="My Map")
for coordinates, names, country, color in zip(coordinates, names, country, color):
    fg.add_child(folium.Marker(location=coordinates, popup=names + ",\n" + country,
                               icon=folium.Icon(color=color, icon=icon_setter(color))))

map1.add_child(fg)
map1.save("map.html")
