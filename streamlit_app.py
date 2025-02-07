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
  X= df.drop('species' , axis =1) #excluding species col=1
  X #display X

  st.write('**y**')
  y=df.species #Only species Col
  y 

#Data Visualization
with st.expander('Data visualization'):
  #"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  #st.scatter_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, size=None, width=None, height=None, use_container_width=True)
  st.scatter_chart(data=df, x = 'bill_length_mm', y = 'body_mass_g', color = 'species')
  


