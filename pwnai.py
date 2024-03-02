import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="PWNAI", page_icon=":robot_face:")

@st.cache
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

data = load_data('https://raw.githubusercontent.com/NoDataFound/PwnAI/main/assets/platforms/PWNAI_Services%20-%20Hosted.csv')

st.sidebar.header("Select services to compare")
selected_services = st.sidebar.multiselect("Select services", options=data['Service'].unique())

sidebar_image_url = 'https://github.com/NoDataFound/PwnAI/blob/main/assets/artwork/PWNAI_logo_main.png'  
main_image_url = 'https://github.com/NoDataFound/PwnAI/blob/main/assets/artwork/PwnAI_Logo_5.png'  

st.sidebar.image(sidebar_image_url, caption='Sidebar Image', use_column_width=True)
st.image(main_image_url, caption='Main Image', use_column_width=True)

if selected_services:
    filtered_data = data[data['Service'].isin(selected_services)]
    st.write(filtered_data)
else:
    st.write("Please select at least one service to compare.")
