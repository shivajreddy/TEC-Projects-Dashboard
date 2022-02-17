from distutils.command.config import config
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from PIL import Image
import datetime

st.set_page_config(
    page_title='Eagle Projects Dashboard',
    layout="wide",
    page_icon='assets/images/fav.png',
)

st.header('Eagle Projects Dashboard')
st.subheader('Lot Specifics')

# Load Dataframe
sheet_name = 'Lot Specifics'
excel_file = 'tectest.xlsx'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='B:K',
                    converters={'Lot #':str, 'Contract Date':str,'Actual':str},
                    header=1)

# df['Contract Date'] = pd.to_datetime(df['Contract Date'])
# df['Contract Date'] = 'WTF'

# for k in df.keys():
#     st.info(k)
#     st.info(type(k))


# df['Contract Date'] = pd.to_datetime(df['Contract Date'])

excel_file = 'test2.xlsx'
sheet_name = 'DATA'
df_2 = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='B:L',
                    header=1)

# Converting Date Time into Date
df_2['Contract Date'] = pd.to_datetime(df_2['Contract Date']).dt.date
df_2['Draft Deadline'] = pd.to_datetime(df_2['Draft Deadline']).dt.date
df_2['Actual'] = pd.to_datetime(df_2['Actual']).dt.date

st.dataframe(df)
st.subheader('TEST2.XLSX')
st.dataframe(df_2)

modeler = df_2['Assigned'].unique().tolist()
times = df_2['Time'].tolist()

# st.write(s)
