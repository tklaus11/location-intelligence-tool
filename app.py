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
latitude,longitude,name,type
51.0447,-114.0719,Real Canadian Superstore,Grocery
53.5461,-113.4938,Shell Edmonton,Gas
52.2681,-113.8112,Liquor Depot,Liquor
50.4452,-104.6189,Sobeys Regina,Grocery
53.6305,-113.3239,Petro-Canada Calgary,Gas
53.9333,-116.5765,Costco Jasper,Grocery
49.2827,-123.1207,Save-On-Foods Vancouver,Grocery
55.1667,-118.7866,Walmart Grande Prairie,Grocery
51.0486,-114.0716,No Frills Calgary,Grocery
51.1622,-114.0773,7-Eleven Edmonton,Convenience

# Example demographics data
latitude,longitude,population_density_2016,population_density_2021,median_income,growth_rate
51.05,-114.07,4000,4200,85000,5.0
53.55,-113.49,3500,3700,80000,5.7
52.27,-113.81,5000,5200,95000,4.0
50.45,-104.62,2500,2600,75000,3.5
53.63,-113.32,2000,2100,70000,5.0
53.93,-116.58,4500,4600,88000,2.0
49.28,-123.12,5400,5800,90000,7.4
55.17,-118.78,1800,1900,70000,6.1
51.04,-114.07,4600,4700,85000,4.8
52.32,-113.52,3900,4000,83000,4.3

# Example traffic data
latitude,longitude,traffic_volume,road_name
51.04,-114.06,25000,Deerfoot Trail
53.54,-113.48,20000,Anthony Henday Drive
52.26,-113.80,23000,Highway 2A
50.44,-104.61,17000,Ring Road
53.63,-113.32,30000,Crowchild Trail
53.93,-116.57,22000,Yellowhead Highway
49.28,-123.11,40000,Granville St
55.17,-118.78,15000,Highway 43
51.05,-114.07,26000,Stoney Trail
52.15,-113.65,18000,Whitemud Drive


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
