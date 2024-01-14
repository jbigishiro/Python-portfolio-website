import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/justin.jpg", width=300)

with col2:
    st.title("Justin Bigishiro")
    content = """"
    Hey, I am Justin! I am a software Engineer. 
    I graduated in 2011 with a bachelor's degree in Electronics Engineer. 
    I have been a high school teacher form 2012 to 2016 in Rwanda.
    In 2023, I decided to change the career to Software Engineering. 
    I am enjoying with different skills I have acquired since.
    """
    st.info(content)