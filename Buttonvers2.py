import streamlit as st
import sqlite3
import pandas as pd

# Function to retrieve data from the database and store it in a DataFrame
def get_data_from_db():
    conn = sqlite3.connect('PeriodTracker-1.db')
    query = "SELECT District FROM regionInfo"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Function to retrieve towns based on the selected district
def get_towns(selected_district):
    conn = sqlite3.connect('PeriodTracker-1.db')
    query = f"SELECT Name FROM regionInfo WHERE District='{selected_district}'"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df['Name'].unique()

# Main Streamlit app code
def Button():
    st.title("Region Table")
    
    # Retrieve data from the database and store it in a DataFrame
    df = get_data_from_db()

    # Get unique districts from the DataFrame
    unique_districts = df['District'].unique()

    # Select the district using a dropdown
    selected_district = st.selectbox('Select a district', unique_districts)

    # Get the towns based on the selected district
    towns = get_towns(selected_district)

    # Select the town using a second dropdown
    selected_town = st.selectbox('Select a town', towns)

    # Display the selected district and town
    st.write("Selected District:", selected_district)
    st.write("Selected Town:", selected_town)

Button()
