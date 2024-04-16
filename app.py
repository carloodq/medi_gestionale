import streamlit as st
import pandas as pd
from datetime import datetime
import time
from tabs import calendario, upload_docs, search_docs

st.title("App Gestionale Liceo Medi")

# Create the tabs
tab1, tab2, tab3 = st.tabs(["Calendario", "Carica Circolari", "Ricerca Circolari"])

# Content for each tab
with tab1:
  calendario()


with tab2:
   upload_docs()

with tab3:
   search_docs()





