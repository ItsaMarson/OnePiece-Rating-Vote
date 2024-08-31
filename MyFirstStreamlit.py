import streamlit as st
import pandas as pd
import numpy as np

col1, col2, col3 = st.columns(3)
st.title("Hello World")
# Initialize session state for ratings at the start of the script
if 'ratings' not in st.session_state:
    st.session_state['ratings'] = {
        "Luffy": 0,
        "Nami": 0,
        "Robin": 0,
        "Zoro": 0,
        "Usopp": 0,
        "Franky": 0,
        "Jinbie": 0,
        "Sanji": 0,
        "Chopper": 0,
        "Brook": 0
    }


def update_rating(character):
    st.session_state['ratings'][character] += 1
    st.toast(f"Thank you for rating {character}!")



st.sidebar.title("One Piece Character Favorite")
st.sidebar.markdown("Straw Hat Crew")

text = st.sidebar.text_area("Please Inpur your Name")
if st.sidebar.button("Click to State Your Name"):
    st.toast(f"Hello {text}, please vote wisely!")

# Col 1
with col1:  
    luffy = "Pictures/luffy.jpeg"
    nami = "Pictures/Nami.jpeg"
    robin = "Pictures/Robin.jpeg"

    with st.container():
        st.image(luffy, use_column_width=True)
        st.markdown("Monkey D. Luffy")
        st.write("3,000,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b1'):
            update_rating("Luffy")

    with st.container():
        st.image(nami, use_column_width=True)
        st.markdown("Nami")
        st.write("366,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b4'):
            update_rating("Nami")

    with st.container():
        st.image(robin, use_column_width=True)
        st.markdown("Nico Robin")
        st.write("930,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b7'):
            update_rating("Robin")

# Col 2
with col2:
    zoro = "Pictures/zoro.jpeg"
    usopp = "Pictures/Usopp.jpeg"
    franky = "Pictures/Franky.jpeg"
    jinbie = "Pictures/Jinbie.jpeg"

    with st.container():
        st.image(zoro, use_column_width=True)
        st.markdown("Ronoroa Zoro")
        st.write("1,111,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b2'):
            update_rating("Zoro")

    with st.container():
        st.image(usopp, use_column_width=True)
        st.markdown("God Usopp")
        st.write("500,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b5'):
            update_rating("Usopp")

    with st.container():
        st.image(franky, use_column_width=True)
        st.markdown("Franky")
        st.write("394,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b8'):
            update_rating("Franky")

    with st.container():
        st.image(jinbie, use_column_width=True)
        st.markdown("Jinbie")
        st.write("1,100,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b10'):
            update_rating("Jinbie")

# Col 3
with col3:
    sanji = "Pictures/Sanji.jpeg"
    chopper = "Pictures/Chopper.jpg"
    brook = "Pictures/Brook.jpg"

    with st.container():
        st.image(sanji, use_column_width=True)
        st.markdown("Vinsmoke Sanji")
        st.write("1,032,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b3'):
            update_rating("Sanji")

    with st.container():
        st.image(chopper, use_column_width=True)
        st.markdown("Tony Tony Chopper")
        st.write("1,000 Bounty")
        if st.button("Click Me to Rate!", key='b6'):
            update_rating("Chopper")

    with st.container():
        st.image(brook, use_column_width=True)
        st.markdown("Brook")
        st.write("383,000,000 Bounty")
        if st.button("Click Me to Rate!", key='b9'):
            update_rating("Brook")

st.sidebar.markdown("# Total Ratings")
for character, count in st.session_state['ratings'].items():
    st.sidebar.write(f"{character}: {count}")

tocontact = st.sidebar.selectbox("How would you like to Contacted?", ("","Email", "Mobile Phone Number"))
if tocontact:
    st.toast("Hi Thank you for Donations " +tocontact)

    
