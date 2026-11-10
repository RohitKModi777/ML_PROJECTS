import pickle
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from win32com.client import Dispatch
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

model = pickle.load(open("spam.pkl","rb"))
cv = pickle.load(open('vectorizer.pkl','rb'))


def main():
    st.title('Email Spam Classification App')
    st.write("Build with Streamlit & Python")
    activities = ["Classification","About"]
    choices = st.sidebar.selectbox("Select activites",activities)
    if choices =="Classification":
        st.subheader('Classification')
        msg =st.text_input('Enter a text')
        if st.button("Process"):
            print(msg)
            print(type(msg))
            data =[msg]
            print(data)
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            if result[0]==0:
                st.success("This is Not A Spam Email")
                speak("This is Not A Spam Email")
            else:
                st.error("This is A Spam Email")    
                speak("This is A Spam Email")

main()