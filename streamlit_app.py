import streamlit as st
import pandas as pd #to read the dataset (.csv)
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('🤖 Machine Learning Application')
st.info('This Application builds a Machine Learning Application using Streamlit!')

#using expander - dropdown to display RAW Dataset
with st.expander('Data'):
  st.write('**Raw data**')
  df= pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df #to display the dataset

  #adding variables
  st.write('**X**')
  X_raw= df.drop('species' , axis= 1) #excluding species col=1
  X_raw #display X

  st.write('**y**')
  y_raw=df.species #Only species Col
  y_raw

#Data Visualization
with st.expander('Data visualization'):
  #"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  #st.scatter_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, size=None, width=None, height=None, use_container_width=True)
  st.scatter_chart(data=df, x = 'bill_length_mm', y = 'body_mass_g', color = 'species')
  
# Input Features
with st.sidebar:
  st.header('Input features')
  #st.selectbox(label, options...)
  island = st.selectbox('island', ('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('Gender', ('Female', 'Male'))
  #st.slider(label, min_value=None, max_value=None, value=None (we are using Avg Value))
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.64, 43.9)
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper Length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body Mass (g)', 2700.0, 6300.0, 4207.0)

  

  # Creating a  dataframe for the input features
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}
  input_df = pd.DataFrame(data, index=[0])
  #Combining it to the original dataset
  input_penguins = pd.concat([input_df, X_raw], axis= 0)
  
with st.expander('**Input Features**'):
  st.write('**Input Penguin**')
  input_df
  st.write('**Combined input Penguin data with the orginal penguins Data**')
  input_penguins

#Data Preparation
#Encode X
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix =encode)

x= df_penguins[1:] #except 1st row
input_row = df_penguins[:1] #only first row

#Encode Y
target_mapper = {'Adelie':0,
                'Chinstrap':1,
                'Gentoo': 2}
#Custom function: 
def target_encode(val):
  return target_mapper[val]

y=y_raw.apply(target_encode)

with st.expander('Data Preparation'):
  st.write('**Encoded X(Input Penguin)**')
  input_row
  st.write('**Encoded Y**')
  y

#Model Training and inference

##Train the Ml MOdel
clf = RandomForestClassifier()
clf = clf.fit(x, y)

##Apply model to make Predictions
pred = clf.predict(input_row)
pred_prob = clf.predict_proba(input_row)

df_pred_prob = pd.DataFrame(pred_prob)
df_pred_prob.columns =['Adelie', 'Chinstrap', 'Gentoo']
df_pred_prob.rename(columns={0:'Adelie', 1:'Chinstrap', 2:'Gentoo'})


#Display Predicticted Species
st.subheader('Predicted species')
st.dataframe(df_pred_prob,
             column_config={
              "Adelie": st.column_config.ProgressColumn(
                "Adelie",
                width = 'medium',
                format="%f",
                min_value=0,
                max_value=1,
              ),
               "Chinstrap": st.column_config.ProgressColumn(
                "Chinstrap",
                width = 'medium',
                format="%f",
                min_value=0,
                max_value=1,
               ),
               "Gentoo": st.column_config.ProgressColumn(
                "Gentoo",
                width = 'medium',
                format="%f",
                min_value=0,
                max_value=1,
               ),
    }, hide_index= True)
df_pred_prob

penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(str(penguins_species[pred][0]))





  
  
  
  
  



