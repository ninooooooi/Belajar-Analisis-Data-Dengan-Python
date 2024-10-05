import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a Pandas DataFrame
data = pd.read_csv('dashboard/main_data.csv')

# Set the title of the Streamlit app
st.title('Dashboard Bike Sharing Dataset')

# Create tabs for different sections of the app
tab1, tab2, tab3 = st.tabs(['Data', 'Data Analysis 1', 'Data Analysis 2'])

# Tab 1: Display the raw data
with tab1:
    # Display the DataFrame in the Streamlit app
    st.write(data)

    # Calculate the total number of bike rentals
    total = data.cnt.sum()

    # Display a metric card for the total rentals
    st.metric("Total Rent", value=total)

# Tab 2: Day of Week Analysis
with tab2:
    # Create a new column for the day of the week from the 'dteday' column
    data['day_of_week'] = pd.to_datetime(data['dteday']).dt.dayofweek

    # Group data by day of the week and calculate average daily usage
    daily_usage_weekday = data.groupby('day_of_week')['cnt'].mean()

    # Define labels for the days of the week (Monday, Tuesday, etc.)
    days_of_week = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

    # Create a Matplotlib figure and axis for the plot
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create a bar chart showing average usage per day of the week
    ax.bar(days_of_week, daily_usage_weekday)

    # Set title, labels, and formatting for the plot
    ax.set_title('Differences in bicycle shared patterns between weekdays and weekends')
    ax.set_xlabel('Day in a week')
    ax.set_ylabel('Average Number of Bikes Borrowed')

    # Set the y-axis limits to slightly exceed the maximum value for better visualization
    ax.set_ylim(0, max(daily_usage_weekday) * 1.1)

    # Add grid lines on the y-axis
    ax.grid(axis='y')

    # Set the title for the plot in Streamlit
    st.title('Different patterns of bicycle use')

    # Improve layout to avoid overlapping elements (optional)
    plt.tight_layout()

    # Display the Matplotlib plot in Streamlit
    st.pyplot(fig)

# Tab 3: Monthly Usage Analysis
with tab3:
    # Calculate monthly usage by summing bike rentals for each day
    monthly_usage = data.groupby('dteday')['cnt'].sum()

    # Create a Matplotlib figure and axis for the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the monthly usage data with markers and lines
    ax.plot(monthly_usage.index, monthly_usage.values, marker='o', linestyle='-')

    # Set title, labels, and formatting for the plot
    ax.set_title('Monthly patterns of bicycle use')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Bikes shared')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)

    # Show only x-axis ticks every 30 days (to avoid overcrowding)
    ax.set_xticks(monthly_usage.index[::30])
    ax.set_xticklabels(monthly_usage.index[::30], rotation=45)

    # Set the title for the plot in Streamlit
    st.title('Monthly patterns of bicycle use')

    # Display the Matplotlib plot in Streamlit
    st.pyplot(fig)


# Add a copyright caption at the end
st.caption('copyright (c) Luthfi Pratama Fauzie 2024')
