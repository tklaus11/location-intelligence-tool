import streamlit as st

st.title("Location Intelligence Tool V1")
st.write("Welcome to the prototype of the location intelligence tool. Use this app to explore demographic, traffic, and competitor data layers.")

import streamlit as st
import pydeck as pdk
import pandas as pd

import streamlit as st
import pydeck as pdk
import pandas as pd

# Title and description
st.title("Location Intelligence Tool V1")
st.write("Explore demographics, traffic, and competitor data layers on this interactive map.")

# Placeholder: Replace these with actual data sources
# Example competitor data
competitor_data = pd.DataFrame({
    "latitude": [51.0447, 53.5461, 52.2681, 50.4452],
    "longitude": [-114.0719, -113.4938, -113.8112, -104.6189],
    "name": ["Competitor A", "Competitor B", "Competitor C", "Competitor D"],
    "type": ["Grocery", "Gas", "Liquor", "Grocery"],
})

# Example demographics data
demographics_data = pd.DataFrame({
    "latitude": [51.05, 53.55, 52.27, 50.45],
    "longitude": [-114.07, -113.49, -113.81, -104.62],
    "population_density": [3000, 2500, 4000, 2000],  # Example population density
})

# Example traffic data
traffic_data = pd.DataFrame({
    "latitude": [51.04, 53.54, 52.26],
    "longitude": [-114.06, -113.48, -113.80],
    "traffic_volume": [20000, 15000, 18000],  # Example traffic volume
})

# Competitor layer
competitor_layer = pdk.Layer(
    "ScatterplotLayer",
    data=competitor_data,
    get_position=["longitude", "latitude"],
    get_radius=1000,
    get_fill_color=[255, 0, 0],  # Red color for competitors
    pickable=True,
)

# Demographics layer (heatmap for population density)
demographics_layer = pdk.Layer(
    "HeatmapLayer",
    data=demographics_data,
    get_position=["longitude", "latitude"],
    get_weight="population_density",
    radius_pixels=50,
)

# Traffic layer (circle markers for traffic volume)
traffic_layer = pdk.Layer(
    "ScatterplotLayer",
    data=traffic_data,
    get_position=["longitude", "latitude"],
    get_radius="traffic_volume",  # Scale radius by traffic volume
    get_fill_color=[0, 0, 255],  # Blue color for traffic
    pickable=True,
)

# Set up the map view
view_state = pdk.ViewState(
    latitude=51.0447,  # Center of Alberta for this example
    longitude=-114.0719,
    zoom=6,
    pitch=0,
)

# Sidebar for layer selection
st.sidebar.title("Map Layers")
show_competitors = st.sidebar.checkbox("Show Competitors", value=True)
show_demographics = st.sidebar.checkbox("Show Demographics", value=True)
show_traffic = st.sidebar.checkbox("Show Traffic", value=True)

# Add selected layers to the map
layers = []
if show_competitors:
    layers.append(competitor_layer)
if show_demographics:
    layers.append(demographics_layer)
if show_traffic:
    layers.append(traffic_layer)

# Render the map with the selected layers
st.pydeck_chart(pdk.Deck(
    initial_view_state=view_state,
    layers=layers,
))

# Optional: Display raw data for each layer
if st.sidebar.checkbox("Show Raw Data"):
    st.write("Competitor Data:", competitor_data)
    st.write("Demographics Data:", demographics_data)
    st.write("Traffic Data:", traffic_data)


st.map()
