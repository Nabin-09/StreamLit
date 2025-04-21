import streamlit as st

st.title("Hello Nabin Bhai!")
st.subheader("Kaise ho?!")
st.text("Welcome to first interactive app")
st.write("Choose one")

chai = st.selectbox("Your fav chai : ",["Masala Chai" , "Lemon Chai" , "Adrak Chai" , "Kesar chai"])
st.write(f"You chose {chai} . Excellent Choice")
st.success("Chai ban chuki hai")