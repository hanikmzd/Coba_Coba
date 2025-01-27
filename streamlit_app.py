import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# 1. Upload dan Load Data
st.title("Visualisasi Data E-Commerce")
uploaded_file = st.file_uploader('Dashboard/Data.csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # 2. Tampilkan Dataframe
    st.write("Data Preview:")
    st.dataframe(data)

    # 3. Analisis Deskriptif
    st.subheader("Descriptive Statistics")
    st.write(data.describe())

    # 4. Visualisasi
    st.subheader("Visualisasi Data")

    # Contoh Bar Chart
    column_to_visualize = st.selectbox("Pilih kolom untuk visualisasi (Bar Chart):", data.columns)
    if column_to_visualize:
        chart_data = data[column_to_visualize].value_counts()
        st.bar_chart(chart_data)

    # Contoh Histogram
    column_for_histogram = st.selectbox("Pilih kolom untuk visualisasi (Histogram):", data.select_dtypes(include='number').columns)
    if column_for_histogram:
        fig, ax = plt.subplots()
        sns.histplot(data[column_for_histogram], kde=True, ax=ax)
        st.pyplot(fig)
