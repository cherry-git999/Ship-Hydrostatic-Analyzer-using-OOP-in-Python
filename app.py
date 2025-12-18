import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ship import Ship
from analyzer import HydroAnalyzer

st.set_page_config(page_title="Ship Hydro Analyzer", layout="centered")

st.title("🚢 Ship Hydro Analyzer")
st.write("Upload a CSV file to analyze ship hydrostatic stability")

# CSV upload
uploaded_file = st.file_uploader(
    "Upload CSV (Name, Length, Breadth, Depth, Draft, Mass, Floats)",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("CSV file loaded successfully ✅")
    st.dataframe(df)

    for _, row in df.iterrows():
        ship = Ship(
            name=row["Name"],
            length=row["Length"],
            breadth=row["Breadth"],
            depth=row["Depth"],
            draft=row["Draft"],
            mass=row["Mass"]
        )

        analyzer = HydroAnalyzer(ship)

        st.subheader(f"📌 Ship: {ship.name}")

        st.write(f"**Displacement:** {analyzer.displacement():.2f} tonnes")
        st.write(f"**Buoyant Force:** {analyzer.buoyant_force():.2f} kN")
        st.write(f"**Block Coefficient:** {analyzer.block_coefficient():.3f}")
        st.write(f"**Float Condition:** {'✅ Floating' if analyzer.is_floating() else '❌ Sinking'}")

        # GZ Curve
        angles, gz = analyzer.gz_curve()

        fig, ax = plt.subplots()
        ax.plot(angles, gz)
        ax.set_xlabel("Heel Angle (degrees)")
        ax.set_ylabel("GZ (m)")
        ax.set_title(f"GZ Curve - {ship.name}")
        ax.grid(True)

        st.pyplot(fig)
