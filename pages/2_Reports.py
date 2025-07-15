import streamlit as st
import pandas as pd
df=pd.DataFrame({'Team':['A','B','C'],
                 'Score':[80,90,85]})
st.title('This is the reports page')
st.dataframe(df)