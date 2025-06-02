import streamlit as st

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

# Input sliders for depot supplies
st.header("🏭 Depot Supplies")
depot1_supply = st.slider("Depot 1 Supply", min_value=0, max_value=300, value=100, step=10)
depot2_supply = st.slider("Depot 2 Supply", min_value=0, max_value=300, value=100, step=10)
depot3_supply = st.slider("Depot 3 Supply", min_value=0, max_value=300, value=100, step=10)

# Calculate button
if st.button("Calculate Delivery Cost"):
    # Dummy values for store demand, distance, and cost per mile
    store_demand = 120 * 3  # assuming 3 stores
    distance = 100
    cost_per_tv_mile = 5

    total_depot_supply = depot1_supply + depot2_supply + depot3_supply
    num_deliveries = min(total_depot_supply, store_demand)

    # Total delivery cost
    total_cost = num_deliveries * distance * cost_per_tv_mile

    # Results
    st.header("💰 Delivery Summary")
    col1, col2 = st.columns(2)
    col1.metric("📺 Number of TVs Delivered", num_deliveries)
    col2.metric("💵 Total Delivery Cost", f"${total_cost}")
    
    st.success(f"✅ The estimated **delivery cost** for delivering {num_deliveries} TVs is **${total_cost}**.")
else:
    st.info("ℹ️ Adjust the sliders and click 'Calculate Delivery Cost' to see results.")

st.divider()
st.caption("Made with ❤️ by amcbhome")
