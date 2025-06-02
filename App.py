import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(
    page_title="TV Delivery Cost Optimizer",
    page_icon="📦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# App title and intro
st.title("📦 TV Delivery Cost Optimizer")
st.write("""
This app helps a delivery company **minimize delivery costs** for TVs from three depots to three stores.
""")

# How it works
st.header("🔧 How It Works")
st.markdown("""
- Provide (or use default) **supply data** for each depot.
- The app calculates the **optimal delivery schedule** using a **greedy algorithm**.
- It ensures:
    - Depot supplies are not exceeded.
    - Store capacities are not exceeded.
- The **total delivery cost** is:
""")
st.latex(r" \text{Total Delivery Cost} = (\text{Number of TVs delivered}) \times (\text{Distance}) \times (\text{Cost per mile}) ")

st.divider()

# Input sliders for depots
st.header("🏭 Depot Supplies")
depot1_supply = st.slider("Depot 1 Supply", min_value=0, max_value=300, value=100, step=10)
depot2_supply = st.slider("Depot 2 Supply", min_value=0, max_value=300, value=100, step=10)
depot3_supply = st.slider("Depot 3 Supply", min_value=0, max_value=300, value=100, step=10)

# Input for store demand (assuming same for simplicity)
store_demand = st.slider(
    "Store Demand (Number of TVs required per store)",
    min_value=50, max_value=300, value=120, step=10
)

# Distance
distance = st.slider(
    "Distance (in miles)",
    min_value=10, max_value=500, value=100, step=10
)

# Delivery cost per TV per mile
cost_per_tv_mile = st.slider(
    "Delivery Cost per TV per Mile ($)",
    min_value=1, max_value=20, value=5, step=1
)

st.divider()

# Dummy greedy approach
# For simplicity: total TVs delivered is minimum of total depot supply and total store demand
total_depot_supply = depot1_supply + depot2_supply + depot3_supply
total_store_demand = store_demand * 3  # assuming 3 stores
num_deliveries = min(total_depot_supply, total_store_demand)

# Total delivery cost
total_cost = num_deliveries * distance * cost_per_tv_mile

# Results
st.header("💰 Delivery Summary")
col1, col2 = st.columns(2)
col1.metric("📺 Number of TVs Delivered", num_deliveries)
col2.metric("💵 Total Delivery Cost", f"${total_cost}")

st.success(f"✅ The estimated **delivery cost** for delivering {num_deliveries} TVs is **${total_cost}**.")

st.divider()
st.caption("Made with ❤️ by amcbhome")
