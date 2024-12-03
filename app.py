import streamlit as st
from datasets import load_dataset
import pandas as pd

# Load the SQuAD dataset
squad = load_dataset("squad")

# Title for the Streamlit App
st.title("Dataset Visualization")

# Sidebar to select dataset split
split = st.sidebar.selectbox("Select Dataset Split", squad.keys())

# Number of rows to display
num_rows = st.sidebar.slider("Number of Rows to Display", 1, 50, 10)

# Convert the selected split to a pandas DataFrame
data = squad[split].to_pandas()

# Display the dataset in a table format
st.subheader(f"{split.capitalize()} Split - First {num_rows} Rows")
st.dataframe(data.head(num_rows))

# Display column information
if st.sidebar.checkbox("Show Dataset Columns"):
    st.subheader("Dataset Columns")
    st.write(data.columns.tolist())

# Option to search by a specific question
if st.sidebar.checkbox("Search by Question"):
    search_query = st.text_input("Enter a question or keyword to search:")
    if search_query:
        filtered_data = data[data['question'].str.contains(search_query, case=False, na=False)]
        st.subheader(f"Search Results for: '{search_query}'")
        st.dataframe(filtered_data)
