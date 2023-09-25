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

from PIL import Image
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from streamlit_js_eval import get_browser_language



st.markdown("<h1 style='text-align: center; color: black;'>부산 EXPO 관광지 추천 </h1>", unsafe_allow_html=True)



# 부산 중심 좌표
center_lat, center_lon = 35.1594965345398, 129.162576586723

# Folium 지도 객체 생성
st.title('해운대의 지도')

m = folium.Map(location=[35.1795543, 129.0756416], zoom_start=11)

st_data = st_folium(m, width=725)


st.title('해운대의 주소')
st.write('부산광역시 해운대구')

