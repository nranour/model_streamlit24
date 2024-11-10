import streamlit as st
import pandas as pd
import pickle

st.image("http://www.ehtp.ac.ma/images/lo.png")

st.title("MSDE6 : ML Course")
st.header("Iris Flower Prediction App")
st.markdown("This app predicts Iris flower type")
select=st.selectbox('How would you like to use the prediction model ?', ['Imput parameters directly', 'Load a file of data'])

st.header("User Imput parameters")


st.sidebar.title("Iris Flower")

st.sidebar.image("https://cdn.britannica.com/39/91239-004-44353E32/Diagram-flowering-plant.jpg")


st.sidebar.title("User Imput parameters")
sep_l=st.sidebar.slider('Sepal lenght',0,10)
sep_w=st.sidebar.slider('Sepal with',0,6)
pet_l=st.sidebar.slider('Petal lenght',0,10)
pet_w=st.sidebar.slider('Petal with',0,3)

if select == 'Imput parameters directly':
    data = pd.DataFrame([sep_l,sep_w,pet_l,pet_w]).T
    

st.table(data)


model = pickle.load(open(r"C:\Users\nrano\Desktop\Projet_Big_Data\02_Labs\10_deploiement\Streamlit\modeliris6.pkl",'rb'))
type = model.predict(data)

st.write(type)

#streamlit community Cloud




    