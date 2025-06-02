import streamlit as st

# Page setup
st.set_page_config(page_title="Alastair McBride - Portfolio", page_icon="📁", layout="centered")

# --- Header / Landing ---
st.title("👋 Alastair McBride")
st.subheader("Accounting Graduate | Data Enthusiast | Python Modeller")

st.markdown("""
Motivated accounting graduate with five years of quality assurance experience, a strong analytical mindset, and expertise in data analysis and Python-based modelling.  
Eager to contribute to a dynamic graduate scheme while progressing towards full ACCA qualification.
""")

# --- About Section ---
st.divider()
st.header("📌 About")
st.write("""
- 🎓 **BAcc (Hons) Accounts** – University of the West of Scotland (2021–2025)  
  - Dissertation: The AI boom and its effect on data analytic skills  
  - Project: Built a scalable scheduling model using linear programming in Python, accelerated with generative AI for code generation.  
  - ACCA Exemptions: BT, FA, MA, LW, TX, FR, PM, FM, AA  
- 💡 **Strong analytical mindset**  
- 🤝 **Collaborative team player**  
""")

# --- Portfolio Section ---
st.divider()
st.header("📂 Portfolio")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/300", caption="Project 1")
    st.write("Built a dynamic delivery cost optimizer with Streamlit & Python.")

with col2:
    st.image("https://via.placeholder.com/300", caption="Project 2")
    st.write("Automated financial data analysis using AI-powered RPA tools.")

with col3:
    st.image("https://via.placeholder.com/300", caption="Project 3")
    st.write("Visualized council budget performance using data dashboards.")

# --- CV Section ---
st.divider()
st.header("📄 CV / Resume")
st.write("""
- **Cleaner (2015–2025)** – Various employers including Brittania Services Group Ltd, Spectrum Facilities Maintenance, Atlas Cleaning Ltd, and more.  
- Experienced in cleaning services, first aid, key holding, health & safety awareness.
""")
st.write("📥 [Download CV (PDF)](https://github.com/your-username/your-repo/raw/main/assets/docs/CV%20(A.%20McBride%20Accountant).pdf)")

# --- Contact Info ---
st.divider()
st.header("📞 Contact")
st.write("""
- 📧 **Email:** [amcb.home@gmail.com](mailto:amcb.home@gmail.com)  
- 📱 **Phone:** 07895 770 953  
- 🌐 **LinkedIn:** [linkedin.com/in/alastairmcbride](https://www.linkedin.com/in/alastairmcbride/)  
""")

st.caption("Made with ❤️ by Alastair McBride")
