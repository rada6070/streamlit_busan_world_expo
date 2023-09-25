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



st.markdown("<h1 style='text-align: center; color: black;'>부산 EXPO 관광지 추천 </h1>", unsafe_allow_html=True)


df = pd.read_excel("data.xlsx")
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

i = st.session_state.get('i', 0)

if f_btn_clicked:
    i = 0
    st.session_state['i'] = i
    st.write(f"장소: {P[i]}")
    st.write(f"답변: {A[i]}")
    st.write(f"위도: {latitude[i]}")
    st.write(f"경도: {longitude[i]}")
    
if n_btn_clicked:
    i += 1
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

