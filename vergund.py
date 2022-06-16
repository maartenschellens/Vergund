import os
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import date
from datetime import datetime

df_horeca = pd.read_csv(os.path.join(os.getcwd(), "testdf_horeca.csv"),
                delimiter=',').drop('Unnamed: 0', axis = 'columns')

st.set_page_config(
    page_title="Vergunde horeca Rotterdam",
     layout="wide")


st.title("Zoek op een horeca-adres om de vergunningen te bekijken")

straat_geselecteerd =  st.selectbox("Straatnaam", df_horeca['straat'].sort_values().unique())

huisnummer_geselecteerd = st.number_input('Huisnummer', 0)

if straat_geselecteerd:
    st.table(df_horeca[df_horeca['straat'] == straat_geselecteerd].drop(['straat', 'huisnr'], axis = 'columns').set_index('adres'))