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


excel_file = 'test2.xlsx'
sheet_name = 'DATA'

#! ---- GLOBAL VARIABLES ----
# columns
g_col_assigned = 'Assigned'
g_col_time = 'Time'

# Main data frame
main_df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='B:L',
                    header=1)
# Converting Date Time into Date
main_df['Contract Date'] = pd.to_datetime(main_df['Contract Date']).dt.date
main_df['Draft Deadline'] = pd.to_datetime(main_df['Draft Deadline']).dt.date
main_df['Actual'] = pd.to_datetime(main_df['Actual']).dt.date
main_df = main_df


st.subheader('TEST2.XLSX')
st.dataframe(main_df)

# TODO : Move this to it's own module
#? chart-1 : Total-projects volume by Modeler
# ---- Selection Box ----
chart1_df = main_df
modelers = chart1_df['Assigned'].unique().tolist()

# data frame for the pie chart
chart1_df = chart1_df['Assigned'].value_counts().to_frame('count').rename_axis('Assigned').reset_index()

# plotly pie chart
chart_1 = px.pie(chart1_df,
                title='Total-Projects volume by Modeler',
                names='Assigned',
                values= 'count',
                labels={'':'Modeler','Assigned':'Assigned Projects'},
                # color_discrete_map= {'R.Arias': 'lightcyan'},
                # color_discrete_sequence=px.colors.sequential.Cividis
                )

# Pie chart customization
chart_1.update_traces(
    textposition='inside',
    textinfo='percent+label+value'
)

chart_1.update_layout(
    title_font_size = 28,
    font_size = 14,
)

st.plotly_chart(chart_1)


#? Chart-2 : Drafring Times by Modeler
# ---- Selection Box ----
chart2_df = df





# df_2.shape
# mask_modelers = df['Assigned'].isin(modelers_selection)
# df[mask_modelers].head()

