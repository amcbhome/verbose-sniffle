import streamlit as st
import pandas as pd

# App title and subtitle
st.set_page_config(page_title="TV Delivery Optimizer", page_icon="📦")
st.title("📦 TV Delivery Cost Optimizer")
st.markdown("""
Welcome to the **TV Delivery Cost Optimizer**!  
This app helps a delivery company **minimize delivery costs** for TVs from three depots to three stores.

### ⚙️ How It Works
- You provide (or use default) **supply data** for each depot.
- The app calculates the **optimal delivery schedule** using a **greedy algorithm**.
- It ensures that:
  - **Depot supplies are not exceeded**.
  - **Store capacities are not exceeded**.
- The total delivery cost is computed using the formula:

> 💰 **Total Delivery Cost** = (Number of TVs delivered) × (Distance in miles) × (Delivery cost per mile)

---

""")

# Explanation of distances and costs
st.header("🛣️ Distances and Costs")
st.markdown("""
| From Depot → To Store | S1 (miles) | S2 (miles) | S3 (miles) |
|------------------------|------------|------------|------------|
| **D1**                 | 22         | 33         | 40         |
| **D2**                 | 27         | 30         | 22         |
| **D3**                 | 36         | 20         | 25         |

- **Delivery cost per mile:** $5  
- **Store capacities:**  
  - **S1:** 2000 TVs  
  - **S2:** 3000 TVs  
  - **S3:** 2000 TVs
""", unsafe_allow_html=True)

# Default data
default_supply = {'D1': 2500, 'D2': 3100, 'D3': 1250}
demand = {'S1': 2000, 'S2': 3000, 'S3': 2000}
distance = pd.DataFrame({
    'S1': [22, 27, 36],
    'S2': [33, 30, 20],
    'S3': [40, 22, 25]
}, index=['D1', 'D2', 'D3'])
cost_per_mile = 5

# User inputs for supplies
st.header("🏭 Depot Supplies")
st.markdown("You can adjust the number of TVs available at each depot. Press **Enter** for default values.")
supply_d1 = st.number_input("Supply from Depot 1 (D1)", min_value=0, value=default_supply['D1'])
supply_d2 = st.number_input("Supply from Depot 2 (D2)", min_value=0, value=default_supply['D2'])
supply_d3 = st.number_input("Supply from Depot 3 (D3)", min_value=0, value=default_supply['D3'])

# Button to calculate
if st.button("🚀 Calculate Optimal Delivery Schedule"):
    # Use entered or default supplies
    supply = {'D1': supply_d1, 'D2': supply_d2, 'D3': supply_d3}

    # Initialize store and depot remaining capacity
    store_remaining = demand.copy()
    depot_remaining = supply.copy()

    # Create a list of (depot, store, distance) sorted by distance
    routes = [(depot, store, distance.loc[depot, store])
              for depot in supply for store in demand]
    routes.sort(key=lambda x: x[2])

    # Initialize delivery schedule
    delivery_schedule = pd.DataFrame(0, index=supply.keys(), columns=demand.keys())

    # Greedy allocation
    for depot, store, dist in routes:
        quantity = min(depot_remaining[depot], store_remaining[store])
        delivery_schedule.loc[depot, store] = quantity
        depot_remaining[depot] -= quantity
        store_remaining[store] -= quantity

    # Calculate total delivery cost
    total_cost = sum(delivery_schedule.loc[depot, store] *
                      distance.loc[depot, store] *
                      cost_per_mile
                      for depot in supply for store in demand)

    # Show results
    st.header("📊 Optimal Delivery Schedule")
    st.dataframe(delivery_schedule)

    st.success(f"💰 **Total delivery cost:** ${total_cost:,.2f}")

    # Option to download CSV
    csv = delivery_schedule.to_csv().encode()
    st.download_button(
        label="Download Delivery Schedule as CSV",
        data=csv,
        file_name='optimal_delivery_schedule.csv',
        mime='text/csv'
    )

    # Explanation
    st.info("""
✅ The schedule above ensures **no depot supply exceeds its limit** and **no store exceeds capacity**.  
✅ The **greedy algorithm** allocates deliveries to the **shortest available route** first.  
✅ This may not be perfectly optimal, but it’s a **practical and cost-effective** approximation.
""")

# Footer
st.markdown("""
---
👨‍💻 Created with ❤️ by [Your Name].  
🔗 [GitHub Repository](https://github.com/yourusername/tv-delivery-optimizer)
""")
