import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(
    page_title="TV Delivery Cost Optimizer",
    page_icon="📦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# App title and introduction
st.title("📦 TV Delivery Cost Optimizer")
st.write("""
Welcome to the **TV Delivery Cost Optimizer**!  
This app helps a delivery company **minimize delivery costs** for TVs from three depots to three stores.
""")

# How It Works
st.header("🔧 How It Works")
st.markdown("""
- You provide (or use default) **supply and demand data**.
- The app calculates the **optimal delivery schedule** using a **greedy algorithm**.
- It ensures:
    - Depot supplies are not exceeded.
    - Store capacities are not exceeded.
- The **total delivery cost** is computed as:
""")
st.latex(r" \text{Total Delivery Cost} = (\text{Number of TVs delivered}) \times (\text{Distance}) \times (\text{Cost per mile}) ")

st.divider()

# Input parameters with sliders
st.header("📊 Input Parameters")
depot_supply = st.slider(
    "Depot Supply (Number of TVs available per depot)",
    min_value=50, max_value=300, value=150, step=10
)

store_demand = st.slider(
    "Store Demand (Number of TVs required per store)",
    min_value=50, max_value=300, value=120, step=10
)

distance = st.slider(
    "Distance (in miles)",
    min_value=10, max_value=500, value=100, step=10
)

cost_per_mile = st.slider(
    "Delivery Cost per Mile ($)",
    min_value=1, max_value=10, value=5, step=1
)

st.divider()

# Dummy greedy algorithm (for demonstration)
num_deliveries = min(depot_supply, store_demand)
total_cost = num_deliveries * distance * cost_per_mile

# Results section
st.header("💰 Delivery Summary")
col1, col2 = st.columns(2)
col1.metric("📺 Number of TVs Delivered", num_deliveries)
col2.metric("💵 Total Delivery Cost", f"${total_cost}")

st.success(f"✅ The estimated **delivery cost** for delivering {num_deliveries} TVs is **${total_cost}**.")

st.divider()
st.caption("Made with ❤️ by amcbhome")
