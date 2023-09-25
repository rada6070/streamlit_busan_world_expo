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



assets.import_assets("assets/style.css", st)


st.markdown("<h1 style='text-align: center; color: black;'>부산 EXPO 관광지 추천 </h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1 :
    col11, col12, col13 = st.columns([1,6,1])

    with col11 :
        st.write(' ')

    with col12 :
        st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.facebook.com%2Fbusanworldexpo2030%2Fevents%2F%3Flocale%3Dda_DK&psig=AOvVaw3aKQWCRcP-dcUyxJ7seRvl&ust=1695747425465000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCNjkjcmdxoEDFQAAAAAdAAAAABAk', width=85)

    with col13 :
        st.write(' ')

with col2 :
    st.write('1')

df = pd.read_excel("data.xlsx")

def tourist_data():
    spots_df = df[df['분류'] == '관광지']
    spots_df = spots_df.reset_index(drop=True)
    Q0 = spots_df['질문']
    P0 = spots_df['장소']
    A0 = spots_df['답변']
    latitude0 = spots_df['위도']
    longitude0 = spots_df['경도']
    return Q0, P0, A0, latitude0, longitude0

def restaurant_data():
    spots_df = df[df['분류'] == '음식점']
    spots_df = spots_df.reset_index(drop=True)
    Q1 = spots_df['질문']
    P1 = spots_df['장소']
    A1 = spots_df['답변']
    latitude1 = spots_df['위도']
    longitude1 = spots_df['경도']
    return Q1, P1, A1, latitude1, longitude1

def nature_data():
    spots_df = df[df['분류'] == '자연/공원']
    spots_df = spots_df.reset_index(drop=True)
    Q2 = spots_df['질문']
    P2 = spots_df['장소']
    A2 = spots_df['답변']
    latitude2 = spots_df['위도']
    longitude2 = spots_df['경도']
    return Q2, P2, A2, latitude2, longitude2

def cafe_data():
    spots_df = df[df['분류'] == '카페/디저트']
    spots_df = spots_df.reset_index(drop=True)
    Q3 = spots_df['질문']
    P3 = spots_df['장소']
    A3 = spots_df['답변']
    latitude3 = spots_df['위도']
    longitude3 = spots_df['경도']
    return Q3, P3, A3, latitude3, longitude3

def expect_data():
    spots_df = df[df['분류'] == '기대효과']
    spots_df = spots_df.reset_index(drop=True)
    Q4 = spots_df['질문']
    P4 = spots_df['장소']
    A4 = spots_df['답변']
    latitude4 = spots_df['위도']
    longitude4 = spots_df['경도']
    return Q4, P4, A4, latitude4, longitude4

def expo_data():
    spots_df = df[df['분류'] == '엑스포']
    spots_df = spots_df.reset_index(drop=True)
    Q5 = spots_df['질문']
    P5 = spots_df['장소']
    A5 = spots_df['답변']
    latitude5 = spots_df['위도']
    longitude5 = spots_df['경도']
    return Q5, P5, A5, latitude5, longitude5


#반복문으로 만들 수 있을것 처럼 보임
Q0, P0, A0, latitude0, longitude0 = tourist_data()
Q1, P1, A1, latitude1, longitude1 = restaurant_data()
Q2, P2, A2, latitude2, longitude2 = nature_data()
Q3, P3, A3, latitude3, longitude3 = cafe_data()
Q4, P4, A4, latitude4, longitude4 = expect_data()
Q5, P5, A5, latitude5, longitude5 = expo_data()



tourist_btn_clicked = st.button(f'{Q0[0]}', key='tourist_btn')
restaurant_btn_clicked = st.button(f'{Q1[0]}', key='restaurant_btn')
nature_btn_clicked = st.button(f'{Q2[0]}', key='nature_btn')
cafe_btn_clicked = st.button(f'{Q3[0]}', key='cafe_btn')
expect_btn_clicked = st.button(f'{Q4[0]}', key='expect_btn')
expo_btn_clicked = st.button(f'{Q5[0]}', key='expo_btn')
expo_next_btn_clicked = st.button('다음 답변', key='expo_next_btn')
expo_back_btn_clicked = st.button('이전 답변', key='expo_back_btn')

i = st.session_state.get('i', 0)
x = st.session_state.get('x', 0)
y = st.session_state.get('y', 0)



# 관광지 버튼
if tourist_btn_clicked:
    i = 0
    x = P0
    y = A0
    st.session_state['i'] = i
    st.session_state['x'] = P0
    st.session_state['y'] = A0
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")
        
# 음식점 버튼
if restaurant_btn_clicked:
    i = 0
    x = P1
    y = A1
    st.session_state['x'] = P1
    st.session_state['y'] = A1
    st.session_state['i'] = i
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")
    
# 자연/공원 버튼
if nature_btn_clicked:
    i = 0
    x = P2
    y = A2
    st.session_state['x'] = P2
    st.session_state['y'] = A2
    st.session_state['i'] = i
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")

# 카페/디저트 버튼
if cafe_btn_clicked:
    i = 0
    x = P3
    y = A3
    st.session_state['x'] = P3
    st.session_state['y'] = A3
    st.session_state['i'] = i
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")

# 기대효과 버튼
if expect_btn_clicked:
    i = 0
    x = P4
    y = A4
    st.session_state['x'] = P4
    st.session_state['y'] = A4
    st.session_state['i'] = i
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")

# 엑스포 버튼
if expo_btn_clicked:
    i = 0
    x = P5
    y = A5
    st.session_state['x'] = P5
    st.session_state['y'] = A5
    st.session_state['i'] = i
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")
    
    
if expo_next_btn_clicked: #다음 버튼
    if i >= len(x) -1 :
        i = len(x) -1
        st.warning('마지막입니다.')
    else :
        i += 1
        st.session_state['i'] = i
        st.success(f"장소: {x[i]}")
        st.info(f"답변: {y[i]}") 
        
           
if expo_back_btn_clicked: #이전 버튼
    if i <= 0 :
        i = 0
        st.warning('처음입니다.')
    else:
        i -= 1
        st.session_state['i'] = i
        st.success(f"장소: {x[i]}")
        st.info(f"답변: {y[i]}")
        
# 부산 중심 좌표
center_lat, center_lon = 35.1594965345398, 129.162576586723

# Folium 지도 객체 생성
st.title('해운대의 지도')

m = folium.Map(location=[35.162336558296, 129.17479991912842], zoom_start=14)

folium.Marker(location=[35.162336558296, 129.17479991912842]).add_to(m)

st_data = st_folium(m, width=725)


st.title('해운대의 주소')
st.write('부산광역시 해운대구')

