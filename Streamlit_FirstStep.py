import streamlit as st
import pandas as pd
from PIL import Image

feederwatch  = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-10/PFW_2021_public.csv")
site_data = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-10/PFW_count_site_data_public_2021.csv")

#dodawanie ikony do nazwy stronyw przeglądarce
im = Image.open('signpost.png')

#określenie spozosbu przentacj danych w apce by było szeroko
st.set_page_config(
  layout="wide",
  page_title="PierwszeApkawStreamlit",
  page_icon=im)


#ukrywanie opcji z górnego prawego rogu i 
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


st.title("Mój pierwsza apka w streamlit")

#tutaj musimy znaleśc rozwiązania na tworzenie bocznego paska na kilka filtrów lub informacji
with st.sidebar:
  st.button("Weś nie pytaj weś klikaj")
  radio = st.radio("Wybierz Rok"
           , options=[2020, 2021]
           , horizontal= True)
  
#left, right = st.columns(2,1)

#tabele pod spodem 
feederwatch.filter(
    items=["Year"
           , "Month"
           , "Day"
           , "entry_technique"
           , "how_many"
           , "valid"
           , "reviewed"
           , "Data_Entry_Method"])

if radio == 2021:
  st.dataframe(feederwatch.query('Year == 2021'))
else:
  st.dataframe(feederwatch.query('Year == 2020'))