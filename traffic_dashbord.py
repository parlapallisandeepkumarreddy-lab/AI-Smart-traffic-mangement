import streamlit as st

st.set_page_config(
    page_title="AI Smart Traffic Management",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 AI Smart Traffic Management")
st.subheader("Four-Way Smart Traffic Junction")

st.success("Dashboard is running successfully!")

st.write("Enter vehicle counts for each road.")

north = st.number_input("North Road", min_value=0, value=12)
south = st.number_input("South Road", min_value=0, value=4)
east = st.number_input("East Road", min_value=0, value=8)
west = st.number_input("West Road", min_value=0, value=2)

traffic = {
    "North": north,
    "South": south,
    "East": east,
    "West": west
}

priority = max(traffic, key=traffic.get)

st.metric("Total Vehicles", sum(traffic.values()))

st.bar_chart(traffic)

st.success(f"Highest traffic: {priority} Road")

st.info("Next: Connect YOLO AI vehicle detection.")