import streamlit as st
import pandas as pd
from datetime import datetime
import time
from pathlib import Path
import os


def calendario():

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

    if st.button("Trova sovrapposizioni", type="primary"):
        salvato = st.success('Nessuna sovrapposizione', icon="✅")
        time.sleep(3) 
        salvato.empty()


def upload_docs():
    st.title("Carica PDF")

    uploaded_file = st.file_uploader("Carica una circolare in formato PDF", type=['pdf'])

    if uploaded_file is not None:
        save_folder = "pdfs"  # Replace with your desired folder path
        save_path = Path(save_folder, uploaded_file.name)

        with open(save_path, mode='wb') as f:
            f.write(uploaded_file.getvalue())

        st.success(f"File '{uploaded_file.name}' saved successfully!")
    else:
        st.info("Please upload a PDF file.")


def search_docs():

    # Create a text input for search terms
    search_term = st.text_input("Inserisci i termini della ricerca:")

    # Create a button to trigger the search functionality
    if st.button("Cerca"):
        # Implement your search logic here using the search_term variable
        # This could involve filtering data, displaying search results, etc.
        st.write(f"Ricerca in corso: '{search_term}'")  # Placeholder for search results


        pdf_filenames = []
        for filename in os.listdir('pdfs'):
            if filename.lower().endswith(".pdf"):  # Check for lowercase and uppercase extensions
                pdf_filenames.append(filename)
                
        # Display title
        st.title("Risultati")

        # Loop to display three results
        for i in range(len(pdf_filenames)):
            container = st.container(border=True)

            # Create columns
            col1, col2 = container.columns( [1, 4])  # You can also specify width ratios as a list (e.g., [2, 1])

            # Use the columns for your content
            with col1:
                col1.write(pdf_filenames[i])

            with col2:
                col2.write("*descrizione*")
            
        





