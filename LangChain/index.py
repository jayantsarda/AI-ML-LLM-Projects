import streamlit as st
import langchainHelper

st.title("Restaurant name generator")
cuisine = st.sidebar.selectbox("Pick  a Cuisine", ("Indian", "Italian", "Mexican", "Arabic"))

if cuisine:
    response = langchainHelper.generate_restaurent_name_and_menu_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_item = response['menu_items'].strip().split(',')
    st.write("*** MENU ***")
    for item in menu_item:
        st.write("- " , item)