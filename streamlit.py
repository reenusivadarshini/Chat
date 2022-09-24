import streamlit as st
from streamlit_chat import message as st_message
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from PIL import Image
image = Image.open('Mental Health (1).png')

st.sidebar.image(image)

image = Image.open('header.png')

st.image(image, caption=' ')


@st.experimental_singleton
def get_models():
    # it may be necessary for other frameworks to cache the model
    # seems pytorch keeps an internal state of the conversation
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model


if "history" not in st.session_state:
    st.session_state.history = []

st.title("Talk To The Bot")


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.freecreatives.com/wp-content/uploads/2016/01/Pink-Abstract-Floral-Background.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 



def generate_answer():
    tokenizer, model = get_models()
    user_message = st.session_state.input_text
    inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
    result = model.generate(**inputs)
    message_bot = tokenizer.decode(
        result[0], skip_special_tokens=True
    )  # .replace("<s>", "").replace("</s>", "")

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})


st.text_input("", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat)  # unpacking
 

for i in st.session_state.history:
    print(i)



st.write(st.session_state.history)
import tweepy
from  textblob import TextBlob 
import pandas as pd
import numpy as np
import re

consumer_key = "pTivamyKt0GtxZiFizMMhsouj"
consumer_sec = "HEkXmzyaALIAD1AfTHLdRnegC8rstIY2AUHbrzvRGIjoJl3PCo"

# from proxy server we need to connect
access_token = "1490018179690602500-6dR6g69GHBE1fMZICvqyDMKrJINNyS"
access_token_sec = "ZAjbICteZd6FsbWEHeP2SIlmmdIycSEvgoOfJaXjf9wTs"
dir(tweepy)

auth=tweepy.OAuthHandler(consumer_key,consumer_sec)

auth.set_access_token(access_token,access_token_sec)

api_connect=tweepy.API(auth)

auth = tweepy.OAuthHandler(consumer_key,consumer_sec)
auth.set_access_token(access_token,access_token_sec)
api = tweepy.API(auth)



def getPolarity(text):
   return  TextBlob(text).sentiment.polarity



for i in st.session_state.history:
    score=getPolarity(i)
    if(score<0):
        st.header("Sentimental Analysis of Tweets")
        st.header("The person is depressed!!!")
    else:
        st.header("Sentimental Analysis of Tweets")
        st.header("The person is not depressed!!")
    
 

    
