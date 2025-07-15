import streamlit as st
import pandas as pd
import plotly.express as px
df=pd.DataFrame({'Month':['Jan','Feb','Mar'],
                 'Sales':[100,150,130]})
st.title('This is the Charts PAGE')
fig=px.line(df,x='Month',y='Sales',title='Monthly Sales')
st.plotly_chart(fig)