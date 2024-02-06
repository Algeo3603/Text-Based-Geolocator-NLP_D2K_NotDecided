import folium
import pandas as pd
from geopy.geocoders import Nominatim
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm



geocoder = Nominatim(user_agent="locator")

# map=folium.Map(location=[0, 0],zoom_start=2)
# fg=folium.FeatureGroup(name="locator")

def plot_places(place_list):
    locations= pd.DataFrame(place_list)
    locations.columns=["Location"]
    locations["coordinates"]=locations["Location"].apply(geocoder.geocode)
    locations["Latitude"]=locations["coordinates"].apply(lambda x:x.latitude)
    locations["Longitude"]=locations["coordinates"].apply(lambda x:x.longitude)
    loc_list = locations[["Location", "Latitude", "Longitude"]].values.tolist()

    print(loc_list)

    # Update the map with new markers
    # m is the folium map object created in streamlit
    for l in loc_list:
        folium.Marker([l[1], l[2]], popup=l[0], tooltip=l[0]).add_to(m)
    # call to render the Folium map in streamlit
    # st_data = st_folium(m, width=725)

place_list = ["Mumbai", "Delhi"]
plot_places(place_list)

