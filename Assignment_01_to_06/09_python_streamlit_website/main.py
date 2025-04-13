import streamlit as st
import pandas as pd

# import matplotlib.pyplot as plt

# Set up Streamlit app
st.set_page_config(page_title="Data Dashboard")

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        if x_column == y_column:
            st.warning("X and Y columns must be different for plotting.")
        elif not pd.api.types.is_numeric_dtype(filtered_df[y_column]):
            st.warning("Y-axis column must be numeric.")
        else:
            chart_data = filtered_df[[x_column, y_column]].dropna()
            chart_data = chart_data.sort_values(
                by=x_column
            )  # Optional: for better plotting
            st.line_chart(data=chart_data, x=x_column, y=y_column)

else:
    st.write("Waiting on file upload...")
