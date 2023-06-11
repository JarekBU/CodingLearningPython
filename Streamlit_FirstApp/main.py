import streamlit as st
import pandas as pd
from PIL import Image


#dodawanie ikony do nazwy stronyw przeglądarce
im = Image.open('signpost.png')

#określenie spozosbu przentacj danych w apce by było szeroko
st.set_page_config(
  layout="wide",
  page_title="PierwszeApkawStreamlit",
  page_icon=im)

###############################################################################################################################################
#ukrywanie opcji z górnego prawego rogu i 
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

#cashpwanie danych w prosty sposób czyli poprzes stowrzenie funkcji
@st.cache_data
def load_data(url):
  df = pd.read_csv(url)
  return df

feederwatch  = load_data("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-10/PFW_2021_public.csv")


st.title("Mój pierwsza apka w streamlit")

#############################################################################################################################################
#tutaj musimy znaleśc rozwiązania na tworzenie bocznego paska na kilka filtrów lub informacji
with st.sidebar:
  st.button("Weś nie pytaj weś klikaj")
  radio = st.radio("Wybierz Rok"
           , options=[2020, 2021]
           , horizontal= True)



############################################################################################################################################
feederwatch = feederwatch.fillna(0)

############################################################################################################################################

left, right = st.columns(2)

with left:
  st.bar_chart(feederwatch, x='species_code', y='how_many', use_container_width=True)

with right:
  st.line_chart(feederwatch, x='Month', y='how_many', use_container_width=True) 


#tabele pod spodem 
if radio == 2021:
  st.dataframe(feederwatch.query('Year == 2021'))
else:
  st.dataframe(feederwatch.query('Year == 2020'))