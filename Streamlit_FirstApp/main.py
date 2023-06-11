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
  if 'radio_option' not in st.session_state:
    st.session_state.radio_option = 2021
  radio = st.radio("Wybierz Rok"
           , options=[2020, 2021]
           , horizontal= True
           , key='radio_option')
  st.write('radio_option = ', st.session_state.radio_option)



############################################################################################################################################





left, right = st.columns(2)

with left:
  @st.cache_data
  def left_bar_chart2 (year1):
    left_bar_chart = feederwatch[['species_code', 'Year', 'how_many']]
    left_bar_chart[left_bar_chart['Year'] == year1]
    return left_bar_chart
  st.bar_chart(left_bar_chart2(st.session_state.radio_option), x='species_code', y='how_many', use_container_width=True)

with right:
  @st.cache_data
  def right_line_chart2 (year1):
    right_line_chart = feederwatch[["Month", "Year","how_many"]]
    right_line_chart[right_line_chart['Year'] == year1]
    return right_line_chart

  st.line_chart(right_line_chart2(st.session_state.radio_option), x='Month', y='how_many', use_container_width=True) 

###########################################################################################################################################

#df_table = feederwatch[]


#tabele pod spodem 
if radio == 2021:
  st.dataframe(feederwatch.query('Year == 2021'))
else:
  st.dataframe(feederwatch.query('Year == 2020'))

##########################################################################################################################################
map_chart_data = feederwatch[['latitude', 'longitude']]

st.map(map_chart_data,
       zoom=3,
       use_container_width=True)