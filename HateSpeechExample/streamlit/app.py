import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn import pipeline
import warnings
warnings.filterwarnings("ignore")

st.title('Hate Speech Detection Streamlit App')

#add a SIDE BAR
st.sidebar.header("Side Bar Example")
st.sidebar.text("Hate Speech")

#load model 
model_filename = "./model/hatespeech.joblib.z"
clf = joblib.load(model_filename)
#st.write(type(clf)) : <class 'sklearn.pipeline.Pipeline'>


#add input text 
c_text = st.text_area("Enter Text","Type Here in english please  (:  ")

if st.button('Analyse'):
	c_result_bis = c_text.split()
	probas = clf.predict_proba(c_result_bis)[0]
	result_predict = {
	'hate speech': probas[0], 
	'offensive language': probas[1], 
	'neither': probas[2]
	}
	st.success(result_predict)
else : 
	st.write("Press le button  (: ")

 
