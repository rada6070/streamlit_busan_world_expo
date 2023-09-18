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

from PIL import Image
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from streamlit_js_eval import get_browser_language

df_e = {
    '해운대': {
        '좋아요': 910,
        '싫어요': 129,
    },
    '해동용궁사': {
        '좋아요': 780,
        '싫어요': 133,
    },
    '오륙도': {
        '좋아요': 798,
        '싫어요': 389,
    },
    '남포동': {
        '좋아요': 1075,
        '싫어요': 111,
    },
    '동백섬': {
        '좋아요': 735,
        '싫어요': 140,
    },
}

df_r = {
    '진양호횟집': {
        '좋아요': 977,
        '싫어요': 98,
    },
    '이재모피자': {
        '좋아요': 1010,
        '싫어요': 96,
    },
    '솔내음한정식': {
        '좋아요': 1224,
        '싫어요': 79,
    },
    '가야밀면': {
        '좋아요': 1382,
        '싫어요': 80,
    },
    '선창횟집': {
        '좋아요': 1240,
        '싫어요': 101,
    },
}

# 넓은 화면 모드
st.set_page_config(layout="wide")


# 브라우저 기본 언어 불러오기
try:
    preferred_language = i18n.FindLangByTag(get_browser_language())
except AttributeError:
    preferred_language = "ko"


# 스타일 시트 불러오기
assets.import_assets("assets/style.css", st)


# 언어 선택
language_list = list(i18n.LangList().keys())
language_select = str(
    st.sidebar.selectbox("Change Language", ["브라우저 기본 설정", *language_list])
)

if language_select == "브라우저 기본 설정":
    language = i18n.LoadLangByCode(preferred_language)
else:
    language = i18n.LoadLangByCode(i18n.LangList(language_select))


# 사이드바 생성
with st.sidebar:
    choose = option_menu(
        language["side_bar_main"],
        [
            language["side_bar_sub_1"],
            language["side_bar_sub_2"],
            language["side_bar_sub_3"],
            language["side_bar_sub_4"],
        ],
        icons=["house", "map", "bar-chart", "bar-chart"],
        menu_icon="bi bi-menu-up",
        default_index=0,
        styles=style.sidebar,
    )

    st.image(
        "https://i.namu.wiki/i/tvGyhYywWMsAcu6DB_LNqDgXsPeaXzDt4Su8mc8pckqINu1ceRlXh6mqVaquCFE9vCBk9Pduf9xkzWr0gcC_Ng.svg",
        use_column_width=False,
    )


if choose == language["side_bar_sub_1"]:
    # 페이지 제목과 부산 월드 엑스포 2030 로고 이미지 표시
    st.title(language["side_bar_sub_1"])
    st.image(
        "https://image.edaily.co.kr/images/Photo/files/NP/S/2022/06/PS22062300100.jpg",
        use_column_width=True,
    )

    # 월드 엑스포 2030에 대한 간단한 설명 추가
    st.write(language["page_1_explain_1"])

    # 주요 행사 정보 표시
    st.subheader(language["page_1_subheader_1"])
    st.write(language["page_1_explain_when"])
    st.write(language["page_1_explain_where"])
    st.write(language["page_1_explain_thema"])

    # 부산 월드 엑스포 2030 관련 이미지 표시
    st.subheader(language["page_1_image_gall"])
    image_urls = [
        "https://thumb.mt.co.kr/06/2021/11/2021110114172440715_1.jpg/dims/optimize/https://thumb.mt.co.kr/06/2021/11/2021110114172440715_1.jpg/dims/optimize/",
        "https://thumb.mtstarnews.com/06/2023/04/2023040312452334740_1.jpg/dims/optimizehttps://thumb.mtstarnews.com/06/2023/04/2023040312452334740_1.jpg/dims/optimize",
        "https://newsroom-prd-data.s3.ap-northeast-2.amazonaws.com/wp-content/uploads/2022/11/%EC%97%91%EC%8A%A4%ED%8F%AC-%EC%B9%BC%EB%9F%BC_%EC%97%91%EC%8A%A4%ED%8F%AC%EA%B0%80-%EB%AA%B0%EA%B3%A0-%EC%98%A8-%EB%86%80%EB%9D%BC%EC%9A%B4-%EB%B3%80%ED%99%94_04.png",
    ]

    # 이미지 갤러리를 가로로 표시
    st.image(image_urls, width=200)

    # 월드 엑스포에 대한 정보를 더 자세히 보여주는 링크 제공
    st.subheader(language["page_1_subheader_2"])
    st.write(language["page_1_explain_2"])
    st.write("[www.expo2030busan.kr](https://www.expo2030busan.kr/index.do)")

if choose == language["side_bar_sub_2"]:

    col1, col2= st.columns([3,2])
    
    # 지도 생성
    
    with col1 :
        st.title(language["side_bar_sub_2"])
        m = folium.Map(location=[35.1795543, 129.0756416], zoom_start=16)

        st_data = st_folium(m, width=725)
        
    with col2 :
        st.title('부산 명소 리스트')

        st.write('관광지 리스트')
        st.dataframe(df_e, width=570)

        st.write('맛집 리스트')
        st.dataframe(df_r, width=570)

        option = st.selectbox(
            '장소 선정',
            ('해운대', '해동용궁사', '오륙도', '남포동', '동백섬',
             '진양호횟집', '이재모피자', '솔내음한정식', '가야밀면','선창횟집')
        )

if choose == language["side_bar_sub_3"]:
    st.title(language["side_bar_sub_3"])

    st.image("https://ifh.cc/g/DpHp4Z.png", use_column_width=True)


if choose == language["side_bar_sub_4"]:
    st.title(language["side_bar_sub_4"])

    st.image("https://ifh.cc/g/vhAAG2.png", use_column_width=True)
