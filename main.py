import streamlit as st
import folium
from streamlit_folium import st_folium
import spacy
import pandas as pd
from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent="locator")
nlp_ner = spacy.load("model-last")


def plot_places(place_list):
    locations = pd.DataFrame(place_list, columns=["Location"])
    locations["coordinates"] = locations["Location"].apply(geocoder.geocode)
    locations["Latitude"] = locations["coordinates"].apply(lambda x: x.latitude)
    locations["Longitude"] = locations["coordinates"].apply(lambda x: x.longitude)
    loc_list = locations[["Location", "Latitude", "Longitude"]].values.tolist()
    #print(loc_list)

    # Update the map with new markers
    # m is the folium map object created in streamlit
    # for l in loc_list:
    #     folium.Marker([l[1], l[2]], popup=l[0], tooltip=l[0]).add_to(m)
    # call to render the Folium map in streamlit
    # st_data = st_folium(m, width=725)
    return loc_list


def get_place_list(text):
    doc = nlp_ner(text)
    loc_entities = [ent.text for ent in doc.ents]
    return loc_entities

def read_text_file(file):
    content = ""
    if file.type == "text/plain":
        content = file.read().decode("utf-8")
    return content

def main():
    st.title("Text-based Geolocation Extraction System")

    perm_loc = []

    # Sidebar options
    option = st.sidebar.radio("Select Option", ["Type your own Text", "Drop your text file"])

    if option == "Type your own Text":
        st.subheader("Type your own Text:")
        user_content = st.text_area("Enter Text")
        if(user_content is not ""):
            if st.button('Find!'):
                place_list = get_place_list(user_content)
                loc_list = plot_places(place_list)
                for item in loc_list:
                    perm_loc.append(item)
                # st.write(user_content)
        

    elif option == "Drop your text file":
        st.subheader("Drop your text file:")
        uploaded_file = st.file_uploader("Upload a .txt file", type=["txt", "doc"])

        if uploaded_file is not None:
            content = read_text_file(uploaded_file)

            st.subheader("Uploaded Text Content:")
            if st.button('Find!'):
                function()
            user_content= st.text_area("Content", content)

        else:
            st.info("Please upload your text file.")

    st.write(perm_loc)
    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    for l in perm_loc:
        st.write(l)
        folium.Marker([l[1], l[2]], popup=l[0], tooltip=l[0]).add_to(m)

    #folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
    st_folium(m,width= 725)
    # folium_static(m)





if __name__ == "__main__":
    main()
