import pandas as pd
from app import main_df
from app import g_col_assigned, g_col_time

testvart = 21
chart2_df = main_df
# chart2_df = chart2_df.value_counts(subset=['Assigned', 'Time'])
chart2_df = chart2_df.value_counts(subset=[g_col_assigned, 'Time'])

