# Imoprting necessary libraries
import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime

# Streamlit App Interface
st.write("""
# Simple Stock Price App

Shown are the stock **closing prices** and **volume prices** of **Apple**.
         """)

company_name = "Apple"

# ticker symbol of Apple
ticker_symbol = "AAPL"
# Fetching data for the ticker symbol using yfinance
ticker_data = yf.Ticker(ticker_symbol)

# Creating date input widgets for selecting the start and end date 
start_date = st.date_input("Start Date", value=datetime(2015,5,31))
end_date = st.date_input("End Date", value=datetime(2022,5,31))

# Ensure that start date is before end date
if start_date < end_date:
    # Convert the dates to string format for yfinance
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Get the stock history based on selected date range
    ticker_df = ticker_data.history(period='1d', start=start_date_str, end=end_date_str)

    if not ticker_df.empty:
        # Displaying the stock closing price chart
        st.write("""
            Closing Price
                 """)
        st.line_chart(ticker_df.Close)
        
        st.write("""
            Volume Price
                 """)
        
        # Displaying the stock volume chart
        st.line_chart(ticker_df.Volume)
    else:
        st.write(f"No data found for {company_name}. Please try another date range.")
else:
    st.write("Start date must be before end date.")

