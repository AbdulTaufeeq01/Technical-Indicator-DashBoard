import streamlit as st
import pandas as pd
from datetime import date
import yfinance as yf
 
def export_data_to_csv(df:pd.DataFrame,filename:str):
    """
    Exports a DataFrame to a CSV file.
    Lets the user download the file after the techical indicators are calculated.
    Args:
        df (pd.DataFrame): The DataFrame to export.
        filename (str): The name of the file to save as.
    """
    csv=df.to_csv(index=True).encode('utf-8')
    """
    .to_csv() converts the DataFrame to a CSV string.
    index=True includes the date index in the CSV.
    .encode('utf-8') encodes the string to bytes as a downloadablte file.
    """
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=filename,
        mime='text/csv'
    )
    """
    st.download_button → Streamlit's built-in widget to let users download files.
    label → The button's visible text.
    data → The binary data we prepared above.
    file_name → What the downloaded file will be called.
    mime='text/csv' → Tells the browser this is a CSV file.
    """
    def validate_parameters(ticker:str, start_date:date, end_date:date)-> bool:
        """
        Validates the input parameters for the stock data retrieval.
        Ensures that the ticker is not empty and that the start date is before the end date.
        
        Args:
            ticker (str): The stock ticker symbol.
            start_date (date): The start date for the data retrieval.
            end_date (date): The end date for the data retrieval.
        
        Returns:
            bool: True if parameters are valid, False otherwise.
        """
        if not ticker:
            st.error("Please enter a valid stock ticker.")
            return False
        if start_date >= end_date:
            st.error("Start date must be before end date.")
            return False
        return True 