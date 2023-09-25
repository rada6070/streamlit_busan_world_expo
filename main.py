import io
import matplotlib
import folium

import streamlit as st
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt

import i18n
import style
import assets
import data
import requests
import json
import random
import openpyxl

from PIL import Image
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from streamlit_js_eval import get_browser_language

try:
    preferred_language = i18n.FindLangByTag(get_browser_language())
except AttributeError:
    preferred_language = "ko"

assets.import_assets("assets/style.css", st)


st.markdown("<h1 style='text-align: center; color: black;'>부산 EXPO 관광지 추천 </h1>", unsafe_allow_html=True)

col1, col2 = columns(2)

with col1 :
    col11, col12, col13 = columns([1,6,1])

    with col11 :
        st.write(' ')

    with col12 :
        st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.facebook.com%2Fbusanworldexpo2030%2Fevents%2F%3Flocale%3Dda_DK&psig=AOvVaw3aKQWCRcP-dcUyxJ7seRvl&ust=1695747425465000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCNjkjcmdxoEDFQAAAAAdAAAAABAk', width=85)

    with col13 :
        st.write(' ')

with col2 :
    language_list = list(i18n.LangList().keys())
    language_select = str(
        st.selectbox("Change Language", ["브라우저 기본 설정", *language_list])
    )
    
    if language_select == "브라우저 기본 설정":
        language = i18n.LoadLangByCode(preferred_language)
    else:
        language = i18n.LoadLangByCode(i18n.LangList(language_select))

    


df = pd.read_excel("C:/Users/USER/Desktop/data.xlsx")

def bring_data():
    spots_df = df[df['분류'] == '엑스포']
    spots_df = spots_df.reset_index(drop=True)
    Q = spots_df['질문']
    P = spots_df['장소']
    A = spots_df['답변']
    latitude= spots_df['위도']
    longitude = spots_df['경도']
    return Q, P, A, latitude, longitude
Q, P, A, latitude, longitude = bring_data()


f_btn_clicked = st.button(f'{Q[0]}', key='test_btn')
n_btn_clicked = st.button('next', key='next_btn')
b_btn_clicked = st.button('back', key='back_btn')

i = st.session_state.get('i', 0)

if f_btn_clicked:
    i = 0
    st.session_state['i'] = i
    st.write(f"장소: {P[i]}")
    st.write(f"답변: {A[i]}")
    st.write(f"위도: {latitude[i]}")
    st.write(f"경도: {longitude[i]}")
    
    
if n_btn_clicked:
    if i >= 4 :
        i = 4
        print('마지막입니다.')
    elif i < 0 :
        i = 0
        st.warning('처음입니다.')
    else :
        i += 1
        st.session_state['i'] = i
        st.write(f"장소: {P[i]}")
        st.write(f"답변: {A[i]}")
        st.write(f"위도: {latitude[i]}")
        st.write(f"경도: {longitude[i]}")

    
    
if b_btn_clicked:
    if i > 4 :
        i = 4
        st.warning('마지막입니다.')
    if i <= 0 :
        i = 0
        st.warning('처음입니다.')
    else:
        i -= 1
        st.session_state['i'] = i
        st.write(f"장소: {P[i]}")
        st.write(f"답변: {A[i]}")
        st.write(f"위도: {latitude[i]}")
        st.write(f"경도: {longitude[i]}")



# 부산 중심 좌표
center_lat, center_lon = 35.1594965345398, 129.162576586723

# Folium 지도 객체 생성
st.title('해운대의 지도')

m = folium.Map(location=[35.162336558296, 129.17479991912842], zoom_start=14)

folium.Marker(location=[35.162336558296, 129.17479991912842]).add_to(m)

st_data = st_folium(m, width=725)


st.title('해운대의 주소')
st.write('부산광역시 해운대구')

