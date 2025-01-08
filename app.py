import streamlit as st

st.title("Location Intelligence Tool V1")
st.write("Welcome to the prototype of the location intelligence tool. Use this app to explore demographic, traffic, and competitor data layers.")

import streamlit as st
import pydeck as pdk
import pandas as pd

# Title and description
st.title("Location Intelligence Tool V1")
st.write("Explore demographics, traffic, and competitor data layers on this map.")

# Sample data: Replace this with your actual data sources
# Example for competitors
competitor_data = pd.DataFrame({
    "latitude": [51.0447, 53.5461, 50.4452],  # Example latitudes
    "longitude": [-114.0719, -113.4938, -104.6189],  # Example longitudes
    "name": ["Competitor A", "Competitor B", "Competitor C"],
})

# Create a Pydeck layer for competitors
competitor_layer = pdk.Layer(
    "ScatterplotLayer",
    data=competitor_data,
    get_position=["longitude", "latitude"],
    get_radius=1000,
    get_fill_color=[255, 0, 0],
    pickable=True,
)

# Set up the map view
view_state = pdk.ViewState(
    latitude=51.0447,  # Adjust for your region
    longitude=-114.0719,
    zoom=10,
    pitch=0,
)

# Render the map with layers
st.pydeck_chart(pdk.Deck(
    initial_view_state=view_state,
    layers=[competitor_layer],
))

# Display the data table
if st.checkbox("Show raw data"):
    st.write(competitor_data)

st.map()
