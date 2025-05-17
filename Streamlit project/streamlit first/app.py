import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.write("Hello everyone, this is streamlit write.")
st.title("this is title")
st.markdown("this is markdown")
st.header("this is image header")
st.image("lotus.webp",caption="Lotus")
st.subheader("this is subheader")
st.caption("this is caption")
st.code("this is code")
st.latex("this is latex")



st.checkbox("yes")
st.button("click me")
st.radio("Enter your gender", ["Male", "Female"])
st.selectbox("Select your hobbies", ["Reading", "Travels", "Playing", "Dancing", "Singing"])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)



st.number_input('Pick a number', 0, 9)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')



st.balloons()


st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))



st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")


with st.container():
  st.write("This is inside the container")



st.title("From Here Visualization")

df = pd.DataFrame({
  'Items' : ["Mobile", "Laptop", "PC", "Keyboard"],
  'Price' : [900,1800, 1300, 100]
})

st.bar_chart(df)


st.title("Display map")

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [28.39, 84.12], columns=['lat', 'lon'])
st.map(df)


