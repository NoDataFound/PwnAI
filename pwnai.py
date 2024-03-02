import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide", page_title="PWNAI", page_icon=":robot_face:")

st.cache_data()
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Load data
data = load_data('https://raw.githubusercontent.com/NoDataFound/PwnAI/main/assets/platforms/PWNAI_Services%20-%20Hosted.csv')

# Initialize or load session state for the scoreboard
if 'scoreboard' not in st.session_state:
    st.session_state['scoreboard'] = {service: 0 for service in data['Service'].unique()}




sidebar_image_url = 'https://raw.githubusercontent.com/NoDataFound/PwnAI/main/assets/artwork/PWNAI_logo_main.png'  
st.sidebar.image(sidebar_image_url, width=200,use_column_width='always')

selected_services = st.sidebar.multiselect("Select services", options=data['Service'].unique())


col1, col2 = st.columns([3, 1])

with col1:
    st.code("""
            
            ░█▄█░▄▀▄░█░░▒█░░░▀█▀░▄▀▄░░░█▄█▒▄▀▄░▄▀▀░█▄▀
▒█▒█░▀▄▀░▀▄▀▄▀▒░░▒█▒░▀▄▀▒░▒█▒█░█▀█░▀▄▄░█▒█

- 𝚂𝚎𝚕𝚎𝚌𝚝 𝚂𝚎𝚛𝚟𝚒𝚌𝚎𝚜 𝚒𝚗 𝚜𝚒𝚍𝚎𝚋𝚊𝚛
- 𝙴𝚗𝚝𝚎𝚛 𝚂𝚎𝚊𝚛𝚌𝚑 𝚀𝚞𝚎𝚛𝚢
- 𝙿𝚛𝚎𝚜𝚜 нα¢к 𝚋𝚞𝚝𝚝𝚘𝚗
            
""",)
with col2:
    hack_button = st.button("нα¢к")


st.markdown("----")

query = st.text_input("", placeholder="Enter your query here", label_visibility="hidden")

    


if selected_services and query:
    filtered_data = data[data['Service'].isin(selected_services)]
    st.write(filtered_data)
else:
    st.write("ᴩʟᴇᴀꜱᴇ ꜱᴇʟᴇᴄᴛ ᴀᴛ ʟᴇᴀꜱᴛ ᴏɴᴇ ꜱᴇʀᴠɪᴄᴇ ᴛᴏ ᴄᴏᴍᴩᴀʀᴇ.")

# Query input and button
if hack_button:
    with st.spinner(f"Sending '{query}' to the following services: {', '.join(selected_services)}"):
        time.sleep(2)  # Simulate a task
        for service in selected_services:
            st.session_state['scoreboard'][service] += 1
    st.success("Query sent successfully!")

# Display the scoreboard
st.sidebar.header("█▓▒▒░░░ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ░░░▒▒▓█")
scoreboard_df = pd.DataFrame(list(st.session_state['scoreboard'].items()), columns=['Service', 'Queries'])
scoreboard_df = scoreboard_df.sort_values(by="Queries", ascending=False)
st.sidebar.write(scoreboard_df)