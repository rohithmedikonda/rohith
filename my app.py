import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1, col2 = st.columns(2)
with col1:
  st.subheader("r0 cat")
  st.image("./r0.jpg", caption="Persian Cat", width=300,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.subheader("R1 Cat")
  st.image("./r1.jpg", caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("Ragdoll cats are proud")
