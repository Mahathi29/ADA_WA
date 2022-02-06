import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sb
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title='Data Analysis Web APP',
                   layout='wide')

st.sidebar.write("Hii welcome to the DA webapp👋🏻")
rad = st.sidebar.radio(
    "NAVIGATION BAR", ["ABOUT ME", "USE APP",])
# Upload CSV data

if rad == "ABOUT ME":
    # Web App Title
    st.markdown('''
    # **The Data Analysis Web App**

    Welcome to the Data Analysis web app!
    This web app makes Data Analysis Easy and helps in generating a Data Analysis report.

    #### ✨Developed By✨:
    - Name:- K. SAI MAHATHI 
    - Rollno:- 18671A1924 
    - Branch:- Department Of _Electronics and Computer Engineering_
    - College:- J.B Institute Of Engineering & Technology

    ### Instructions:
    1. Click on Use APP from navigation menu.
    2. Upload your Data Set.
    3. Lets get the Data Analysis Report!
    ## Diving into the App:
    ### 📌The Overview Panel: 
    The overview panel has 3 sections or tabs which u can activate them by toggling on them.

    1. The Overview Section:
    This column Tells gives you a basic overview of the data set!
    ![image](https://raw.githubusercontent.com/Mahathi29/ADA_WA/main/Data/Overview.1.png)
    
    2. Warnings Section:
    You can Find The important factors of variables here!
    ![image](https://raw.githubusercontent.com/Mahathi29/ADA_WA/main/Data/Overview.2.png)

    3. Reproduction Section:
    This Basically gives you an analysis about How much Duration it took to make the report, software names and its configurations, etc.,
    ![image](https://raw.githubusercontent.com/Mahathi29/ADA_WA/main/Data/Overview.3.png)

    ### 📌Variables Panel:
    In this section It Analyzes the data set and provide per variable analysis report for all the variables in the data set. It even plots histogram for all the variables.
    ![image](https://raw.githubusercontent.com/Mahathi29/ADA_WA/main/Data/Variables.1.png)
   
    ### 📌Correlation Panel:
    - This panel shows the correlation of the variables in the form of correleation matrix.
    - The correlation between two variables can be found by using Correlation coeefitients.
    - If the Variables doesnt have proper Correlation then the app doesnt show the tags of "High Correlation", In this case On seeing this report the Analyst should understand that proper correlation should be found out by doing necessary steps.
    ![image](https://raw.githubusercontent.com/Mahathi29/ADA_WA/main/Data/COR.1.png)

    ### 📌Missing Values Panel:
    To make things more easy, a missing value graph is displayed which visualizes the number of missing values in variables.
    ![image](https://raw.githubusercontent.com/Mahathi29/ADA_WA/main/Data/Missing_values.1.png)

    ## Features for Future Enhancement:
    ### 📌Data set run limit:
    - Currently this app can only support a dataset file runtime size of 50mb.
    - Using a dataset over the mentioned size might cause the app not to display features or generate the report properly.
    - Using a dataset over the mentioned size might cause the app not to run / function at all.
    - Anyone can contribute to this app by including memory size feature.
    ![image](https://raw.githubusercontent.com/Mahathi29/ADA_WA/main/Data/Data_limit_1.png)
    
    
    ### 📌Interactable Graph Panel:
    - If the Interaction Graphs are necessary then it prints out the Interaction graphs for the variables.
    - Anyone can contribute to this app by including this Interactable GRaph feature for all datasets if possible because Many people fancies such graphs as they can understand even more better through them! 
    
 
    ### 📌Data set Analysis time:
    - As the size of the data set increases, the Data Analysis time also increases.
    - Someone can contribute to this by using more effitient way of using the resources and generating reports.

    🟢 THANK YOU 🟢
    
  

    ''')
if rad == "USE APP":
    with st.sidebar.header('1. Upload your CSV data'):
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
        st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/Mahathi29/ADA_WA/main/Test_Data_sets/delaney_solubility_with_descriptors.csv)
    """)

    st.markdown('''
    ### 🚀 Upload Your Data Set, Grab a Cup of Coffee and Relax while The App generate the Data Analysis Report for you!



    ''')

   
# Data Analysis Report
    if uploaded_file is not None:
        @st.cache
        def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv
        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Data Analysis Report**')
        st_profile_report(pr)
    else:
        st.info('Awaiting for CSV file to be uploaded.')
        if st.button('Press to use Example Dataset'):
            # Example data
            @st.cache
            def load_data():
                a = pd.DataFrame(
                    np.random.rand(100, 5),
                    columns=['a', 'b', 'c', 'd', 'e']
                )
                return a
            df = load_data()
            pr = ProfileReport(df, explorative=True)
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
            st.header('**Data Analysis Report**')
            st_profile_report(pr)
