import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of tiger")

col1, col2 = st.columns(2)
with col1:
  st.subheader("r0 tiger")
  st.image("./r0.jpg", caption=" r0 tiger", width=300,use_column_width=True)
  st.write("r0 tigers are cute")
with col2:
  st.subheader("R1 Cat")
  st.image("./r1.jpg", caption="r1 tiger", width=300,use_column_width=True)
  st.write("r1 tigers are proud")
