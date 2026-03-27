import streamlit as st
import io
import pandas as pd


def workloop(df):
    st.divider()
    st.header("Our Cleaning Tools")
    if st.checkbox("1.Do you want to fill none or any word in the empty cells"):
         option=st.radio(
             "Select the following You want to perform"
            ,["Replace with \"None\"", "Replace with \"0\"","Replace with a specific word"]
             )
         if option=="Replace with \"None\"":
             df=df.fillna("None")
             st.write("Here is the representation of your csv",df.head())
         elif option=="Replace with \"0\"":
             df=df.fillna("0")
             st.write("Here is the representation of your csv",df.head())
         elif option=="Replace with a specific word":
             customvalue=st.text_input("Enter the custom value you want to enter")
             df=df.fillna(customvalue)
             st.write("Here is the representation of your csv",df.head())
    if st.checkbox("2.Do you want to drop Empty Rows"):
        initialrows=len(df)
        df=df.dropna()
        # afterdropcolumns=len(df.columns)
        rowsscount=initialrows-len(df)
        st.write(f"*Done {rowsscount} rows has been removed.*",df.head())
    if st.checkbox("3.Do you want to remove duplicates"):
        initialrows=len(df)
        df=df.drop_duplicates()
        # afterdropcolumns=len(df.columns)
        rowsscount=initialrows-len(df)
        st.write(f"*Done {rowsscount} Duplicate rows has been removed.*",df.head())
    if st.checkbox("4. Delete Specific Columns"):
        cols_to_delete = st.multiselect("Select columns to remove", df.columns)
        if cols_to_delete:
            df = df.drop(columns=cols_to_delete)
            st.warning(f"Deleted: {', '.join(cols_to_delete)}")
            st.dataframe(df.head())

            
        
        

             
    return df
        




def main():
    st.title("CSV Cleaner")
    uploaded=st.file_uploader("Welcome To Further Proceed the Cleaning",type="csv")
    if uploaded is not None:
        df=pd.read_csv(uploaded,on_bad_lines="skip",engine="python")
        st.write("File loaded sucessfully.(corrupted rows skipped)")
        st.write("Here is your Uploaded file",df.head(15))
        st.text(f"Total Size of your csv for rows is {df.shape[0]} and for columns is {df.shape[1]}")
        if st.checkbox("if your Csv is correct click the checkbox and we shall proceed"):
         cleanedcsv=workloop(df)

        




if __name__ == "__main__":
    main()