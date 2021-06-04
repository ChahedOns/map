from folium.map import Tooltip
from pyroutelib3 import Router
import folium
import webbrowser
lat1=43.53520
lon1=6.47070
lat2=43.47187
lon2=6.54500
router = Router("car")
depart = router.findNode(lat1, lon1)
arrivee = router.findNode(lat2,  lon2)

status, route = router.doRoute(depart, arrivee)
if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route))
tooltip="Affiche destination"
c= folium.Map(location=[lat1, lon1],zoom_start=10)
folium.Marker([43.53520, 6.47070] , popup="Place de paix" ,tooltip=tooltip, color="#9933ff").add_to(c)
folium.Marker([43.47187, 6.54500] , popup="Rue Vaugerenier", tooltip=tooltip, color="9933ff").add_to(c)
for indice,coord in enumerate(routeLatLons):
    if indice%10==0:
        coord=list(coord)
        folium.CircleMarker(coord,radius = 3,fill=True, color='blue' ).add_to(c)
c.save('maCarte_2.html')
webbrowser.open('maCarte_2.html')