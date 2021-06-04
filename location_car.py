from folium.map import Tooltip
from pyroutelib3 import Router
import folium
import webbrowser
c= folium.Map(location=[43.53520, 6.47070],zoom_start=10)
tooltip="Afficher véhicule"
folium.Marker([43.53520, 6.47070] , popup="150Tu2015" ,tooltip=tooltip, color="#9933ff").add_to(c)
folium.Marker([43.47187, 6.54500] , popup="148Tu546", tooltip=tooltip, color="9933ff").add_to(c)
folium.Marker([45.78647100671141, 5.65744181208053] , popup="78Tu2154" ,tooltip=tooltip, color="#9933ff").add_to(c)
folium.Marker([46.20755872093024, 5.65991651162791] , popup="96Tn2450", tooltip=tooltip, color="9933ff").add_to(c)
folium.Marker([46.00481852941176, 5.50401754901961] , popup="148Tu2015" ,tooltip=tooltip, color="#9933ff").add_to(c)
folium.Marker([46.47556610169492, 4.96954813559322] , popup="17Tu2015", tooltip=tooltip, color="9933ff").add_to(c)
folium.CircleMarker([43.53520, 6.47070] , popup="150Tu2015" ,tooltip=tooltip, color="#3186cc",
    fill=True,
    fill_color="#3186cc",).add_to(c)
folium.CircleMarker([43.47187, 6.54500] , popup="148Tu546", tooltip=tooltip, color="#3186cc",
    fill=True,
    fill_color="#3186cc",).add_to(c)
folium.CircleMarker([45.78647100671141, 5.65744181208053] , popup="78Tu2154" ,tooltip=tooltip, color="#3186cc",
    fill=True,
    fill_color="#3186cc",).add_to(c)
folium.CircleMarker([46.20755872093024, 5.65991651162791] , popup="96Tn2450", tooltip=tooltip, color="#3186cc",
    fill=True,
    fill_color="#3186cc",).add_to(c)
folium.CircleMarker([46.00481852941176, 5.50401754901961] , popup="148Tu2015" ,tooltip=tooltip, color="#3186cc",
    fill=True,
    fill_color="#3186cc",).add_to(c)
folium.CircleMarker([46.47556610169492, 4.96954813559322] , popup="17Tu2015", tooltip=tooltip, color="#3186cc",
    fill=True,
    fill_color="#3186cc",).add_to(c)
c.save('location_2.html')
webbrowser.open('location_2.html')