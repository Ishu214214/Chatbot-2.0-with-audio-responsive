import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask ,render_template , request
import nltk
from nltk.chat.util import Chat
from flask_ngrok import run_with_ngrok
from gtts import gTTS
import IPython

qa_pairs = [    [ 'what is your owner name' ,                               ['ishu'] ]  ,
                [ '(.*)name' ,                                              [ 'ishu kumar' ] ]  ,           
                [ 'what is your favourate colour' ,                         ['black'] ]  ,
                [ 'what is your age'              ,                         [ '12' ] ]                     ,
                [ 'what is your favourate book'    ,                        ['Java'] ]        ,
                [ 'what is your favourate food' ,                           [ 'chiken' ] ]      ,                                      
                [ 'what is your creater' ,                                  [ 'ishu kumar' ] ]       ,       
                [ 'what is the favourate colour of your owner' ,            ['black'] ]    ,            
                [ '(hi|HI|Hi|hey|HEY|Hey|HELLO|Hello|hello)',               [' \t hello 👋 \n how can i help u'  ,  '👋 '] ] ,            
                [ '(.*)(location|city|address|place|Place) ?',              ['khagaria bihar']   ]   ,
                [ '(.*)contact(.*)' ,                                       ['call - 7004718739 for more information ℹ '] ]   ,
                [  '(.*)weather(.*)' ,                                      ['it cool 😎 ']    ] ,
                [ '(.*)',                                                   ['sorry']  ]
                
            ]

cb = Chat(qa_pairs)



def predict_note_authentication(UserID):

  
  response= cb.respond(UserID)

 
  tts=gTTS(response)
  tts.save('demo.wav')
  sound_file='demo.wav'
  
  audio_file = open("demo.wav", "rb")
  st.audio(audio_file.read())
  



  
  return response


def main():
    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Chatbot 2.0</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.header("Ask Qustions")
    UserID = st.text_input("Ask","")

    resul=""

    if st.button("ASk"):
      result=predict_note_authentication(UserID)
      st.success(' {}'.format(result))

    if st.button("About Me"):
      st.subheader("Developed by Ishu kumar")
      st.subheader(" Department of Computer Engineering")

if __name__=='__main__':
  main()
   
