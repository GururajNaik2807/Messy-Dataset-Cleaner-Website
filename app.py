import streamlit as st
import pandas as pd
import sys
st.title("CSV Data Cleaner")
# 1. File Uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])


def workloop(df):
    if uploaded_file is not None:
    # Read the CSV
        df = pd.read_csv(uploaded_file)
        st.write("Original Data:", df.head())

    # 2. Cleaning Operations
        if st.checkbox("Remove Duplicates"):
            df = df.drop_duplicates()

        if st.checkbox("Fill Missing Values (with 0)"):
            df = df.fillna(0)
        
        if st.checkbox("Or Drop all Na"):
            df = df.dropna()
   
        if st.checkbox("Want to replace a particular field data with something?"):
            columnname=st.text_input("Enter the Field name here")
            Previous=st.text_input("Enter the Data You want to Replace")
            replaced=st.text_input("Enter what should it be replaced to")
            if columnname and Previous and replaced:
        
              df = df.replace({columnname:Previous},replaced,regex=True)
              print("done")


        if st.checkbox("want to remove any unwanted symbols from your data set"):
            if st.checkbox("Do you want to delete these from the whole dataset?"):
            # Replaces any pattern of [...] with an empty string across all columns
                 df = df.replace(to_replace=r'\[.*?\]', value='', regex=True)
            else:
                columnname=st.text_input("Please enter the columnname")
                if columnname in df.columns:
                     st.write("The Column Exists")
                # Replaces any pattern of [...] with an empty string across all columns
                     df[columnname] = df[columnname].replace(to_replace=r'\[.*?\]', value='', regex=True)
                else:
                    st.write("Sorry the column doesnt exists")






        
        





def main():
     st.title("CSV Data Cleaner")
    # 1. File Uploader
     uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
     if uploaded_file is not None:
     # Read the CSV
         df = pd.read_csv(uploaded_file)
         st.write("Original Data:", df.head())
         workloop()
    # 3. Show Cleaned Data
     st.write("Cleaned Data:", df.head(10))

    # 4. Download Cleaned File
     st.download_button(
         label="Download Cleaned CSV",
         data=df.to_csv(index=False).encode('utf-8'),
         file_name='cleaned_data.csv',
         mime='text/csv',
     )

