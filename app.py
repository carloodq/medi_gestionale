import streamlit as st
import pandas as pd
st.title("App Gestionale Liceo Medi")
from datetime import datetime
import time

import streamlit as st

data_df = pd.read_csv("calendario_medi.csv")

data_df['inizio'] = data_df['inizio'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
data_df['fine'] = data_df['fine'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

updated_df = st.data_editor(
    data_df,
    column_config={
        "inizio": st.column_config.DatetimeColumn(
            "Inizio",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="YYYY-MM-DD HH:mm",
            step=60,
        ),
                "fine": st.column_config.DatetimeColumn(
            "Fine",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="YYYY-MM-DD HH:mm",
            step=60,
        ),
    },
    hide_index=True,
    num_rows="dynamic"

)

if st.button("Salva", type="primary"):
    updated_df = updated_df.dropna()
    updated_df.to_csv("calendario_medi.csv", index = False)
    salvato = st.success('Salvato', icon="✅")
    time.sleep(3) 
    salvato.empty()




