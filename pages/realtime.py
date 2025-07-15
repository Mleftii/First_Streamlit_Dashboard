import streamlit as st
import pandas as pd

st.title("🔄 Upload & Filter Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Optional: Let user choose column to filter by
    filter_column = st.selectbox("Choose a column to filter", df.columns)

    # Automatically extract unique values for filtering
    filter_values = df[filter_column].dropna().unique()
    selected_value = st.selectbox(f"Filter {filter_column} by:", ['All'] + list(filter_values))

    # Apply the filter
    if selected_value != 'All':
        df = df[df[filter_column] == selected_value]

    st.subheader("Filtered Results")
    st.dataframe(df)

    # Download filtered data
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Filtered Data", data=csv, file_name="filtered_data.csv", mime="text/csv")
