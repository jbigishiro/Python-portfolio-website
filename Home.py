import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)


with col1:
    st.image("images/justin.jpg")

with col2:
    st.title("Justin Bigishiro")
    content = """"
    Hey, I am Justin! I am a software Engineer. 
    I graduated in 2011 with a bachelor's degree in Electronics Engineering. 
    I have been a high school teacher form 2012 to 2016 in Rwanda.
    In 2023, I decided to change the career to Software Engineering. 
    I am enjoying with different skills I have acquired since.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3,empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")