import streamlit as st
import pandas as pd #to read the dataset (.csv)

st.title('🤖 Machine Learning Application')
st.info('This Application builds a Machine Learning Application using Streamlit!')

#using expander - dropdown
with st.expander('Data'):
  st.write('**Raw data**')
  df= pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df #to display the dataset

  #adding variables
  st.write('**X**')
  X= df.drop('species' , axis =1)
  X #display X

  st.write('**y**')
  y=df.species
  y
  


