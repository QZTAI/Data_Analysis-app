import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.set_page_config(page_title="Data Analysis App", layout="wide")
st.title("📊 Data Analysis Web App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📂 Dataset Preview")
    st.dataframe(df.head())

    # Show basic info
    st.subheader("📑 Dataset Information")
    st.write("Shape:", df.shape)
    st.write("Columns:", list(df.columns))

    # Summary stats
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    # Correlation heatmap
    st.subheader("🔗 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Column selection for plots
    st.subheader("📊 Visualizations")
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:
        col_x = st.selectbox("Select X-axis", numeric_cols)
        col_y = st.selectbox("Select Y-axis", numeric_cols)

        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x=col_x, y=col_y, ax=ax2)
        st.pyplot(fig2)

        st.bar_chart(df[numeric_cols])

    else:
        st.warning("No numeric columns available for plotting.")

else:
    st.info("👆 Upload a file to get started.")
