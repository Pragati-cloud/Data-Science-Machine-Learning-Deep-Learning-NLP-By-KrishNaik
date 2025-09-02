import streamlit as st
import pandas as pd
import numpy as np

# title of app
st.title("My First Streamlit App")

# simple text
st.write("Hello, welcome to my app!")

#create dataframe
df = pd.DataFrame({
  'first column':[1,2,3,4],
  'second column':[10,20,30,40]
})

#display dataframe
st.write("This is my dataframe:")
st.write(df)


#create a line chart
chart_data = pd.DataFrame(
  np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)