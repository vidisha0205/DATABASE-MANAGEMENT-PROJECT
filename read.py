import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data
def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Order ID', 'Customer Name', 'Plant Name','Pot Size', 'Price'])
    st.dataframe(df)
    with st.expander("Plants:"):
        plant_df = df['Plant Name'].value_counts().to_frame()
        plant_df = plant_df.reset_index()
        st.dataframe(plant_df)
        p1 = px.pie(plant_df, names='index', values='Plant Name')
        st.plotly_chart(p1)
